# AI and Frontend Boundaries

## Validated Audio API

```sh
uv sync --extra ai
uv run --extra ai uvicorn ai_examples.service:app --host 127.0.0.1 --port 8000
# In another terminal:
uv run --extra ai python -m ai_examples.client
uv run --extra ai pytest tests/test_ai.py
```

The API accepts a small mono float PCM window and returns sample peak/RMS levels.
This is deterministic signal analysis, **not AI**. JSON schemas, explicit limits,
connection pooling, status checks, and response validation also apply when the
upstream is an inference server. Strict Pydantic models are runtime validators;
Python hints alone are analogous to TypeScript's erased types.

The server is loopback-only. Use a frontend dev proxy rather than opening CORS
to every origin. For a deployed application add authentication, rate/body-size
limits at the ingress, TLS, cancellation, and a bounded job queue. Model validation
limits samples after parsing; it does not prevent an oversized HTTP body from
being received. Don't send large recordings as JSON arrays: upload a bounded
binary object and pass a server-issued ID, not an arbitrary filesystem path.

The sync FastAPI handler runs in the server's thread pool, not on its async event
loop. Short arithmetic here is fine; long inference belongs in a worker with
backpressure. `async def` does not make synchronous ML inference non-blocking.
Transport retries are not automatically safe for billable POST requests; use
provider-supported idempotency keys and bounded retries when appropriate.

## Local Speech Transcription

```sh
uv sync --extra transcribe
uv run --extra transcribe python -m ai_examples.transcribe output/voice.wav --model tiny.en
```

This explicit command may download a Whisper model from Hugging Face on first
use. Audio is processed locally, but model download needs network access and disk
space. Use `--model /path/to/downloaded/model` for a local CTranslate2 model.
`tiny.en` is English-only; use a multilingual model for other languages. The
example chooses CPU int8 to avoid GPU-specific setup. Test doubles exercise the
lazy inference boundary; they do not prove transcription quality or native model
compatibility. Optional dependencies are not installed by the base test run.

Whisper can hallucinate speech in silence, and VAD can remove quiet speech.
Inspect output, retain timestamps, and evaluate on representative audio. Never
automatically turn a transcript into executable tool calls. Consider consent,
retention, and licenses before recording or sending audio to a hosted provider.

## From Arrays to Models

Python differs from browser media in a few important ways:

- NumPy uses `(frames, channels)` here; many ML models expect `(batch, channels,
  time)` tensors. Inspect the model contract before transposing or resampling.
- Use float32, keep the original sample rate, downmix deliberately, then resample.
  Blind averaging can cancel out-of-phase stereo. A 16 kHz model cannot recover
  frequencies above 8 kHz.
- A speech frontend often computes STFT and log-mel features. Use the model's
  preprocessing library rather than inventing normalization or padding rules.
- For PyTorch inference use `model.eval()` and `torch.inference_mode()`, choose
  CPU/CUDA/MPS explicitly, and avoid host-device copies in a hot loop. CUDA is
  not available on macOS. faster-whisper uses CTranslate2, not PyTorch or MPS.
- Do not execute untrusted pickle-based checkpoints or `trust_remote_code=True`.
  Prefer trusted sources and formats such as safetensors; pin model revisions
  and record preprocessing/model versions for reproducible results.

Learn [PyTorch](https://pytorch.org/),
[Transformers](https://huggingface.co/docs/transformers/),
[faster-whisper](https://github.com/SYSTRAN/faster-whisper), and
[ONNX Runtime](https://onnxruntime.ai/) after the language/audio basics. For a
browser deployment, ONNX Runtime Web or Rust/WASM has different threading,
memory, and device constraints from this CPython environment.