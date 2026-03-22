# 02 - Audio Basics, Signals, and Sampling

## Why This Matters
Every downstream metric in speech analytics is limited by signal quality. Bad sampling or clipping propagates into ASR, diarization, and sentiment errors.

## Sampling Rate (Practical Understanding)
**Definition**: Sampling Rate (`Sr`) is the number of audio samples captured per second.

Examples:
- `44100 Hz` -> 44.1K samples/second
- `16000 Hz` -> 16K samples/second

Nyquist reminder:

$$
f_{max} = \frac{Sr}{2}
$$

If `Sr = 16000`, then the maximum captured frequency is `8000 Hz`.

Practical insight:
- ASR pipelines usually standardize to `16kHz`.
- Music/audio mastering commonly uses `44.1kHz` or `48kHz`.
- Higher `Sr` means larger file size and more compute.
- Lower `Sr` reduces size but may remove useful high-frequency detail.

Goal: keep frequencies that matter for speech understanding, not unnecessary bandwidth.

## Mono vs Stereo
- **Mono**: single channel, standard for speech tasks and ASR.
- **Stereo**: two channels, common in music and immersive audio.

`librosa` loading behavior:
- `mono=True` forces single channel output.
- `mono=False` keeps original channel layout.

## Bit Depth and Amplitude Scaling
- Bit depth controls amplitude resolution and quantization precision.
- `librosa.load()` returns float samples typically scaled in `[-1, +1]`.

Why this helps:
- Stable ML training
- Consistent preprocessing across datasets

## Duration Calculation
Use `librosa.get_duration()` to:
- Validate recording length
- Detect truncated clips
- Normalize dataset assumptions (e.g., minimum call segment length)

## Practical Standards
- Normalize to canonical input for speech models (`mono`, `16kHz`, `16-bit PCM`).
- Keep channel/source metadata (agent/customer, mic type, region).
- Detect clipping, silence-only segments, and packet loss before model inference.

## Minimal Example (Librosa)
```python
import librosa

y, sr = librosa.load("call.wav", sr=16000, mono=True)
duration_sec = librosa.get_duration(y=y, sr=sr)
print(sr, duration_sec, y.min(), y.max())  # 16000, duration, range near [-1, 1]
```

## Real-Time Example
A telecom support team sees rising WER in one region. Root cause analysis finds mixed sampling (`8kHz`, `16kHz`, `44.1kHz`) and inconsistent channel conversion. Enforcing `mono + 16kHz` at ingestion stabilizes ASR quality and lowers correction effort.

## SLP3 Coverage Mapping
- Ch. 14.4 Acoustic phonetics and signals
- Ch. 14.3 Prosody basics
