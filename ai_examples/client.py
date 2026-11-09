"""HTTPX uses resource-scoped connection pooling and validates remote JSON."""

import asyncio
import os

import httpx

from ai_examples.service import AudioWindow, Levels
from modern_python.concurrency import map_bounded


async def analyze_remote(client: httpx.AsyncClient, window: AudioWindow) -> Levels:
    response = await client.post("/analyze", json=window.model_dump())
    response.raise_for_status()
    # Parsing JSON is not validation. Validate even if the remote API is typed.
    return Levels.model_validate(response.json())


async def main() -> None:
    # Keep this origin controlled by configuration, not a user-supplied URL.
    origin = os.environ.get("AUDIO_API_URL", "http://127.0.0.1:8000")
    async with httpx.AsyncClient(
        base_url=origin,
        timeout=httpx.Timeout(10, connect=3),
        limits=httpx.Limits(max_connections=4),
    ) as client:
        windows = [AudioWindow(samples=[0.0, 0.25, -0.25], sample_rate=16_000)]

        async def request(window: AudioWindow) -> Levels:
            return await analyze_remote(client, window)

        # A total deadline complements HTTPX's individual network-operation timeouts.
        async with asyncio.timeout(10):
            results = await map_bounded(windows, request)
        for levels in results:
            print(levels.model_dump_json())


if __name__ == "__main__":
    asyncio.run(main())
