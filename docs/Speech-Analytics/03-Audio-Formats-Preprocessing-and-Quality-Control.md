# 03 - Audio Formats, Preprocessing, and Quality Control

## Objective
Design a robust preprocessing stage so ASR and analytics models receive stable, clean, and traceable inputs.

## Input Format Strategy
- Accept: WAV, FLAC, MP3, AAC, Opus, streaming RTP/WebRTC
- Canonical internal representation: PCM WAV (`mono`, `16kHz` unless use case requires otherwise)
- Preserve source metadata for auditability and replay

## Preprocessing Pipeline
1. Silence trimming and VAD segmentation
2. Loudness normalization (LUFS/RMS targets)
3. Noise suppression and dereverberation
4. Optional echo cancellation
5. Channel separation for two-party calls

## Silence Trimming (Feature Engineering Step)
Use `librosa.effects.trim()` to remove:
- Leading silence
- Trailing silence
- Very low-amplitude edge noise

Typical use cases:
- Remove dead air at call start/end
- Clean voice-note datasets
- Improve feature stability for short utterances

## Pre-Emphasis
Pre-emphasis boosts higher frequencies and sharpens formant-related information.

Common transform:

$$
y[t] = x[t] - \alpha x[t-1]
$$

Typical coefficient: `alpha = 0.95` to `0.97`.

Why it helps:
- Enhances high-frequency clarity
- Improves downstream speech feature quality in some pipelines

## Framing and Hop Length (Windowing)
Speech is non-stationary over long spans, so we analyze short windows.

Standards:
- Frame length: `25 ms`
- Hop length: `10 ms`

Why:
- Speech is approximately stationary within 20-30 ms windows.
- Too large a hop can miss fast acoustic events.
- Too small a hop increases compute and feature volume.

## Resampling
Resampling aligns data with model requirements.

Example:
- `44.1kHz` media audio -> `16kHz` ASR input

Benefits:
- Consistent feature extraction
- Lower inference cost
- Reduced mismatches between train and serve pipelines

## Normalization (Z-Score)
Standardize feature scale before ML training:

$$
Z = \frac{X - \mu}{\sigma}
$$

Implementation note:
- Guard against division by zero with a small epsilon if `sigma == 0`.

## Practical Example (Librosa + Numpy)
```python
import librosa
import numpy as np

y, sr = librosa.load("call.wav", sr=16000, mono=True)
y_trimmed, _ = librosa.effects.trim(y, top_db=25)
y_pre = librosa.effects.preemphasis(y_trimmed, coef=0.97)

frame_length = int(0.025 * sr)  # 25 ms
hop_length = int(0.010 * sr)    # 10 ms

# Example feature to normalize (RMS here)
rms = librosa.feature.rms(y=y_pre, frame_length=frame_length, hop_length=hop_length)
rms_z = (rms - rms.mean()) / (rms.std() + 1e-8)
```

## Quality Control Gates
- Audio duration bounds
- Signal-to-noise ratio (SNR) threshold
- Clipping percentage threshold
- Corrupt payload and timestamp continuity checks

## Real-Time Example
A healthcare triage bot trims edge silence, applies pre-emphasis, and standardizes framing before intent detection. Low-SNR clips are routed to fallback flow, reducing unsafe automation decisions.

## SLP3 Coverage Mapping
- Ch. 14.4 signal characteristics
- Ch. 15.1 ASR task assumptions about clean vs noisy conditions
