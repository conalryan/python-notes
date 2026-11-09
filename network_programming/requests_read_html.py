"""Requests remains useful for synchronous HTTP; HTTPX also supports async clients."""


def main() -> None:
    import requests

    # Explicit connect/read timeouts and context-scoped cleanup are important in
    # Requests too. This request runs only when the exercise is executed directly.
    with requests.get("https://www.python.org", timeout=(3, 10)) as response:
        response.raise_for_status()
        print(response.headers["content-type"])
        # response.text uses the response encoding; slicing bytes can split UTF-8.
        print(response.text[:200])


if __name__ == "__main__":
    main()
