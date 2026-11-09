"""A small typed API boundary for a frontend audio interface, not an ML model."""

from math import fsum, log10, sqrt

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field


class AudioWindow(BaseModel):
    # Unlike a TypeScript cast, Pydantic rejects invalid data at runtime.
    model_config = ConfigDict(extra="forbid", allow_inf_nan=False, strict=True)
    samples: list[float] = Field(min_length=1, max_length=16_000)
    sample_rate: int = Field(ge=8_000, le=192_000)


class Levels(BaseModel):
    model_config = ConfigDict(extra="forbid", allow_inf_nan=False, strict=True)
    frames: int = Field(gt=0)
    duration: float = Field(gt=0)
    peak: float = Field(ge=0)
    rms: float = Field(ge=0)
    rms_dbfs: float | None


app = FastAPI(title="Audio window analysis")


@app.post("/analyze", response_model=Levels)
def analyze(window: AudioWindow) -> Levels:
    # Bound sample amplitude as well as length so squaring cannot overflow.
    # This is a mono PCM window; a MediaRecorder WebM blob is not a sample list.
    peak = max(abs(sample) for sample in window.samples)
    if peak > 1:
        from fastapi import HTTPException

        raise HTTPException(status_code=422, detail="samples must be normalized PCM in [-1, 1]")
    rms = sqrt(fsum(sample * sample for sample in window.samples) / len(window.samples))
    return Levels(
        frames=len(window.samples),
        duration=len(window.samples) / window.sample_rate,
        peak=peak,
        rms=rms,
        rms_dbfs=20 * log10(rms) if rms > 0 else None,
    )


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
