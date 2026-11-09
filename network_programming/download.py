"""An opt-in file download with bounded size, explicit timeouts, and no shell."""

import argparse
from pathlib import Path

import httpx


def download(
    client: httpx.Client, url: str, destination: Path, *, max_bytes: int = 10_000_000
) -> int:
    if max_bytes <= 0:
        raise ValueError("max_bytes must be positive")
    if httpx.URL(url).scheme != "https":
        raise ValueError("use HTTPS for downloads")
    written = 0
    created = False
    try:
        with client.stream("GET", url) as response:
            response.raise_for_status()
            with destination.open("xb") as output:
                created = True
                for chunk in response.iter_bytes(chunk_size=64 * 1024):
                    written += len(chunk)
                    if written > max_bytes:
                        raise ValueError("download exceeds the configured size limit")
                    output.write(chunk)
    except BaseException:
        # Only remove a file this call created, including on interruption. Never
        # remove an existing destination when exclusive creation fails.
        if created:
            destination.unlink(missing_ok=True)
        raise
    return written


def main() -> None:
    parser = argparse.ArgumentParser(description="Download an explicitly chosen HTTPS asset")
    parser.add_argument("url")
    parser.add_argument("destination", type=Path)
    parser.add_argument("--max-bytes", type=int, default=10_000_000)
    arguments = parser.parse_args()
    # Redirects are not automatically trusted; TLS verification stays enabled.
    with httpx.Client(timeout=httpx.Timeout(10, connect=3), follow_redirects=False) as client:
        size = download(client, arguments.url, arguments.destination, max_bytes=arguments.max_bytes)
    print(f"Downloaded {size} bytes")


if __name__ == "__main__":
    main()
