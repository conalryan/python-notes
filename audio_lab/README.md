# Audio Workbench

```sh
uv sync --extra audio
mkdir -p output
uv run --extra audio python -m audio_lab demo output/master.wav
uv run --extra audio python -m audio_lab edit output/master.wav output/edited.wav --start 0.1 --stop 0.9 --gain-db -3
uv run --extra audio python -m audio_lab export output/edited.wav output/listening.mp3
uv run --extra audio python -m audio_lab export output/edited.wav output/listening.m4a
uv run --extra audio python -m audio_lab export output/edited.wav output/listening.mp4
uv run --extra audio pytest tests/test_audio.py
```

Install FFmpeg separately (`brew install ffmpeg` on macOS). An FFmpeg build needs
the `libmp3lame` encoder for MP3; AAC uses FFmpeg's native encoder. WAV is a
container, PCM is sample encoding, MP3 is lossy, and MP4/M4A are containers that
can hold AAC. An audio-only `.mp4` is not a music video. The encoder commands use
`-n` to refuse overwrites and raise on errors; retain your WAV master.

## Signal Model

- Arrays are float32 with shape `(frames, channels)`, even for mono. A stereo
  frame contains two samples. Seconds are converted to nearest frame boundaries.
- 48 kHz is a useful audio/video rate; speech models often expect mono 16 kHz.
  Changing a header is not resampling. `resample_poly` includes anti-alias filtering.
- Editing returns new buffers; NumPy slices normally share memory, unlike a
  typical JS array copy. The `Audio` boundary copies and marks buffers read-only.
- Gain, trim, fades, constant-power panning, and timeline-offset mixing are in
  `processing.py`. Resample tracks and choose a common channel layout before mixing.
- Floating-point mixes can exceed full scale; do not clip each track. The demo
  normalizes the final sample peak to -1 dBFS. This is **not** LUFS normalization,
  true-peak limiting, dithering, mastering, or protection from intersample peaks.
- WAV export is explicit 24-bit PCM. For a final 16-bit deliverable, consider
  dither after the last DSP stage. Never normalize silence by dividing by zero.

## Recording

Only run these commands when you intend to access the microphone:

```sh
uv run --extra audio python -m audio_lab devices
uv run --extra audio python -m audio_lab record output/voice.wav --seconds 5 --device 0
```

Pick an actual input device from the list, not necessarily device 0. macOS needs
microphone permission for the terminal/editor. sounddevice wheels typically bundle
PortAudio on macOS/Windows; Linux may need the system PortAudio library.
SoundFile wheels usually bundle libsndfile. No recording starts during imports or
tests. Input overflow reports mean audio was lost; do not mistake them for an
exact count of dropped frames. Interrupted recordings may leave a valid partial
file, which should be inspected before reuse.

The recorder streams fixed-size blocks to disk to bound memory. It is intentionally
not real-time monitoring. For interactive instruments, use a native callback with
preallocated buffers and a bounded SPSC ring buffer; move disk I/O, model inference,
logging, locks, and encoding off that callback. A 256-frame block at 48 kHz gives
about 5.33 ms of processing budget, before other latency. UI updates belong on
their own event loop and should consume coalesced meters, not every sample.

Browser MediaRecorder commonly produces Opus in WebM, not WAV. Decode it with
FFmpeg before sample editing. Web Audio AudioWorklets and Rust/WASM are another
deployment boundary; Python native extensions do not load in a browser.

## Next Libraries

Use SciPy for filters/FFT/STFT, librosa for offline analysis and features,
Pedalboard for effects and plugin hosting, and pyloudnorm or FFmpeg's `loudnorm`
for loudness measurement. Check licenses and platform support for codecs and
plugins. Do not hand-roll production resamplers or MP3/AAC encoders. The Rust
integration notes explain CPAL, Symphonia, Rubato, rustfft, and plugin tooling.