"""Python 3.14-only runtime APIs; the module can still be imported on 3.12/3.13."""

import sys


def latest_features() -> dict[str, object]:
    if sys.version_info < (3, 14):
        raise RuntimeError("run this example with Python 3.14 or newer")

    from functools import Placeholder, partial
    from string.templatelib import Interpolation, Template
    from uuid import uuid7

    from annotationlib import Format, get_annotations
    from compression import zstd

    def label(name: str) -> str:
        return name.upper()

    session_id = uuid7()
    # On 3.14, t"session={session_id}" creates the same kind of Template object.
    # Constructing it explicitly keeps this module parseable on earlier versions.
    template = Template("session=", Interpolation(session_id, "session_id"), "")
    payload = b"audio session metadata " * 100
    compressed = zstd.compress(payload)
    square = partial(pow, Placeholder, 2)
    return {
        "annotations": get_annotations(label, format=Format.STRING),
        "session_uuid_version": session_id.version,
        "template_parts": len(list(template)),
        "compression_round_trip": zstd.decompress(compressed) == payload,
        "partial_result": square(4),
    }


def main() -> None:
    print(latest_features())
    from concurrent.futures import InterpreterPoolExecutor

    # Each worker has isolated imports/state and its own interpreter. Calls/results
    # are serialized; arbitrary NumPy or ML extensions may not support this yet.
    with InterpreterPoolExecutor(max_workers=2) as workers:
        print(list(workers.map(sum, [[1, 2, 3], [4, 5, 6]])))


if __name__ == "__main__":
    main()
