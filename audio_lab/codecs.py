"""FFmpeg handles codecs; Python handles orchestration, not handwritten encoders."""

import shutil
import subprocess
from pathlib import Path


def export(source: Path, destination: Path) -> None:
    codecs = {
        ".wav": ["-c:a", "pcm_s24le"],
        ".mp3": ["-c:a", "libmp3lame", "-b:a", "192k"],
        ".m4a": ["-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart"],
        ".mp4": ["-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart"],
    }
    if destination.suffix.lower() not in codecs:
        raise ValueError("choose .wav, .mp3, .m4a, or .mp4")
    source = source.resolve(strict=True)
    destination = destination.resolve()
    if source == destination:
        raise ValueError("source and destination must differ")
    executable = shutil.which("ffmpeg")
    if executable is None:
        raise RuntimeError("FFmpeg is required; on macOS install it with brew install ffmpeg")
    # No shell, no stdin prompts, no implicit overwrite, and a bounded wait.
    command = [
        executable,
        "-nostdin",
        "-hide_banner",
        "-loglevel",
        "error",
        "-n",
        "-i",
        str(source),
        "-map",
        "0:a:0",
        "-vn",
        *codecs[destination.suffix.lower()],
        str(destination),
    ]
    subprocess.run(command, check=True, capture_output=True, timeout=120)
