"""Opt-in, bounded-memory recording. Nothing opens a microphone on import."""

from math import isfinite
from pathlib import Path


def record(
    path: Path,
    *,
    seconds: float = 5,
    sample_rate: int = 48_000,
    channels: int = 1,
    device: int | str | None = None,
    block_size: int = 1024,
) -> int:
    """Write bounded blocks and return the number of reads reporting overflow."""
    if not isfinite(seconds) or not 0 < seconds <= 3600:
        raise ValueError("recording duration must be between 0 and 3600 seconds")
    for value in (sample_rate, channels, block_size):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError("sample rate, channels, and block size must be positive integers")
    remaining = round(seconds * sample_rate)
    if not remaining:
        raise ValueError("recording must contain at least one frame")

    # Optional native libraries are imported only when recording is requested.
    import sounddevice as sd
    import soundfile as sf

    sd.check_input_settings(
        device=device, channels=channels, samplerate=sample_rate, dtype="float32"
    )
    overflow_count = 0
    # Blocking mode avoids doing file I/O inside a real-time callback. This is
    # a recorder, not a monitor; slow disks can still cause reported overflows.
    with (
        path.open("xb") as file,
        sf.SoundFile(
            file,
            mode="w",
            samplerate=sample_rate,
            channels=channels,
            format="WAV",
            subtype="PCM_24",
        ) as output,
        sd.InputStream(
            samplerate=sample_rate,
            channels=channels,
            device=device,
            dtype="float32",
            blocksize=block_size,
        ) as stream,
    ):
        while remaining:
            frames = min(block_size, remaining)
            samples, overflowed = stream.read(frames)
            output.write(samples)
            overflow_count += int(overflowed)
            remaining -= frames
    return overflow_count
