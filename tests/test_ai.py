"""Test HTTP contracts locally; never request a remote service or download a model."""

import asyncio
from pathlib import Path
from types import SimpleNamespace

import pytest

httpx = pytest.importorskip("httpx")
pytest.importorskip("pydantic")
pytest.importorskip("fastapi")

from pydantic import ValidationError

from ai_examples.client import analyze_remote
from ai_examples.service import AudioWindow, app
from ai_examples.transcribe import Segment, transcribe


def post_window(payload: dict[str, object]) -> httpx.Response:
    async def request() -> httpx.Response:
        # ASGITransport exercises the app in-process without a socket or a server.
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://testserver"
        ) as client:
            return await client.post("/analyze", json=payload)

    return asyncio.run(request())


def test_api_levels_and_silence() -> None:
    response = post_window({"samples": [0.5, -0.5], "sample_rate": 16_000})
    assert response.status_code == 200
    result = response.json()
    assert result["rms"] == 0.5 and result["peak"] == 0.5
    assert result["rms_dbfs"] == pytest.approx(-6.0206)
    assert post_window({"samples": [0.0], "sample_rate": 16_000}).json()["rms_dbfs"] is None


@pytest.mark.parametrize(
    "payload",
    [
        {"samples": [], "sample_rate": 16_000},
        {"samples": [0.1], "sample_rate": "16000"},
        {"samples": [2.0], "sample_rate": 16_000},
        {"samples": [0.1] * 16_001, "sample_rate": 16_000},
        {"samples": [0.1], "sample_rate": 16_000, "unexpected": True},
    ],
)
def test_api_rejects_invalid_pcm(payload: dict[str, object]) -> None:
    assert post_window(payload).status_code == 422


def test_remote_json_is_validated() -> None:
    async def scenario() -> None:
        transport = httpx.MockTransport(lambda request: httpx.Response(200, json={"rms": "oops"}))
        async with httpx.AsyncClient(
            transport=transport, base_url="https://example.test"
        ) as client:
            with pytest.raises(ValidationError):
                await analyze_remote(client, AudioWindow(samples=[0.0], sample_rate=16_000))

    asyncio.run(scenario())


def test_transcription_consumes_lazy_segments(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    import sys

    calls = []

    class FakeModel:
        def __init__(self, name, **options):
            calls.append((name, options))

        def transcribe(self, path, **options):
            def segments():
                yield SimpleNamespace(start=0.0, end=1.0, text=" hello ")

            return segments(), None

    monkeypatch.setitem(sys.modules, "faster_whisper", SimpleNamespace(WhisperModel=FakeModel))
    source = tmp_path / "voice.wav"
    source.touch()
    assert transcribe(source) == [Segment(0.0, 1.0, "hello")]
    assert calls == [("tiny.en", {"device": "cpu", "compute_type": "int8"})]
