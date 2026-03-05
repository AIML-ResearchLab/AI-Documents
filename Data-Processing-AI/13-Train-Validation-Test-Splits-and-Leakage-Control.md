# 13 - Train, Validation, Test Splits and Leakage Control

## 13.1 Split Strategy
Use split design based on task and data generation process.

## 13.2 Common Split Types
- random split
- stratified split
- time-based split
- group-aware split

## 13.3 Leakage Sources
- future data in features
- target leakage fields
- leakage through preprocessing fit on full data

## 13.4 Controls
- fit transforms only on train data
- freeze split keys
- audit feature provenance

## 13.5 Real-Time Example
Time-based split for fraud model prevents future transaction leakage.

