# 03 - Audio Formats, Preprocessing, and Quality Control

## 3.1 Formats
WAV, FLAC, MP3, and telephony codecs have different quality/size tradeoffs.

## 3.2 Preprocessing
- resampling
- silence trimming
- channel normalization
- VAD-based segmentation

## 3.3 Quality Gates
Check clipping, SNR, duration, and corruption before model inference.

## 3.4 Real-Time Example
Reject low-quality call segments before ASR to improve transcript reliability.

