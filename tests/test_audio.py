"""Synthetic signals keep editing tests deterministic and hardware-free."""

import subprocess
from pathlib import Path

import pytest

np = pytest.importorskip("numpy")
sf = pytest.importorskip("soundfile")
pytest.importorskip("scipy")

from audio_lab.codecs import export
from audio_lab.processing import (
    Audio,
    Track,
    fade,
    gain,
    load,
    mix,
    normalize_peak,
    pan,
    resample,
    tone,
    trim,
    write_wav,
)
from audio_lab.record import record


def test_editing_is_non_destructive_and_sample_accurate() -> None:
    source = Audio(np.full((100, 1), 0.25, dtype=np.float32), 100)
    edited = fade(trim(source, 0.1, 0.9), 0.1)
    assert len(edited.samples) == 80
    assert edited.samples[0, 0] == edited.samples[-1, 0] == 0
    np.testing.assert_array_equal(source.samples, 0.25)
    assert gain(source, -6).peak == pytest.approx(0.25 * 10 ** (-6 / 20))


def test_mix_offsets_headroom_pan_and_resampling() -> None:
    mono = Audio(np.full((4, 1), 0.75, dtype=np.float32), 4)
    mixed = mix([Track(mono), Track(mono, start=0.5)])
    np.testing.assert_allclose(mixed.samples[:, 0], [0.75, 0.75, 1.5, 1.5, 0.75, 0.75])
    assert normalize_peak(mixed).peak == pytest.approx(10 ** (-1 / 20))
    stereo = pan(mono, 0)
    np.testing.assert_allclose(
        np.sum(stereo.samples**2, axis=1), mono.samples[:, 0] ** 2, rtol=1e-6
    )
    converted = resample(tone(440, 0.1), 16_000)
    assert converted.samples.shape == (1600, 1)
    assert converted.sample_rate == 16_000


def test_silence_and_wav_round_trip(tmp_path: Path) -> None:
    silence = Audio(np.zeros((100, 2), dtype=np.float32), 48_000)
    assert normalize_peak(silence).peak == 0
    quiet = Audio(np.full((4, 1), np.nextafter(np.float32(0), np.float32(1))), 48_000)
    assert normalize_peak(quiet).peak == pytest.approx(10 ** (-1 / 20))
    path = tmp_path / "master.wav"
    write_wav(silence, path)
    assert sf.info(path).subtype == "PCM_24"
    assert load(path).samples.shape == (100, 2)
    with pytest.raises(OSError, match="File exists"):
        write_wav(silence, path)
    with pytest.raises(ValueError, match="clip"):
        write_wav(Audio(np.full((4, 1), 2, dtype=np.float32), 48_000), tmp_path / "clip.wav")


def test_invalid_audio_and_edit_boundaries() -> None:
    for samples in (
        np.zeros((0, 1)),
        np.zeros(4),
        np.array([[float("nan")]]),
        np.ones((2, 1), dtype=int),
    ):
        with pytest.raises(ValueError):
            Audio(samples, 48_000)
    mono = tone(440, 0.1)
    with pytest.raises(ValueError):
        trim(mono, -1, 0.01)
    with pytest.raises(ValueError):
        pan(mono, 2)
    with pytest.raises(ValueError):
        mix([Track(mono), Track(resample(mono, 16_000))])
    with pytest.raises(ValueError):
        mix([Track(mono, start=float("nan"))])
    with pytest.raises(ValueError):
        normalize_peak(mono, 1)


def test_export_uses_argument_vector_and_codec(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    source = tmp_path / "input with spaces.wav"
    source.touch()
    calls = []
    monkeypatch.setattr("audio_lab.codecs.shutil.which", lambda name: "/usr/bin/ffmpeg")
    monkeypatch.setattr(
        "audio_lab.codecs.subprocess.run",
        lambda command, **options: calls.append((command, options)),
    )
    export(source, tmp_path / "output.mp4")
    command, options = calls[0]
    assert "aac" in command and "-nostdin" in command and "-n" in command
    assert str(source.resolve()) in command
    assert options == {"check": True, "capture_output": True, "timeout": 120}
    with pytest.raises(ValueError):
        export(source, source)
    with pytest.raises(ValueError):
        export(source, tmp_path / "output.exe")


def test_recording_writes_exact_frames_and_reports_overflow(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    sd = pytest.importorskip("sounddevice")

    class FakeStream:
        def __init__(self, **options):
            self.options = options

        def __enter__(self):
            return self

        def __exit__(self, *error):
            return False

        def read(self, frames):
            return np.zeros((frames, 1), dtype=np.float32), True

    monkeypatch.setattr(sd, "check_input_settings", lambda **options: None)
    monkeypatch.setattr(sd, "InputStream", FakeStream)
    path = tmp_path / "recording.wav"
    assert record(path, seconds=0.1, sample_rate=100, block_size=4) == 3
    assert sf.info(path).frames == 10
    with pytest.raises(ValueError):
        record(tmp_path / "invalid.wav", seconds=-1)


@pytest.mark.parametrize("suffix,codec", [(".mp3", "mp3"), (".m4a", "aac"), (".mp4", "aac")])
def test_real_codec_round_trip_when_ffmpeg_is_available(
    tmp_path: Path, suffix: str, codec: str
) -> None:
    import json
    import shutil

    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        pytest.skip("FFmpeg and ffprobe are optional system dependencies")
    source = tmp_path / "master.wav"
    destination = tmp_path / f"encoded{suffix}"
    write_wav(pan(tone(440, 0.1), 0), source)
    export(source, destination)
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_streams", "-of", "json", str(destination)],
        capture_output=True,
        check=True,
        timeout=10,
    )
    stream = json.loads(result.stdout)["streams"][0]
    assert stream["codec_name"] == codec
    assert stream["channels"] == 2
