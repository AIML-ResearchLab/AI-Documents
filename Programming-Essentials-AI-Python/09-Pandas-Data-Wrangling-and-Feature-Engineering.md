# 09 - Pandas Data Wrangling and Feature Engineering

## 9.1 DataFrame Fundamentals
```python
import pandas as pd

df = pd.read_csv("train.csv")
print(df.head())
```

## 9.2 Core Operations
- Select columns and rows
- Filter records
- Group and aggregate
- Sort and deduplicate

## 9.3 Missing Data Handling
- `dropna()` for controlled removal
- `fillna()` with domain-aware defaults
- Track imputation strategy for reproducibility

## 9.4 Joins and Merges
Use keys carefully to avoid record explosion.

## 9.5 Feature Engineering Patterns
- Categorical encoding
- Date/time feature extraction
- Text length and keyword features
- Scaling and normalization

## 9.6 Leakage Prevention
Do not use target-derived information during training feature creation.

## 9.7 Real-Time Feature Example
Customer ticket priority model:
- text_length
- urgency_keyword_count
- prior_ticket_count
- account_tier

