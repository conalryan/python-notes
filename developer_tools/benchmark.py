"""Benchmark comparable operations with fresh state rather than a growing list."""

from timeit import repeat


def append_loop() -> list[int]:
    values = []
    for index in range(10_000):
        values.append(index)
    return values


def comprehension() -> list[int]:
    return [index for index in range(10_000)]


def main() -> None:
    assert append_loop() == comprehension()
    for operation in (append_loop, comprehension):
        # Each call builds its own list. Timeit setup runs once per timing trial,
        # so putting a mutable list there would keep growing it across iterations.
        timings = repeat(operation, number=100, repeat=5)
        print(f"{operation.__name__}: {min(timings) / 100:.6f}s per call")
    # For DSP, include Python/Rust conversions, allocations, and device copies in
    # benchmarks. A tight loop benchmark alone does not prove a real-time speedup.


if __name__ == "__main__":
    main()
