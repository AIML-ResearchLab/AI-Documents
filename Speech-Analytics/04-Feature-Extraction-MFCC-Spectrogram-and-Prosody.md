# 04 - Feature Extraction: MFCC, Spectrogram, and Prosody

## Objective
Convert raw speech into compact features that support ASR, speaker, emotion, and conversation models.

## FFT vs STFT
- **FFT**: frequency content of the entire signal; loses time-local context.
- **STFT**: frequency content over short windows through time; standard for speech processing.

## Spectrogram Interpretation
- X-axis: time
- Y-axis: frequency (Hz)
- Color/intensity: amplitude or power

Interpretation:
- Dark regions: low energy/silence
- Bright regions: high energy/active speech events

## Amplitude vs Power
Power spectrogram is based on squared amplitude:

$$
Power = Amplitude^2
$$

Convert to decibel scale using `librosa.power_to_db()` for more interpretable, perception-aligned visualization.

## Mel Spectrogram
Humans are more sensitive to low frequencies than high frequencies, so Mel scaling better matches perception.

Key parameters:
- `n_mels`: number of Mel bands
- `fmin`: minimum frequency
- `fmax`: maximum frequency

## MFCC (Core Practical Feature)
MFCC = Mel Frequency Cepstral Coefficients.

Typical speech feature stack:
- 12 static cepstral coefficients
- 12 delta coefficients
- 12 delta-delta coefficients
- 1 energy
- 1 delta energy
- 1 delta-delta energy

Total common representation: **39 features per frame**.

## MFCC vs LFCC
| Method | Scale | Typical usage |
|---|---|---|
| MFCC | Mel (perceptual) | Most common in speech tasks |
| LFCC | Linear frequency | Alternative in some pipelines |

## Delta and Delta-Delta
Use temporal derivatives to capture motion/change over time.

Practical effect:
- Better capture of speaking dynamics
- Improved recognition robustness vs static-only features

## Additional Frame-Level Features
- **RMS energy**: loudness/intensity trend (`librosa.feature.rms`)
- **Pitch/F0**: prosody and emotion signals (`librosa.piptrack`)
- **Spectral centroid**: perceived brightness
- **Spectral bandwidth**: spread of frequencies
- **Spectral rolloff**: cutoff below which most energy lies
- **Spectral flatness**: tonal vs noise-like character
- **Zero Crossing Rate (ZCR)**: sign-change density, useful for speed/noise cues

High ZCR often indicates:
- Higher-frequency/noisy content
- Fast or unvoiced segments

Low ZCR often indicates:
- Slower voiced segments
- Longer pauses and stable tones

## Voice Activity Detection (VAD)
Separating silent and non-silent intervals:
- Reduces blank audio processing
- Improves feature quality
- Supports downstream segmentation quality

## Practical Example (Librosa)
```python
import librosa
import numpy as np

y, sr = librosa.load("call.wav", sr=16000, mono=True)

# STFT and power/dB spectrogram
S = np.abs(librosa.stft(y, n_fft=512, hop_length=160, win_length=400)) ** 2
S_db = librosa.power_to_db(S, ref=np.max)

# Mel and MFCC
mel = librosa.feature.melspectrogram(S=S, sr=sr, n_mels=80, fmin=50, fmax=7600)
mfcc = librosa.feature.mfcc(S=librosa.power_to_db(mel), n_mfcc=13)
delta = librosa.feature.delta(mfcc)
delta2 = librosa.feature.delta(mfcc, order=2)

# Extra features
rms = librosa.feature.rms(y=y)
zcr = librosa.feature.zero_crossing_rate(y)
centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
flatness = librosa.feature.spectral_flatness(y=y)
pitch, mag = librosa.piptrack(y=y, sr=sr)
```

## Engineering Guidelines
- Use fixed frame/hop across training and inference.
- Version feature extractors like models.
- Track domain shifts (e.g., headset vs speakerphone frequency profile).

## Complete Feature Engineering Pipeline
Raw audio  
-> Mono conversion  
-> Silence trimming  
-> Pre-emphasis  
-> Framing (`25 ms`)  
-> Hop (`10 ms`)  
-> STFT  
-> Power spectrogram  
-> Mel spectrogram  
-> MFCC/LFCC  
-> Delta + delta-delta  
-> Energy + ZCR + spectral features  
-> Normalization  
-> Model-ready feature set

## Real-Time Example
A retention-risk model combines lexical sentiment with prosodic escalation (increased pitch variance + interruption density) to trigger supervisor assistance before churn events.

## SLP3 Coverage Mapping
- Ch. 14.5 log-Mel feature extraction
- Ch. 14.6 MFCC derivation
- Ch. 14.3 prosody
