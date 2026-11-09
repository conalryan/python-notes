"""Structured concurrency: sibling tasks belong to a lifetime, not the background."""

import asyncio
from collections.abc import Awaitable, Callable, Sequence


async def map_bounded[Item, Result](
    items: Sequence[Item],
    operation: Callable[[Item], Awaitable[Result]],
    *,
    concurrency: int = 4,
) -> list[Result]:
    """A fixed worker pool bounds both running work and task creation."""
    if concurrency < 1:
        raise ValueError("concurrency must be positive")
    pending = iter(enumerate(items))
    results: dict[int, Result] = {}

    async def worker() -> None:
        # next() and assignment run without an await, so event-loop tasks cannot
        # interleave inside them. This is not a thread-safe iterator pattern.
        for index, item in pending:
            results[index] = await operation(item)

    async with asyncio.TaskGroup() as group:
        for worker_index in range(min(concurrency, len(items))):
            group.create_task(worker(), name=f"worker-{worker_index}")
    # TaskGroup cancels siblings if one fails, then raises an ExceptionGroup.
    return [results[index] for index in range(len(items))]


async def main() -> None:
    async def load_metadata(name: str) -> str:
        # to_thread suits blocking I/O. It does not make a Python DSP loop parallel;
        # cancelling its await also cannot forcibly stop an already-running thread.
        return await asyncio.to_thread(str.upper, name)

    # The caller owns the deadline, so it can cover several composed operations.
    async with asyncio.timeout(10):
        print(await map_bounded(["voice", "drums", "bass"], load_metadata))


if __name__ == "__main__":
    asyncio.run(main())
