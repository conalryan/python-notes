"""Call Rust DSP from Python and keep file/codec orchestration in Python."""

import argparse
from pathlib import Path

import numpy as np
from audio_lab.processing import Audio, tone, write_wav


def render(path: Path) -> None:
    # Build/install rust_audio first. This is intentionally optional, not a fallback
    # that would silently claim a Rust speedup while executing Python instead.
    import rusty_audio

    source = tone(440, 1)
    samples = rusty_audio.gain(source.samples.ravel().tolist(), -3.0)
    normalized = rusty_audio.normalize(samples, -1.0)
    output = np.asarray(normalized, dtype=np.float32).reshape(source.samples.shape)
    write_wav(Audio(output, source.sample_rate), path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a WAV using native Rust DSP")
    parser.add_argument("output", type=Path)
    render(parser.parse_args().output)


if __name__ == "__main__":
    main()
