"""Run with python -m modern_python.language; no third-party dependencies needed."""

from collections.abc import Callable, Iterable, Iterator
from dataclasses import dataclass, field, replace
from enum import StrEnum
from functools import wraps
from itertools import batched
from math import isfinite
from time import perf_counter
from typing import Protocol

# A type alias describes intent without introducing a runtime wrapper.
type Samples = tuple[float, ...]


class Format(StrEnum):
    WAV = "wav"
    MP3 = "mp3"


@dataclass(frozen=True, slots=True, kw_only=True)
class Clip:
    """Immutable metadata; keyword-only construction avoids swapped arguments."""

    name: str
    sample_rate: int = 48_000
    tags: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        # An annotation alone would happily accept a negative number at runtime.
        if isinstance(self.sample_rate, bool) or not isinstance(self.sample_rate, int):
            raise TypeError("sample_rate must be an integer")
        if self.sample_rate <= 0:
            raise ValueError("sample_rate must be positive")


class Effect(Protocol):
    """Like a TypeScript structural interface; inheritance is not required."""

    def process(self, samples: Samples) -> Samples: ...


@dataclass(frozen=True, slots=True)
class Gain:
    decibels: float

    def process(self, samples: Samples) -> Samples:
        if not isfinite(self.decibels):
            raise ValueError("gain must be finite")
        multiplier = 10 ** (self.decibels / 20)
        return tuple(sample * multiplier for sample in samples)


def apply_effect(samples: Samples, effect: Effect) -> Samples:
    return effect.process(samples)


def blocks(samples: Iterable[float], size: int = 4) -> Iterator[Samples]:
    """Lazy batching bounds working memory; the final block may be shorter."""
    yield from batched(samples, size)


def export_description(command: dict[str, object]) -> str:
    # Matching destructures a mapping; it is not a general JSON schema validator.
    match command:
        case {"format": "wav", "bits": 16 | 24 as bits}:
            return f"Uncompressed PCM, {bits}-bit"
        case {"format": "mp3"}:
            return "Lossy MP3; keep a WAV master"
        case _:
            raise ValueError("unsupported export command")


def timed[**Parameters, Result](
    function: Callable[Parameters, Result],
) -> Callable[Parameters, Result]:
    """PEP 695 generics preserve a wrapped callable's parameter and result types."""

    @wraps(function)
    def wrapper(*args: Parameters.args, **kwargs: Parameters.kwargs) -> Result:
        started = perf_counter()
        try:
            return function(*args, **kwargs)
        finally:
            # finally runs on success and failure; never return here and hide an error.
            print(f"{function.__name__}: {perf_counter() - started:.6f}s")

    return wrapper


def main() -> None:
    clip = Clip(name="voice", tags=("dialogue",))
    print(replace(clip, name="voice-edited"))
    print(apply_effect((0.1, -0.2, 0.3), Gain(-6)))
    print(list(blocks(range(9))))
    print(export_description({"format": "wav", "bits": 24}))
    # strict=True catches misaligned parallel data rather than silently truncating it.
    print(dict(zip(("left", "right"), (0.8, 0.6), strict=True)))


if __name__ == "__main__":
    main()
