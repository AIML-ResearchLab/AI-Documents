## 1. CognitiveTwin

**Paper:** `CognitiveTwin: Robust Multi-Modal Digital Twins for Predicting Cognitive Decline in Alzheimer's Disease`
**Link:** `https://arxiv.org/abs/2604.22428`

Predicting individual cognitive decline in Alzheimer's disease (AD) is difficult due to the heterogeneity of disease progression. Reliable clinical tools require not only high accuracy but also fairness across demographics and robustness to missing data.We present CognitiveTwin, a digital twin framework that predicts patient-specific cognitive trajectories. The model integrates multi-modal longitudinal data (cognitive scores, magnetic resonance imaging, positron emission tomography, cerebrospinal fluid biomarkers, and genetics). We use a Transformer-based architecture to fuse these modalities and a Deep Markov Model to capture temporal dynamics. We trained and evaluated the framework using data from 1,666 patients in the TADPOLE (Alzheimer's Disease Neuroimaging Initiative) dataset. We assessed the model for prediction error, demographic fairness, and robustness to missing-not-at-random (MNAR) data patterns. ognitiveTwin provides accurate and personalized predictions of cognitive decline. Its demonstrated fairness across patient demographics and resilience to clinical dropout make it a reliable tool for clinical trial enrichment and personalized care planning.


## What problem is this paper solving?
Alzheimer's disease progresses differently for every patient.Some patients decline rapidly, while others remain stable for years.
Doctors currently use:

- MMSE (Mini-Mental State Examination)
- ADAS-Cog
- MRI scans
- PET scans
- Biomarkers
- Genetics

But predicting **how a specific patient will decline over the next 2–3 years** is very difficult.The paper proposes a **Digital Twin** for each patient.

Think of it as: `A virtual AI version of the patient that learns their disease progression and predicts their future cognitive decline.`

## What is a Digital Twin?
A Digital Twin is:

```
Real Patient
      |
      v
+----------------+
| CognitiveTwin  |
| (AI Replica)   |
+----------------+
      |
      v
Predict Future MMSE
Predict Risk
Predict Progression
```

The AI continuously learns from patient history and predicts:

- Future cognitive scores
- Disease progression
- Risk of rapid decline
- Uncertainty around predictions

## What data does CognitiveTwin use?
The model combines **4 modalities**.

**A. Cognitive Tests**

Examples:

- MMSE
- ADAS-Cog
- CDR-SB
- FAQ
- RAVLT

**B. Biomarkers**

Examples:

- Amyloid-beta
- Tau protein
- PET scan biomarkers

**C. MRI Features**

Examples:

- Hippocampus volume
- Brain volume
- Ventricles
- Entorhinal cortex thickness

These capture structural brain damage.

**D. Genetics**

- APOE4 count (0 / 1 / 2)

Total:

```
32 features per visit
1666 patients
12505 visits
```

from the ADNI/TADPOLE dataset.

## Architecture Overview

The architecture combines: `Multi-Modal Transformer` + `Deep Markov Model`

Why both?

- Transformer: `learns relationships between modalities`
- Deep Markov Model: `learns disease evolution over time`

## Transformer-Based Fusion
The paper first converts all modalities into a common embedding space.

Example:

```
MRI --------\
PET ---------\
Biomarkers --- > Transformer
Genetics ----/
Cognitive ---/
```

The Transformer learns:
- Which modality matters most
- At what stage

- Early disease: `PET > Cognitive Scores`
- Late disease: `MRI + Cognitive Scores > Genetics`

The attention mechanism dynamically learns this.

## Deep Markov Model (DMM)
This is what makes the paper different.

Most healthcare models use: `LSTM`, `GRU`, `Transformer` . But those only learn patterns.
A Deep Markov Model learns: `Hidden Disease State`

Example: `Patient looks stable today`.
But internally: `Disease State = worsening`

The DMM tracks this hidden state.

Conceptually:

```
Disease State(t)
      |
      v
Disease State(t+1)
      |
      v
Disease State(t+2)
```

The model predicts how the hidden disease evolves.This is ideal for Alzheimer's because disease progression is gradual and latent.

## Why DMM is powerful

Imagine:

```
MRI missing
PET missing
Patient skipped visit
```

Most models fail. DMM can estimate: `Hidden disease state` and continue forecasting.
This explains why the model handles missing data well.

## Results

**MMSE Prediction** 24-month prediction:

| Metric | Result |
| ------ | ------ |
| MAE    | 1.619  |
| RMSE   | 2.248  |
| R²     | 0.682  |


**Interpretation** Average prediction error: `≈ 1.6 MMSE points`
**Clinical MMSE test-retest variability is roughly:** `1.5–2.0 points`

Meaning: `The AI's prediction error is almost as small as the natural measurement noise itself.`


## Progression Prediction

They also predict: `Will this patient rapidly decline?`

Result: `AUROC = 0.912`

In medicine: `0.912 is strong.`

| AUROC | Quality   |
| ----- | --------- |
| 0.50  | Random    |
| 0.70  | Good      |
| 0.80  | Very Good |
| 0.90+ | Excellent |


## Fairness Analysis

Many healthcare AIs work better for one demographic.
The authors checked this.

**Male:** `MAE = 1.622`
**Female:** `MAE = 1.614`

**Difference:** `0.008`

Almost identical.The model also performed consistently across age groups.

## Missing Data Robustness

Very important for healthcare.

They simulated: `15% MRI data missing` specifically for sicker patients.

Result: `MAE : 1.619 -> 1.625`
Only: `0.3% degradation`

This is one of the strongest findings of the paper.

## Ablation Study

They removed components to see what matters.

**Full Model:** `MAE = 1.619`
**Remove DMM:** `MAE = 1.749`

`8% worse.`

**Remove Genetics** `MAE = 1.700`

`5% worse.`

**Cognitive Scores Only** `MAE = 1.862`

`15% worse.`

**Simple Baseline** `MAE = 3.080`

`90% worse.`







## 2. Transition-Based Digital Twin Modelling for Alzheimer's Disease

**Paper:** `Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data`
**Link:** `https://arxiv.org/abs/2606.09671`


