# Python and Rust Audio

This crate uses Rust 2024 edition (Rust 1.85+) and current PyO3 0.30 APIs.
Install the stable Rust toolchain with [rustup](https://rustup.rs/) or your
package manager, then run from the repository root:

```sh
uv sync --extra audio
uv pip install ./rust_audio
uv run --no-sync pytest tests/test_native.py
mkdir -p output
uv run --no-sync python -m audio_lab.native output/rust-master.wav
cargo test --manifest-path rust_audio/Cargo.toml
cargo run --release --manifest-path rust_audio/Cargo.toml --bin render -- output/rust-tone.wav
uv run --no-sync python -m audio_lab export output/rust-master.wav output/rust-master.mp3
```

`maturin` is the Python build backend and invokes Cargo to compile a native wheel.
The extension module name must match the library and `#[pymodule]` name. Use
`uv run --no-sync` after manually installing the extension; an exact `uv sync`
can remove packages not declared in the root project. Reinstall after source
changes. For iterative release builds, activate `.venv` and use
`uv tool run maturin develop --release --manifest-path rust_audio/Cargo.toml --features python`.
Commit the generated Cargo lockfile to reproduce the standalone demo.

## What the Boundary Teaches

- Rust `&[f32]` borrows input, `Vec<f32>` owns output, and `Result` exposes errors.
  `?` propagates failures; Python bindings translate them into `ValueError`.
- PyO3 extracts Python lists into owned vectors, then `Python::detach` permits
  other Python threads to run while Rust computes. No Python APIs run detached.
- This intentionally simple boundary copies in both directions. It is **not
  zero-copy** or guaranteed faster than vectorized NumPy. Benchmark whole calls,
  not just Rust loops, and amortize boundary overhead across useful blocks.
- For larger buffers, learn rust-numpy's array APIs and ndarray layouts. Shared
  mutable NumPy storage can race even when Python's GIL is held; establish
  ownership, copy, or synchronization before detaching. Avoid Python lists in
  real-time audio callbacks.
- Pure Rust tests do not enable the optional Python feature, avoiding extension
  linking issues. Python tests check the actual FFI after the wheel is installed.
- The standalone producer uses hound's WAV writer. Keep MP3/AAC encoding in
  FFmpeg unless a measured, license-compatible native codec requirement exists.

## Rust Libraries by Job

| Job | Library | Boundary to understand |
| --- | --- | --- |
| Device recording/playback | [CPAL](https://github.com/RustAudio/cpal) | Native callback deadlines, device formats, and lifetime of the stream |
| Decode common audio formats | [Symphonia](https://github.com/pdeljanov/Symphonia) | Feature-gated codecs; decoding is not encoding |
| Playback | [Rodio](https://github.com/RustAudio/rodio) | Higher-level playback over CPAL; use current mixer APIs |
| Resampling | [Rubato](https://github.com/HEnquist/rubato) | Allocate buffers ahead of callbacks; preserve filter state across blocks |
| FFT/spectral work | [rustfft](https://github.com/ejmahler/RustFFT) | Plan once, reuse scratch storage |
| WAV read/write | [hound](https://github.com/ruuda/hound) | PCM bit depth, headers, and finalizing output |
| Plugins | [NIH-plug](https://github.com/robbert-vdh/nih-plug) | Host thread rules, CLAP/VST3 licensing and packaging |
| Browser DSP | [wasm-bindgen](https://rustwasm.github.io/wasm-bindgen/) | AudioWorklet/WASM buffers; separate from PyO3/CPython |

For a production recorder, let CPAL own device callbacks and use a bounded SPSC
ring buffer to communicate with workers. Don't run Tokio futures, Python, disk
writes, logging, or model inference in the callback. Rust prevents many memory
bugs; it does not automatically prevent dropouts or remove OS scheduling latency.
For a desktop frontend, Tauri commands can expose Rust orchestration, while a
Python worker owns inference. Design framing, job IDs, cancellation, and process
shutdown explicitly rather than embedding several event loops in the audio thread.