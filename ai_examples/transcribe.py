"""Local speech inference; model loading and downloading are explicit CLI actions."""

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Segment:
    start: float
    end: float
    text: str


def transcribe(path: Path, *, model_name: str = "tiny.en") -> list[Segment]:
    path = path.resolve(strict=True)
    if not path.is_file():
        raise ValueError("input must be an audio file")
    # faster-whisper decodes through PyAV and resamples for Whisper internally.
    # CPU int8 is a portable starting point; do not claim CUDA or MPS support here.
    from faster_whisper import WhisperModel

    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    segments, _info = model.transcribe(str(path), beam_size=1, vad_filter=True)
    # Inference is lazy: consuming the generator actually runs the model.
    return [Segment(segment.start, segment.end, segment.text.strip()) for segment in segments]


def main() -> None:
    parser = argparse.ArgumentParser(description="Transcribe a local audio file on the CPU")
    parser.add_argument("source", type=Path)
    parser.add_argument(
        "--model", default="tiny.en", help="Model identifier or local model directory"
    )
    arguments = parser.parse_args()
    print(
        json.dumps(
            [
                asdict(segment)
                for segment in transcribe(arguments.source, model_name=arguments.model)
            ],
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
