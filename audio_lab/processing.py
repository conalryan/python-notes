"""Small offline DSP examples; NumPy/SciPy do the numerical heavy lifting."""

from dataclasses import dataclass
from math import gcd, isfinite
from pathlib import Path

import soundfile as sf
from numpy.typing import NDArray
from scipy.signal import resample_poly

import numpy as np

type Samples = NDArray[np.float32]


@dataclass(frozen=True, slots=True)
class Audio:
    samples: Samples
    sample_rate: int

    def __post_init__(self) -> None:
        if (
            isinstance(self.sample_rate, bool)
            or not isinstance(self.sample_rate, int)
            or self.sample_rate <= 0
        ):
            raise ValueError("sample_rate must be a positive integer")
        raw = np.asarray(self.samples)
        if raw.ndim != 2 or min(raw.shape) == 0 or raw.dtype.kind != "f":
            raise ValueError("samples must be a nonempty floating-point (frames, channels) array")
        # Copy once at the boundary so edits cannot accidentally change a source clip.
        samples = np.array(raw, dtype=np.float32, copy=True)
        if not np.isfinite(samples).all():
            raise ValueError("samples must be finite")
        samples.setflags(write=False)
        object.__setattr__(self, "samples", samples)

    @property
    def duration(self) -> float:
        return len(self.samples) / self.sample_rate

    @property
    def channels(self) -> int:
        return self.samples.shape[1]

    @property
    def peak(self) -> float:
        return float(np.max(np.abs(self.samples)))


def load(path: Path) -> Audio:
    # always_2d avoids a special mono shape; float reads scale integer PCM correctly.
    samples, sample_rate = sf.read(path, dtype="float32", always_2d=True)
    return Audio(samples, sample_rate)


def tone(frequency: float, seconds: float, *, sample_rate: int = 48_000) -> Audio:
    if not isfinite(seconds) or not 0 < seconds <= 60:
        raise ValueError("tone duration must be between 0 and 60 seconds")
    if not isfinite(frequency) or not 0 < frequency < sample_rate / 2:
        raise ValueError("frequency must be below the Nyquist limit")
    # endpoint=False is equivalent here to arange / rate: no duplicated end sample.
    times = np.arange(round(seconds * sample_rate), dtype=np.float64) / sample_rate
    samples = (0.2 * np.sin(2 * np.pi * frequency * times)).astype(np.float32)
    return Audio(samples[:, None], sample_rate)


def trim(audio: Audio, start: float, stop: float) -> Audio:
    if not all(isfinite(value) for value in (start, stop)):
        raise ValueError("trim times must be finite")
    if not 0 <= start < stop <= audio.duration:
        raise ValueError("trim must lie inside the clip")
    # Seconds become nearest frame boundaries; stop is exclusive, like a Python slice.
    return Audio(
        audio.samples[round(start * audio.sample_rate) : round(stop * audio.sample_rate)],
        audio.sample_rate,
    )


def gain(audio: Audio, decibels: float) -> Audio:
    if not isfinite(decibels) or not -120 <= decibels <= 60:
        raise ValueError("gain must be finite and between -120 and 60 dB")
    # Amplitude uses 20 log10; power would use 10 log10. Do not clip during mixing.
    return Audio(audio.samples * 10 ** (decibels / 20), audio.sample_rate)


def fade(audio: Audio, seconds: float = 0.01) -> Audio:
    if not isfinite(seconds) or not 0 <= seconds <= audio.duration / 2:
        raise ValueError("fade must fit within half the clip")
    frames = round(seconds * audio.sample_rate)
    envelope = np.ones(len(audio.samples), dtype=np.float32)
    if frames:
        envelope[:frames] = np.linspace(0, 1, frames, dtype=np.float32)
        envelope[-frames:] = np.linspace(1, 0, frames, dtype=np.float32)
    return Audio(audio.samples * envelope[:, None], audio.sample_rate)


def pan(audio: Audio, position: float) -> Audio:
    if audio.channels != 1 or not isfinite(position) or not -1 <= position <= 1:
        raise ValueError("pan requires mono input and a position between -1 and 1")
    angle = (position + 1) * np.pi / 4
    # Constant-power pan keeps L^2 + R^2 constant as a mono source moves across stereo.
    weights = np.array([np.cos(angle), np.sin(angle)], dtype=np.float32)
    return Audio(audio.samples * weights, audio.sample_rate)


def resample(audio: Audio, sample_rate: int) -> Audio:
    if isinstance(sample_rate, bool) or not isinstance(sample_rate, int) or sample_rate <= 0:
        raise ValueError("sample_rate must be a positive integer")
    if sample_rate == audio.sample_rate:
        return audio
    divisor = gcd(sample_rate, audio.sample_rate)
    # Polyphase filtering removes frequencies that would alias when downsampling.
    samples = resample_poly(
        audio.samples, sample_rate // divisor, audio.sample_rate // divisor, axis=0
    )
    return Audio(samples, sample_rate)


@dataclass(frozen=True, slots=True)
class Track:
    audio: Audio
    start: float = 0
    decibels: float = 0


def mix(tracks: list[Track]) -> Audio:
    if not tracks:
        raise ValueError("mix needs at least one track")
    reference = tracks[0].audio
    offsets = []
    for track in tracks:
        if (track.audio.sample_rate, track.audio.channels) != (
            reference.sample_rate,
            reference.channels,
        ):
            raise ValueError("resample and align channels before mixing")
        if not isfinite(track.start) or track.start < 0:
            raise ValueError("track start must be finite and nonnegative")
        offsets.append(round(track.start * reference.sample_rate))
    frames = max(
        offset + len(track.audio.samples) for offset, track in zip(offsets, tracks, strict=True)
    )
    output = np.zeros((frames, reference.channels), dtype=np.float32)
    for offset, track in zip(offsets, tracks, strict=True):
        output[offset : offset + len(track.audio.samples)] += gain(
            track.audio, track.decibels
        ).samples
    return Audio(output, reference.sample_rate)


def normalize_peak(audio: Audio, target_dbfs: float = -1) -> Audio:
    if not isfinite(target_dbfs) or not -120 <= target_dbfs <= 0:
        raise ValueError("target must be finite and between -120 and 0 dBFS")
    if audio.peak == 0:
        return audio
    # Dividing samples first avoids overflowing a float32 gain for subnormal input.
    return Audio((audio.samples / audio.peak) * 10 ** (target_dbfs / 20), audio.sample_rate)


def write_wav(audio: Audio, path: Path) -> None:
    if audio.peak > 1:
        raise ValueError("PCM export would clip; reduce gain or normalize the master")
    # Exclusive creation protects recordings. PCM_24 is an interchange master;
    # float32 in memory does not automatically select the file's bit depth.
    with (
        path.open("xb") as file,
        sf.SoundFile(
            file,
            mode="w",
            samplerate=audio.sample_rate,
            channels=audio.channels,
            format="WAV",
            subtype="PCM_24",
        ) as output,
    ):
        output.write(audio.samples)
