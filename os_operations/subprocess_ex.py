"""A bounded external command without a shell; ps is a Unix-specific utility."""

import subprocess


def main() -> None:
    # run handles resource cleanup; check raises on failure, and timeout bounds waits.
    result = subprocess.run(
        ["ps", "-U", "0"], capture_output=True, text=True, check=True, timeout=10
    )
    print(result.stdout)


if __name__ == "__main__":
    main()
