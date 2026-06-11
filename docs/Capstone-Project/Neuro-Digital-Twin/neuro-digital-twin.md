# All Parameters — Section-Wise

## Section 1: Cognitive / Clinical Scores — 10 Features (BiLSTM features 1–10)

| #  | Feature            | Full Name                           | Range / Unit | Clinical Meaning |
|----|---------------------|-------------------------------------|---------------|-------------------|
| 1  | `mmse`              | Mini-Mental State Examination       | 0–30          | Overall cognitive status (30 = normal, <24 = impaired) |
| 2  | `cdr_global`        | Clinical Dementia Rating (Global)   | 0, 0.5, 1, 2, 3 | Global dementia severity |
| 3  | `cdrsb`             | Clinical Dementia Rating Sum of Boxes | 0–18        | Sum of scores across the six CDR domains |
| 4  | `adas_cog11`        | Alzheimer's Disease Assessment Scale – Cognitive Subscale (11-item) | 0–70 | Measures cognitive impairment in Alzheimer's disease (higher scores indicate worse cognition) |
| 5  | `adas_cog13`        | Alzheimer's Disease Assessment Scale – Cognitive Subscale (13-item) | 0–85 | Extended version of ADAS-Cog with additional cognitive tasks |
| 6  | `ravlt_immediate`   | Rey Auditory Verbal Learning Test – Immediate Recall | 0–75 | Assesses verbal learning and immediate memory through repeated word-list recall |
| 7  | `ravlt_learning`    | Rey Auditory Verbal Learning Test – Learning Score | 0–15 | Reflects improvement in learning across the five acquisition trials |
| 8  | `ravlt_forgetting`  | Rey Auditory Verbal Learning Test – Forgetting Score | 0–15 | Indicates the amount of information forgotten after a delay (higher values suggest greater forgetting) |
| 9  | `faq`               | Functional Activities Questionnaire | 0–30 | Evaluates impairment in instrumental activities of daily living (higher scores indicate greater functional decline) |
| 10 | `moca`              | Montreal Cognitive Assessment       | 0–30          | Screening tool for mild cognitive impairment and broader cognitive deficits (<26 suggests impairment) |

## Section 2: MRI Volumetric Features — 20 Features (BiLSTM features 11–30)

| #  | Feature                      | Sub-group    | Unit  | Clinical Meaning |
|----|------------------------------|---------------|--------|-------------------|
| 11 | `hippocampal_volume_left`    | Hippocampal   | mm³    | Left hippocampal volume — a key biomarker for Alzheimer's disease; reduced volume is associated with memory impairment and disease progression. |
| 12 | `hippocampal_volume_right`   | Hippocampal   | mm³    | Right hippocampal volume — contributes to memory and spatial processing; atrophy may indicate neurodegeneration. |
| 13 | `hippocampal_volume_total`   | Hippocampal   | mm³    | Combined bilateral hippocampal volume used to assess overall hippocampal integrity and Alzheimer's disease severity. |
| 14 | `entorhinal_cortex_left`     | Entorhinal    | mm³    | Left entorhinal cortex volume — one of the earliest regions affected in Alzheimer's disease, involved in memory encoding and navigation. |
| 15 | `entorhinal_cortex_right`    | Entorhinal    | mm³    | Right entorhinal cortex volume — supports memory and spatial orientation; early degeneration may precede cognitive symptoms. |
| 16 | `amygdala_volume_left`       | Amygdala      | mm³    | Left amygdala volume — involved in emotional processing and memory; shrinkage may contribute to behavioral symptoms. |
| 17 | `amygdala_volume_right`      | Amygdala      | mm³    | Right amygdala volume — associated with emotion regulation and social cognition. |
| 18 | `ventricular_volume`         | Global        | mm³    | Lateral ventricular volume — enlargement often reflects loss of surrounding brain tissue and progressive atrophy. |
| 19 | `whole_brain_volume`         | Global        | mm³    | Total brain parenchymal volume — decreases with aging and accelerates in neurodegenerative disorders. |
| 20 | `gray_matter_volume`         | Global        | mm³    | Total gray matter volume — reflects neuronal density and cortical integrity; reductions indicate neurodegeneration. |
| 21 | `white_matter_volume`        | Global        | mm³    | Total white matter volume — represents structural connectivity between brain regions; loss may impair information processing. |
| 22 | `cortical_thickness_mean`    | Global        | mm     | Average cortical thickness across brain regions; cortical thinning is associated with cognitive decline. |
| 23 | `temporal_lobe_volume`       | Lobar         | mm³    | Temporal lobe volume — critical for memory and language functions; early atrophy is common in Alzheimer's disease. |
| 24 | `frontal_lobe_volume`        | Lobar         | mm³    | Frontal lobe volume — supports executive function, planning, and decision-making; reductions may impair daily functioning. |
| 25 | `parietal_lobe_volume`       | Lobar         | mm³    | Parietal lobe volume — involved in spatial awareness and sensory integration; degeneration may affect orientation and visuospatial abilities. |
| 26 | `occipital_lobe_volume`      | Lobar         | mm³    | Occipital lobe volume — responsible for visual processing; usually relatively preserved in early Alzheimer's disease. |
| 27 | `cerebellum_volume`          | Lobar         | mm³    | Cerebellar volume — contributes to motor coordination and cognitive functions; changes may occur in advanced neurodegeneration. |
| 28 | `brain_atrophy_score`        | Atrophy       | 0–1    | Composite index representing overall brain atrophy severity (0 = none, 1 = severe). |
| 29 | `hippocampal_atrophy_rate`   | Atrophy       | %/year | Annual percentage reduction in hippocampal volume; accelerated decline predicts disease progression. |
| 30 | `ventricular_expansion_rate` | Atrophy       | %/year | Annual percentage increase in ventricular size; serves as an indirect marker of brain tissue loss. |

## Section 3: Demographics — 5 Features (BiLSTM features 31–35)

| #  | Feature              | Type    | Values / Unit           | Clinical Meaning |
|----|-----------------------|----------|---------------------------|-------------------|
| 31 | `age`                 | Float    | Years (e.g., 72.0)        | Age at the time of clinical assessment, typically calculated from date of birth. Increasing age is the strongest non-modifiable risk factor for Alzheimer's disease and other dementias. |
| 32 | `sex_bin`             | Binary   | 0 = Female, 1 = Male      | Biological sex of the individual. Sex differences may influence Alzheimer's disease prevalence, progression patterns, and treatment responses. |
| 33 | `education_years`     | Integer  | 0–30 years                | Total years of formal education. Often used as a proxy for **cognitive reserve**, where higher educational attainment may delay the clinical manifestation of dementia symptoms despite underlying pathology. |
| 34 | `apoe4_alleles`        | Integer  | 0, 1, 2                   | Number of **APOE ε4** alleles carried by the individual. APOE ε4 is the strongest common genetic risk factor for late-onset Alzheimer's disease; risk increases with allele count. |
| 35 | `family_history_ad`   | Binary   | 0 = No, 1 = Yes           | Indicates whether a first-degree relative (parent or sibling) has a history of Alzheimer's disease. A positive family history suggests increased genetic and shared environmental risk. |

## Section 4: CSF Biomarkers — 5 Features (BiLSTM features 36–40)

| #  | Feature                  | Full Name                          | Unit  | Clinical Meaning |
|----|---------------------------|------------------------------------|--------|-------------------|
| 36 | `csf_abeta42`             | CSF Amyloid Beta 1–42              | pg/mL  | Primary cerebrospinal fluid (CSF) amyloid biomarker. **Lower concentrations indicate cerebral amyloid plaque deposition**, a hallmark of Alzheimer's disease. Values **< 192 pg/mL** are commonly considered abnormal in AD research cohorts. |
| 37 | `csf_abeta40`             | CSF Amyloid Beta 1–40              | pg/mL  | Amyloid beta peptide used primarily in conjunction with Aβ42 to calculate the **Aβ42/Aβ40 ratio**, helping reduce variability due to individual differences in total amyloid production. |
| 38 | `csf_tau_total`           | CSF Total Tau                      | pg/mL  | Marker of **neuronal injury and neurodegeneration**. Elevated levels reflect axonal damage and are associated with disease severity and progression in Alzheimer's disease and other neurodegenerative disorders. |
| 39 | `csf_ptau181`             | CSF Phosphorylated Tau 181         | pg/mL  | Specific biomarker of **tau pathology** and neurofibrillary tangle formation. Increased concentrations strongly support an Alzheimer's disease pathological process. |
| 40 | `csf_abeta42_tau_ratio`   | CSF Aβ42 / Total Tau Ratio         | Ratio  | Composite biomarker integrating **amyloid deposition and neurodegeneration**. Lower ratios indicate a higher likelihood of Alzheimer's disease pathology and often provide better diagnostic accuracy than individual markers alone. |

## Section 5: PET Imaging + White Matter — 4 Features (BiLSTM features 41–44)

| #  | Feature                     | Full Name                    | Unit | Clinical Meaning |
|----|------------------------------|------------------------------|-------|-------------------|
| 41 | `fdg_pet_suvr`              | FDG-PET Standardized Uptake Value Ratio (SUVR) | SUVR | Measures cerebral glucose metabolism using fluorodeoxyglucose positron emission tomography (FDG-PET). **Lower SUVR values indicate hypometabolism**, reflecting neuronal dysfunction and neurodegeneration. Considered an **N (Neurodegeneration)** biomarker within the AT(N) framework. |
| 42 | `amyloid_pet_suvr`          | Amyloid PET Standardized Uptake Value Ratio (SUVR) | SUVR | Quantifies cerebral amyloid plaque deposition using amyloid-targeted PET tracers. **Higher SUVR values indicate increased amyloid burden**, supporting **amyloid positivity (A+)** in the AT(N) framework. |
| 43 | `tau_pet_suvr`              | Tau PET Standardized Uptake Value Ratio (SUVR) | SUVR | Assesses the burden and distribution of neurofibrillary tau tangles using tau-specific PET tracers. **Higher SUVR values indicate greater tau pathology**, corresponding to **tau positivity (T+)** in the AT(N) framework. |
| 44 | `wm_hyperintensity_volume`  | White Matter Hyperintensity Volume | mL | Represents the volume of white matter lesions typically detected on MRI (e.g., FLAIR sequences). Increased burden is associated with **cerebral small vessel disease, vascular injury, chronic ischemia, and neuroinflammatory processes**, which may contribute to cognitive impairment and mixed dementia. |

## Section 6: Temporal / Visit Tracking — 3 Features (BiLSTM features 45–47)

| #  | Feature                   | Type    | Values / Range         | Clinical Meaning |
|----|----------------------------|----------|-------------------------|-------------------|
| 45 | `visit_month`              | Integer  | 0, 6, 12, 18, 24, ...   | Scheduled assessment time point expressed as months from study enrollment or baseline visit. Used to align longitudinal observations across participants and evaluate disease progression at predefined intervals. |
| 46 | `months_since_baseline`    | Integer  | 0–N months              | Actual elapsed time since the participant's baseline assessment. Enables precise temporal modeling of cognitive decline, biomarker trajectories, and disease evolution, especially when visits do not occur exactly as scheduled. |
| 47 | `visit_number`             | Integer  | 1, 2, 3, ...            | Sequential index representing the order of clinical visits for an individual participant. Facilitates longitudinal tracking, time-series analysis, and organization of repeated measurements over the course of follow-up. |

#   ## BiLSTM 47-Feature Block Summary

Features  1–10  │ Cognitive Scores    │ 10 features
Features 11–30  │ MRI Volumetric      │ 20 features
Features 31–35  │ Demographics        │  5 features
Features 36–40  │ CSF Biomarkers      │  5 features
Features 41–44  │ PET + WMH           │  4 features
Features 45–47  │ Temporal            │  3 features
─────────────────────────────────────────────────
TOTAL                                    47 features


### Feature Distribution

| Domain | Included Features |
|---------|--------------------|
| **Cognitive Assessments** | MMSE, CDR, ADAS-Cog, RAVLT, FAQ, MoCA |
| **Structural MRI** | Hippocampal, Entorhinal, Amygdala, Whole Brain, Cortical Thickness, Lobar Volumes, Atrophy Measures |
| **Demographics & Genetics** | Age, Sex, Education, APOE ε4 Status, Family History |
| **Fluid Biomarkers (CSF)** | Aβ42, Aβ40, Total Tau, pTau181, Aβ42/Tau Ratio |
| **Molecular & Functional Imaging** | FDG-PET, Amyloid PET, Tau PET, White Matter Hyperintensity Burden |
| **Longitudinal Tracking** | Visit Month, Months Since Baseline, Visit Number |


### Dataset Composition

```text
┌──────────────────────────────────────────────┬──────────┐
│ Feature Category                             │ Count    │
├──────────────────────────────────────────────┼──────────┤
│ Cognitive Scores                             │ 10       │
│ MRI Volumetric Biomarkers                    │ 20       │
│ Demographics & Genetic Risk Factors          │  5       │
│ CSF Biomarkers                               │  5       │
│ PET Imaging + WMH                            │  4       │
│ Temporal / Longitudinal Variables            │  3       │
├──────────────────────────────────────────────┼──────────┤
│ TOTAL                                        │ 47       │
└──────────────────────────────────────────────┴──────────┘
```

### Multimodal Coverage of the 47-Feature Neuro-Digital Twin

| Clinical Dimension | Covered by Features |
|--------------------|--------------------|
| **Cognitive Function** | 1–10 |
| **Brain Structure (MRI)** | 11–30 |
| **Patient Characteristics** | 31–35 |
| **Biological Pathology (CSF)** | 36–40 |
| **Molecular / Functional Imaging** | 41–44 |
| **Disease Progression Over Time** | 45–47 |

### Alignment with the AT(N) Framework

| AT(N) Component | Corresponding Features |
|-----------------|------------------------|
| **A (Amyloid)** | 36 (`csf_abeta42`), 37 (`csf_abeta40`), 40 (`csf_abeta42_tau_ratio`), 42 (`amyloid_pet_suvr`) |
| **T (Tau Pathology)** | 39 (`csf_ptau181`), 43 (`tau_pet_suvr`) |
| **N (Neurodegeneration)** | 11–30 (MRI), 38 (`csf_tau_total`), 41 (`fdg_pet_suvr`) |
| **Vascular / Mixed Pathology** | 44 (`wm_hyperintensity_volume`) |
| **Clinical Expression** | 1–10 (Cognitive Measures) |
| **Risk & Susceptibility Factors** | 31–35 |
| **Temporal Disease Trajectory** | 45–47 |


**Summary:** The final **47-feature multimodal dataset** integrates **clinical cognition, structural neuroimaging, genetics, fluid biomarkers, PET imaging, vascular burden, and longitudinal follow-up information**, providing a comprehensive foundation for **Alzheimer's Disease progression modeling, Neuro-Digital Twin construction, survival analysis, trajectory forecasting, and personalized intervention simulation**.

## ClinicalFusionNet — 41 Features (4 Separate Branches)

The neural fusion model uses a slightly different feature set — fewer cognitive features, combined biomarker branch:

**Branch 1: Cognitive (8 features — feeds 64-dim sub-network)**


| # | Feature             | Difference from BiLSTM |
|---|----------------------|-------------------------|
| 1 | `mmse`               | Same |
| 2 | `cdr_global`         | Same |
| 3 | `cdrsb`              | Same |
| 4 | `adas_cog11`         | Same |
| 5 | `ravlt_immediate`    | Same |
| 6 | `ravlt_forgetting`   | Same |
| 7 | `faq`                | Same |
| 8 | `moca`               | Same |

`adas_cog13` and `ravlt_learning` are excluded from fusion net (used only in BiLSTM)

**Branch 2: MRI (20 features — feeds 128-dim sub-network)**

Same 20 features as BiLSTM features 11–30 above.

**Branch 3: Biomarkers (8 features — feeds 64-dim sub-network)**


## Additional Biomarkers Added Beyond the BiLSTM Model

| # | Feature                     | Source  |
|---|-----------------------------|----------|
| 1 | `csf_abeta42`               | CSF |
| 2 | `csf_tau_total`             | CSF |
| 3 | `csf_ptau181`               | CSF |
| 4 | `csf_abeta42_tau_ratio`     | CSF |
| 5 | `fdg_pet_suvr`              | PET |
| 6 | `amyloid_pet_suvr`          | PET |
| 7 | `tau_pet_suvr`              | PET |
| 8 | `wm_hyperintensity_volume`  | MRI |

---

### Biomarker Category Summary

| Source | Features | Count |
|---------|-----------|--------|
| **CSF Biomarkers** | `csf_abeta42`, `csf_tau_total`, `csf_ptau181`, `csf_abeta42_tau_ratio` | 4 |
| **PET Imaging Biomarkers** | `fdg_pet_suvr`, `amyloid_pet_suvr`, `tau_pet_suvr` | 3 |
| **MRI Biomarker** | `wm_hyperintensity_volume` | 1 |
| **Total New Biomarkers** | — | **8** |

---

### Clinical Significance

| Feature | AT(N) Category | Clinical Relevance |
|----------|----------------|-------------------|
| `csf_abeta42` | **A** | Detects amyloid plaque pathology |
| `csf_tau_total` | **N** | Indicates neuronal injury and neurodegeneration |
| `csf_ptau181` | **T** | Measures tau tangle pathology specific to Alzheimer's disease |
| `csf_abeta42_tau_ratio` | **A + N** | Improves diagnostic accuracy by combining amyloid and neurodegeneration signals |
| `fdg_pet_suvr` | **N** | Reflects reduced cerebral glucose metabolism associated with neurodegeneration |
| `amyloid_pet_suvr` | **A** | Quantifies amyloid plaque burden in vivo |
| `tau_pet_suvr` | **T** | Measures neurofibrillary tangle distribution and severity |
| `wm_hyperintensity_volume` | Vascular | Captures white matter damage related to small vessel disease and mixed dementia |

---

### Difference from the Original BiLSTM Model

```text
Original BiLSTM:
✓ Cognitive assessments
✓ Structural MRI measures
✓ Demographics / APOE
✓ Longitudinal temporal variables

Neuro-Digital Twin Extensions:
+ CSF amyloid biomarkers
+ CSF tau biomarkers
+ FDG-PET metabolism measures
+ Amyloid PET imaging
+ Tau PET imaging
+ White matter lesion burden
```

> **Key enhancement:** These eight biomarkers extend the BiLSTM framework from a predominantly **clinical and structural prediction model** into a **multimodal Neuro-Digital Twin** capable of modeling the underlying **AT(N) biological mechanisms** of Alzheimer's disease progression. This enables earlier detection, improved disease staging, and more personalized forecasting of future outcomes.


`csf_abeta40` is excluded from fusion net (used only in BiLSTM)


**Branch 4: Demographics (5 features — feeds 32-dim sub-network)**

Same 5 features as BiLSTM features 31–35 above.



# Neuro-Digital Twin Encoder Architecture (41 Features)

## Multimodal Branch Design

| Branch | Input Domain | Features | Encoder Output |
|---------|---------------|-----------|-----------------|
| Branch 1 | Cognitive | 8 features | 64-dimensional |
| Branch 2 | MRI Volumetric | 20 features | 128-dimensional |
| Branch 3 | Fluid & Molecular Biomarkers | 8 features | 64-dimensional |
| Branch 4 | Demographics & Genetics | 5 features | 32-dimensional |

---

## Input Feature Allocation

### Branch 1 – Cognitive (8 Features → 64-dim)

| Features |
|-----------|
| `mmse` |
| `cdr_global` |
| `cdrsb` |
| `adas_cog11` |
| `ravlt_immediate` |
| `ravlt_forgetting` |
| `faq` |
| `moca` |

---

### Branch 2 – MRI Volumetric (20 Features → 128-dim)

| Features |
|-----------|
| `hippocampal_volume_left` |
| `hippocampal_volume_right` |
| `hippocampal_volume_total` |
| `entorhinal_cortex_left` |
| `entorhinal_cortex_right` |
| `amygdala_volume_left` |
| `amygdala_volume_right` |
| `ventricular_volume` |
| `whole_brain_volume` |
| `gray_matter_volume` |
| `white_matter_volume` |
| `cortical_thickness_mean` |
| `temporal_lobe_volume` |
| `frontal_lobe_volume` |
| `parietal_lobe_volume` |
| `occipital_lobe_volume` |
| `cerebellum_volume` |
| `brain_atrophy_score` |
| `hippocampal_atrophy_rate` |
| `ventricular_expansion_rate` |

---

### Branch 3 – Biomarkers (8 Features → 64-dim)

| Features |
|-----------|
| `csf_abeta42` |
| `csf_tau_total` |
| `csf_ptau181` |
| `csf_abeta42_tau_ratio` |
| `fdg_pet_suvr` |
| `amyloid_pet_suvr` |
| `tau_pet_suvr` |
| `wm_hyperintensity_volume` |

---

### Branch 4 – Demographics & Genetics (5 Features → 32-dim)

| Features |
|-----------|
| `age` |
| `sex_bin` |
| `education_years` |
| `apoe4_alleles` |
| `family_history_ad` |

---

## Feature Count Summary

| Domain | Feature Count |
|---------|---------------|
| Cognitive | 8 |
| MRI Volumetric | 20 |
| Biomarkers | 8 |
| Demographics & Genetics | 5 |
| **Total** | **41 Features** |

---

## Encoder Fusion Architecture

```text
Branch 1: Cognitive
(8 features)
      │
      ▼
MLP Encoder
      │
      ▼
64-dim embedding
      │

Branch 2: MRI
(20 features)
      │
      ▼
MLP Encoder
      │
      ▼
128-dim embedding
      │

Branch 3: Biomarkers
(8 features)
      │
      ▼
MLP Encoder
      │
      ▼
64-dim embedding
      │

Branch 4: Demographics
(5 features)
      │
      ▼
MLP Encoder
      │
      ▼
32-dim embedding
      │
      ▼
─────────────────────────────────────
Concatenate
64 + 128 + 64 + 32
─────────────────────────────────────
          │
          ▼
     288-dim vector
          │
          ▼
Linear(288 → 256)
          │
          ▼
Neuro-Digital Twin
Patient Embedding
(256 dimensions)
```

---

## Mathematical Representation

For each modality:

```text
E_cog = f_cog(X_cog) ∈ ℝ⁶⁴
E_mri = f_mri(X_mri) ∈ ℝ¹²⁸
E_bio = f_bio(X_bio) ∈ ℝ⁶⁴
E_demo = f_demo(X_demo) ∈ ℝ³²
```

Fusion:

```text
E_concat = [E_cog ; E_mri ; E_bio ; E_demo]
```

```text
E_concat ∈ ℝ²⁸⁸
```

Final embedding:

```text
E_twin = W(E_concat) + b
```

```text
E_twin ∈ ℝ²⁵⁶
```

---

## Why This Design?

| Branch | Rationale |
|----------|------------|
| **Cognitive (64-dim)** | Captures current clinical manifestation of disease. |
| **MRI (128-dim)** | Largest branch because structural neurodegeneration contributes substantial predictive information. |
| **Biomarkers (64-dim)** | Encodes AT(N) pathology including amyloid, tau, and metabolic dysfunction. |
| **Demographics (32-dim)** | Represents relatively static risk modifiers and cognitive reserve factors. |
| **Fusion Layer (256-dim)** | Produces a compact, patient-specific latent representation for downstream forecasting and digital twin simulations. |

> The resulting **256-dimensional Neuro-Digital Twin embedding** serves as the unified representation of an individual's cognitive state, brain structure, biological pathology, and risk profile, enabling downstream tasks such as trajectory prediction, survival analysis, intervention simulation, and personalized clinical decision support.


## Full Comparison: BiLSTM (47) vs ClinicalFusionNet (41)

## Feature Comparison: BiLSTM vs FusionNet

| Section | BiLSTM | FusionNet | Difference |
|----------|---------|------------|-------------|
| Cognitive | 10 | 8 | FusionNet excludes `adas_cog13` and `ravlt_learning` |
| MRI Volumetric | 20 | 20 | Identical feature set |
| Demographics | 5 | 5 | Identical feature set |
| CSF Biomarkers | 5 | 4 | FusionNet excludes `csf_abeta40` |
| PET + WMH | 4 | 4 | Identical features; incorporated into the Biomarker branch |
| Temporal | 3 | 0 | FusionNet does not explicitly use temporal variables |
| **Total** | **47** | **41** | **FusionNet uses 6 fewer features** |

---

## Detailed Feature Differences

### Features Present in BiLSTM but Excluded from FusionNet

| Category | Feature | Reason for Exclusion |
|-----------|----------|-----------------------|
| Cognitive | `adas_cog13` | Highly correlated with `adas_cog11`; removed to reduce redundancy. |
| Cognitive | `ravlt_learning` | Information partially captured by `ravlt_immediate` and `ravlt_forgetting`. |
| CSF | `csf_abeta40` | Primarily used to derive the Aβ42/Aβ40 relationship; the composite ratio feature is retained instead. |
| Temporal | `visit_month` | Temporal information modeled implicitly through sequence architectures in BiLSTM, not required in FusionNet. |
| Temporal | `months_since_baseline` | Excluded because FusionNet operates on a single fused representation rather than longitudinal sequences. |
| Temporal | `visit_number` | Not applicable in a static multimodal embedding framework. |

---

## Architecture Perspective

### BiLSTM Input Structure (47 Features)

```text
Cognitive           : 10
MRI Volumetric      : 20
Demographics        :  5
CSF Biomarkers      :  5
PET + WMH           :  4
Temporal Variables  :  3
────────────────────────
Total               : 47 Features
```

---

### FusionNet Input Structure (41 Features)

```text
Cognitive           :  8
MRI Volumetric      : 20
Demographics        :  5
Biomarkers          :  8
────────────────────────
Total               : 41 Features
```

Where:

```text
Biomarkers (8) =
CSF (4) + PET (3) + WMH (1)
```

---

## Conceptual Difference

| BiLSTM | FusionNet |
|---------|------------|
| Designed for **longitudinal sequence learning**. | Designed for **multimodal representation learning**. |
| Uses **explicit temporal variables**. | Uses a **static multimodal snapshot** at a given visit. |
| Captures disease progression through **time dependencies**. | Captures cross-modal interactions through **feature fusion**. |
| Input size: **47 features per time step**. | Input size: **41 features per patient visit**. |
| Output: Forecast of future trajectories. | Output: 256-dimensional patient embedding. |

---

## Why FusionNet Uses Fewer Features

The six removed features either provide **redundant information** or are **specific to temporal modeling**:

1. **Redundant cognitive assessments**
   - `adas_cog13`
   - `ravlt_learning`

2. **Derived biomarker support variable**
   - `csf_abeta40`

3. **Sequence-related temporal variables**
   - `visit_month`
   - `months_since_baseline`
   - `visit_number`

---

### Final Summary

```text
BiLSTM   : 47 features
FusionNet: 41 features
─────────────────────
Difference: 6 features removed

Removed Features:
• adas_cog13
• ravlt_learning
• csf_abeta40
• visit_month
• months_since_baseline
• visit_number
```

> **Interpretation:** BiLSTM emphasizes **when disease changes occur**, whereas FusionNet emphasizes **what the patient's current multimodal state looks like**. Together, they provide complementary capabilities within the Neuro-Digital Twin framework.


## ATN Biomarker Classification (used by CDSS)

## Convergence Biomarkers Tracked Across the Fusion Engine

The Fusion Engine continuously monitors a set of **eight high-value convergence biomarkers** that span the **AT(N) biological framework** and **clinical expression of disease**. These markers serve as a common reference layer across all predictive models within the Neuro-Digital Twin ecosystem.

| Marker | AT(N) Category | Threshold (Abnormal) | Direction of Pathology |
|----------|----------------|-----------------------|-------------------------|
| `amyloid_pet_suvr` | **A (Amyloid)** | > 1.11 SUVR | Higher values indicate greater amyloid plaque burden |
| `csf_abeta42` | **A (Amyloid)** | < 192 pg/mL | Lower values indicate amyloid pathology |
| `tau_pet_suvr` | **T (Tau)** | > 1.20 SUVR | Higher values indicate increased tau tangle burden |
| `csf_ptau181` | **T (Tau)** | > 23 pg/mL | Higher values indicate Alzheimer's-related tau pathology |
| `fdg_pet_suvr` | **N (Neurodegeneration)** | < 1.05 SUVR | Lower values indicate cerebral hypometabolism and neurodegeneration |
| `hippocampal_volume_total` | **N (Neurodegeneration)** | < 6500 mm³ | Lower volumes indicate hippocampal atrophy |
| `brain_atrophy_score` | **N (Neurodegeneration)** | > 0.40 | Higher scores reflect more severe global brain atrophy |
| `mmse` | **Clinical Stage** | < 24 | Lower scores indicate cognitive impairment |

---

## Convergence Monitoring Framework

```text
                    Fusion Engine
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
     Amyloid             Tau         Neurodegeneration
       (A)               (T)                (N)
        │                 │                  │
        │                 │                  │
 ┌──────┴──────┐   ┌──────┴──────┐   ┌───────┴────────┐
 │ Amyloid PET │   │  Tau PET    │   │   FDG-PET      │
 │ CSF Aβ42    │   │ CSF pTau181 │   │ Hippocampal Vol│
 └─────────────┘   └─────────────┘   │ Atrophy Score  │
                                     └────────────────┘
                                              │
                                              ▼
                                      Clinical Expression
                                              │
                                              ▼
                                           MMSE
```

---

## Clinical Interpretation

### Amyloid Domain (A)

| Marker | Interpretation |
|----------|----------------|
| `amyloid_pet_suvr > 1.11` | Positive amyloid PET indicating cerebral amyloid deposition |
| `csf_abeta42 < 192 pg/mL` | Reduced CSF Aβ42 due to sequestration into amyloid plaques |

---

### Tau Domain (T)

| Marker | Interpretation |
|----------|----------------|
| `tau_pet_suvr > 1.20` | Increased neurofibrillary tangle burden |
| `csf_ptau181 > 23 pg/mL` | Elevated phosphorylated tau supporting AD-specific tau pathology |

---

### Neurodegeneration Domain (N)

| Marker | Interpretation |
|----------|----------------|
| `fdg_pet_suvr < 1.05` | Reduced cerebral glucose metabolism |
| `hippocampal_volume_total < 6500 mm³` | Significant hippocampal atrophy |
| `brain_atrophy_score > 0.40` | Moderate-to-severe global brain volume loss |

---

### Clinical Domain

| Marker | Interpretation |
|----------|----------------|
| `mmse < 24` | Cognitive impairment consistent with MCI or dementia |

---

## Fusion Engine Role

These convergence biomarkers are used to:

- **Cross-validate predictions** generated by different models.
- Detect **agreement or disagreement** between modalities.
- Improve **robustness of disease staging**.
- Support **Human-in-the-Loop (HITL) review** when conflicting signals emerge.
- Generate **patient-specific explanations** within the Neuro-Digital Twin.
- Monitor **disease trajectories** during longitudinal follow-up.

---

## Example Convergence Assessment

| Biomarker | Patient Value | Threshold | Status |
|------------|----------------|------------|---------|
| Amyloid PET SUVR | 1.34 | > 1.11 | Abnormal |
| CSF Aβ42 | 148 pg/mL | < 192 | Abnormal |
| Tau PET SUVR | 1.28 | > 1.20 | Abnormal |
| CSF pTau181 | 29 pg/mL | > 23 | Abnormal |
| FDG-PET SUVR | 0.97 | < 1.05 | Abnormal |
| Hippocampal Volume | 5,820 mm³ | < 6,500 | Abnormal |
| Brain Atrophy Score | 0.48 | > 0.40 | Abnormal |
| MMSE | 22 | < 24 | Impaired |

**Interpretation:** This pattern demonstrates **strong biological and clinical convergence**, supporting an **A+ / T+ / N+ Alzheimer's disease profile with objective cognitive impairment**.

---

### Importance in the Neuro-Digital Twin

```text
AT(N) Biology
      +
Structural Degeneration
      +
Clinical Expression
      ↓
Convergence Analysis
      ↓
Fusion Engine Confidence
      ↓
Digital Twin Decision Support
```

> These **eight convergence biomarkers** form the **core validation layer** of the Fusion Engine, ensuring that predictions are not driven by a single modality but instead reflect consistent evidence across molecular pathology, neurodegeneration, and cognitive function.



# Clinical Brain Twin — Complete Agentic Architecture

## System Overview

```text
10-Agent System │ 9 LangGraph Nodes │ 2 HITL Pauses │ 1 Reflexion Loop

LLM            : gpt-4o-mini (JSON-mode)
Orchestrator   : LangGraph StateGraph
State Object   : BrainTwinState (TypedDict)
State Sections : 19 sections flowing through all agents
```

---

# Agent 1 — Digital Twin Orchestration Agent

| Property | Detail                                                                     |
| -------- | -------------------------------------------------------------------------- |
| File     | `orchestrator/graph.py`                                                    |
| Pattern  | ReAct + Routing                                                            |
| LLM      | None (pure graph logic)                                                    |
| Role     | Builds and compiles the LangGraph state machine and owns routing decisions |

## Responsibilities

* Constructs the 9-node `StateGraph`
* Defines conditional routing functions:

  * `_route_after_reflexion`
  * `_route_after_oversight`
* Compiles graph using `MemorySaver`
* Enables HITL resumability
* Defines interrupt checkpoints

## Interrupt Points

```python
interrupt_before = [
    "clinician_oversight_approval",
    "continuous_twin_learning"
]
```

## Routing Logic

```text
graph.invoke(initial_state)
    ↓
Sequential node execution
    ↓
Pause at HITL interrupts
    ↓
graph.update_state(...)
    ↓
graph.invoke(None, config)
    ↓
Conditional routing
```

---

# Agent 2 — Virtual Patient Modeling Agent (Node 1)

| Property | Detail                                      |
| -------- | ------------------------------------------- |
| File     | `agents/virtual_patient_modeling_runner.py` |
| Pattern  | CoT + ReAct                                 |
| LLM      | Available but bypassed                      |
| Tools    | 3 direct tool calls                         |

## Inputs

```text
patient_input.patient_id
```

## Outputs

```text
longitudinal_extractor
multimodal_fusion
population_similarity
```

## Workflow

### Step 1 — Longitudinal Extraction

```text
extract_longitudinal_data(patient_id)

Reads PostgreSQL

Returns:
47-feature matrix per visit

Cognitive     : 10
MRI           : 20
Demographics  : 5
CSF           : 5
PET           : 4
Temporal      : 3
```

Additional outputs:

```text
trends
completeness_flags
bilstm_ready_matrix
```

---

### Step 2 — Clinical FusionNet

```text
fuse_patient_modalities()
```

Latest visit only.

```text
Cognitive     (8) → 64-dim
MRI          (20) → 128-dim
Biomarkers    (8) → 64-dim
Demographics  (5) → 32-dim

Concat:
64 + 128 + 64 + 32
= 288

Linear(288→256)

L2 normalize

embedding_256
```

Outputs:

```text
embedding_256
modality_weights
P(CN/MCI/AD)
fusion_confidence
```

---

### Step 3 — Population Similarity

```text
population_similarity_search()
```

Uses:

```text
embedding_256
```

Performs:

```text
ChromaDB cosine search
k = 5
```

Returns:

```text
cohort_statistics
patient_z_scores
RAG clinical passages
```

---

# Agent 3 — Personalized Care Pathway Planning Agent (Node 2)

| Property | Detail                                   |
| -------- | ---------------------------------------- |
| File     | `agents/care_pathway_planning_runner.py` |
| Pattern  | Plan-and-Execute + Tree-of-Thought       |
| LLM      | gpt-4o-mini                              |
| Tools    | 5                                        |

## Inputs

```text
patient_input
longitudinal_extractor
```

## Outputs

```text
clinical_plan
```

---

## Phase 1 — Planning

LLM reasoning receives:

```text
Patient demographics
MMSE
CDR
CDRSB
MRI findings
Longitudinal trends
```

### Tool Usage

```text
retrieve_workflow_memory
retrieve_clinical_knowledge
record_reasoning_trace
```

### 7-Step Chain-of-Thought

1. Interpret cognitive scores
2. Review MRI findings
3. Assess biomarker trends
4. Evaluate APOE4/family history
5. Consult NIA-AA guidelines
6. Generate differential diagnosis
7. Formulate care pathway

Returns:

```json
{
  "reasoning_steps": [],
  "clinical_plan": "",
  "tests_ordered": [],
  "risk_factors": [],
  "urgency": "",
  "follow_up_interval_months": 0
}
```

---

## Phase 2 — Execution

ReAct loop.

```text
Thought
↓
Action
↓
Observation
```

Outputs:

```text
steps_executed
pathway_verification
guideline_references
execution_summary
```

---

# Agent 4 — Disease Progression Simulation Agent (Node 3)

| Property | Detail                                |
| -------- | ------------------------------------- |
| File     | `agents/disease_simulation_runner.py` |
| Pattern  | ReAct + Toolformer                    |
| LLM      | None                                  |
| Tools    | 8 deterministic models                |

## Inputs

```text
longitudinal_extractor
multimodal_fusion
```

## Outputs

```text
bilstm_forecast
hmm_result
monte_carlo_result
abm_result
bayesian_result
trajectory_model
fusion_result
cdss_output
```

---

## Disease Simulation Pipeline

### Tool 1 — BiLSTM Forecast

```text
forecast_cognitive_trajectory()

Model:
BiLSTM + Attention

Input:
T × 47 matrix

Output:
5-year trajectory forecast
risk_at_12m
risk_at_24m
uncertainty
```

---

### Tool 2 — HMM

```text
7-state HMM

States:
CN
MCI
early_AD
moderate_AD
severe_AD
+ transitional states
```

Outputs:

```text
current_state
transition_probs
dwell_times
```

---

### Tool 3 — Monte Carlo

```text
10,000 simulations

Seed:
BiLSTM trajectory
```

Outputs:

```text
p5–p95 bands
conversion probabilities
confidence intervals
```

---

### Tool 4 — ABM

```text
Intervention simulation

Medication
Lifestyle
Sleep
Diet
Training
```

Outputs:

```text
benefit_summary
optimal_combination
```

---

### Tool 5 — Bayesian Forecast

```text
ATN Bayesian Model

Prior × Likelihood
↓
Posterior
```

Outputs:

```text
risk_ad
credible_interval_95
biomarker_contributions
```

---

### Tool 6 — Disease Trajectory

```text
Jack Cascade Model
```

Outputs:

```text
disease_stage_position
progression_class
months_to_mci
months_to_ad
```

---

### Tool 7 — Fusion Engine

```text
Weighted Ensemble

BiLSTM : 0.40
HMM    : 0.30
MC     : 0.20
CDSS   : 0.10
```

Outputs:

```text
fused_risk
fused_stage
confidence
alert_flags
```

---

### Tool 8 — CDSS

```text
NIA-AA ATN Rule Engine
```

Outputs:

```text
ATN profile
clinical_stage
ICD-10 codes
recommendations
```

---

# Agent 5 — Clinical Insight & Explainability Agent (Node 4)

| Property | Detail                              |
| -------- | ----------------------------------- |
| File     | `agents/clinical_insight_runner.py` |
| Pattern  | Self-Explanation + CoT              |
| LLM      | gpt-4o-mini                         |
| Tools    | 3                                   |

## Outputs

```text
shap_result
confidence_score
uncertainty_calibration
explainability
```

## Tool Stack

### SHAP

```text
KernelSHAP

Top-5 drivers
Modality importance
Waterfall data
```

---

### Confidence Score

Components:

```text
Data completeness   25%
BiLSTM certainty    20%
HMM certainty       20%
Model agreement     25%
Temporal coverage   10%
```

---

### Uncertainty Calibration

Outputs:

```text
ECE
calibrated_risk
CI95
reliability_score
```

---

## Narrative Generation

Produces:

```text
Clinician explanation
Patient explanation
Uncertainty explanation
Additional data recommendations
```

---

# Agent 6 — Clinical Safety & Validation Agent (Node 5)

| Property | Detail                             |
| -------- | ---------------------------------- |
| File     | `agents/clinical_safety_runner.py` |
| Pattern  | Guardrails + Constraints           |
| LLM      | gpt-4o-mini                        |
| Tools    | 4                                  |

## Safety Checks

### Check 1

```text
Data Completeness
```

---

### Check 2

```text
Clinical Consistency
```

---

### Check 3

```text
Plan Completeness
```

---

### Check 4

```text
Data Quality
```

---

### Check 5

```text
Pathway Compliance
```

---

Outputs:

```text
checks_passed
checks_failed
overall_valid
blocking_issues
```

---

# Agent 7 — Digital Twin Reflexion Agent (Node 6)

| Property | Detail                       |
| -------- | ---------------------------- |
| File     | `agents/reflexion_runner.py` |
| Pattern  | Reflexion + Self-Correction  |
| LLM      | Critic + Refiner             |
| Tools    | 4                            |

---

## Pass 1 — Critic

Audits:

1. Risk plausibility
2. Biomarker-stage consistency
3. Urgency appropriateness
4. Model agreement
5. Guideline compliance
6. Missing critical data

Returns:

```text
issues_found
severity
needs_refinement
```

---

## Pass 2 — Refiner

If required:

```text
Refines outputs
Applies fixes
Documents changes
```

---

## Routing

```text
critical + replan_count < 2
        ↓
Return to Node 2

otherwise
        ↓
Proceed to HITL
```

---

# Agent 8 — Clinician Oversight & Approval Agent (Node 7)

| Property | Detail                                 |
| -------- | -------------------------------------- |
| File     | `agents/clinician_oversight_runner.py` |
| Pattern  | Approval Workflow                      |
| LLM      | None                                   |
| Tools    | hitl_approval                          |

---

## HITL Review Inputs

Clinician reviews:

```text
Fusion results
CDSS outputs
Explainability outputs
```

Provides:

```text
reviewed_by
approved
comments
modifications_json
```

---

## Routing

```text
approved = TRUE
      ↓
Node 8

approved = FALSE
      ↓
END
```

---

# Agent 9 — Clinical Summary & Reporting Agent (Node 8)

| Property | Detail                                |
| -------- | ------------------------------------- |
| File     | `agents/clinical_reporting_runner.py` |
| Pattern  | Structured Output                     |
| LLM      | None                                  |
| Tools    | generate_final_report                 |

## Final Report Sections

1. Header
2. Executive Summary
3. Patient Profile
4. Visit History
5. MRI Findings
6. Cognitive Assessment
7. Biomarkers
8. Forecast Summary
9. Probabilistic Forecast
10. Disease State
11. Intervention Analysis
12. Clinical Diagnosis
13. Treatment Plan
14. Monitoring Schedule
15. Referrals & Safety
16. Model Metadata

Outputs:

```text
report_id
sections
full_text
metadata
```

---

# Agent 10 — Continuous Twin Learning Agent (Node 9)

| Property | Detail                           |
| -------- | -------------------------------- |
| File     | `agents/twin_learning_runner.py` |
| Pattern  | Memory-Augmented                 |
| LLM      | None                             |
| Tools    | clinical_feedback                |

---

## HITL Feedback Collection

Clinician provides:

```text
rating
reasons
comments
section
```

---

## Feedback Outputs

```text
feedback_id
rating
reason_labels
data_quality_flag
display_summary
```

---

# Agent Comparison Table

| Agent                    | Node | Pattern               | LLM Used | Tool Calls | Output                |
| ------------------------ | ---- | --------------------- | -------- | ---------- | --------------------- |
| Orchestration            | —    | ReAct + Routing       | No       | 0          | Graph routing         |
| Virtual Patient Modeling | 1    | CoT + ReAct           | Optional | 3          | Longitudinal + Fusion |
| Care Planning            | 2    | Plan-Execute + ToT    | Yes      | 5          | Clinical plan         |
| Disease Simulation       | 3    | ReAct + Toolformer    | No       | 8          | Model outputs         |
| Clinical Insight & XAI   | 4    | Self-Explanation      | Yes      | 3          | Explainability        |
| Safety & Validation      | 5    | Guardrails            | Yes      | 4          | Validation            |
| Reflexion                | 6    | Self-Correction       | Yes      | 4          | Reflection            |
| Clinician Oversight      | 7    | Approval Workflow     | No       | 1          | HITL approval         |
| Clinical Reporting       | 8    | Structured Generation | No       | 1          | Final report          |
| Twin Learning            | 9    | Memory-Augmented      | No       | 1          | Feedback              |

---

# LLM vs Non-LLM Split

## Uses Active LLM Reasoning

```text
Agent 3 — Care Planning
Agent 5 — Explainability
Agent 6 — Safety Validation
Agent 7 — Reflexion
```

---

## Uses Deterministic Tools

```text
Agent 1  — Orchestrator
Agent 2  — Virtual Patient Modeling
Agent 4  — Disease Simulation
Agent 8  — HITL Oversight
Agent 9  — Clinical Reporting
Agent 10 — Twin Learning
```

---

# End-to-End Clinical Brain Twin Flow

```text
Patient Input
      ↓
Node 1  Virtual Patient Modeling
      ↓
Node 2  Care Pathway Planning
      ↓
Node 3  Disease Simulation
      ↓
Node 4  Explainability
      ↓
Node 5  Safety Validation
      ↓
Node 6  Reflexion
      ↓
      ├─ Critical → Replan → Node 2
      │
      └─ Proceed
              ↓
Node 7  Clinician HITL Approval
              ↓
      Approved?
         │
    Yes  ↓
Node 8  Clinical Reporting
              ↓
Node 9  Twin Learning HITL
              ↓
             END
```


```
Agentic AI-Driven Neuro Digital Twin Workflow
The Neuro Digital Twin orchestrates multiple specialized AI agents to transform patient data into explainable clinical recommendations while maintaining clinician oversight, safety validation, and continuous learning.

End-to-End Workflow
                                   ┌────────────────────┐
                                   │    USER INPUT      │
                                   │────────────────────│
                                   │ Patient ID         │
                                   │ EHR Data           │
                                   │ MRI Findings       │
                                   │ Biomarkers         │
                                   │ Cognitive Scores   │
                                   └─────────┬──────────┘
                                             │
                                             ▼
┌───────────────────────────────────────────────────────────────────────────┐
│ NODE 1: VIRTUAL PATIENT MODELING AGENT                                    │
├───────────────────────────────────────────────────────────────────────────┤
│ Purpose: Construct the patient's digital twin representation              │
│                                                                           │
│ Technologies:                                                             │
│ • PostgreSQL (47-feature longitudinal data)                               │
│ • PyTorch ClinicalFusionNet                                               │
│ • ChromaDB (patient embeddings)                                           │
│                                                                           │
│ Outputs:                                                                  │
│ • Longitudinal trajectories                                               │
│ • 256-dimensional patient embedding                                       │
│ • Similar patient cohorts                                                 │
└───────────────────────────────┬───────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────────────────┐
│ NODE 2: CARE PATHWAY PLANNING AGENT                                       │
├───────────────────────────────────────────────────────────────────────────┤
│ Purpose: Generate evidence-based clinical pathways                        │
│                                                                           │
│ Technologies:                                                             │
│ • GPT-4o-mini                                                             │
│ • TF-IDF Retrieval-Augmented Generation                                   │
│                                                                           │
│ Outputs:                                                                  │
│ • Personalized care recommendations                                       │
│ • Clinical guidance options                                               │
└───────────────────────────────┬───────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────────────────┐
│ NODE 3: DISEASE PROGRESSION SIMULATION AGENT                              │
├───────────────────────────────────────────────────────────────────────────┤
│ Purpose: Forecast disease trajectories and intervention outcomes          │
│                                                                           │
│ Models:                                                                   │
│ • BiLSTM                                                                  │
│ • Hidden Markov Model (HMM)                                               │
│ • Monte Carlo Simulation                                                  │
│ • Agent-Based Model (ABM)                                                 │
│ • Bayesian Forecasting                                                    │
│ • Disease Trajectory Models                                               │
│ • Multimodal Fusion Models                                                │
│ • Clinical Decision Support Models                                        │
│                                                                           │
│ Outputs:                                                                  │
│ • Conversion risk                                                         │
│ • Disease progression forecasts                                           │
│ • Intervention scenarios                                                  │
└───────────────────────────────┬───────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────────────────┐
│ NODE 4: CLINICAL INSIGHT & EXPLAINABILITY AGENT                           │
├───────────────────────────────────────────────────────────────────────────┤
│ Purpose: Explain model predictions to clinicians                          │
│                                                                           │
│ Technologies:                                                             │
│ • KernelSHAP                                                              │
│ • Confidence Estimation                                                   │
│ • Predictive Uncertainty Analysis                                         │
│                                                                           │
│ Outputs:                                                                  │
│ • Key risk drivers                                                        │
│ • Feature contributions                                                   │
│ • Confidence intervals                                                    │
│ • Explanation summaries                                                   │
└───────────────────────────────┬───────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────────────────┐
│ NODE 5: SAFETY & VALIDATION AGENT                                         │
├───────────────────────────────────────────────────────────────────────────┤
│ Purpose: Ensure clinical safety and regulatory compliance                 │
│                                                                           │
│ Components:                                                               │
│ • Five safety guardrails                                                  │
│ • Clinical rule validation                                                │
│ • Audit logging                                                           │
│                                                                           │
│ Outputs:                                                                  │
│ • Safety status                                                           │
│ • Validation findings                                                     │
│ • Audit trail entries                                                     │
└───────────────────────────────┬───────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────────────────┐
│ NODE 6: REFLEXION AGENT                                                   │
├───────────────────────────────────────────────────────────────────────────┤
│ Purpose: Critique and refine generated recommendations                    │
│                                                                           │
│ Components:                                                               │
│ • Critic Agent                                                            │
│ • Refiner Agent                                                           │
│                                                                           │
│ Rules:                                                                    │
│ • Maximum 2 replanning cycles                                             │
│ • Triggered when severe inconsistencies are detected                      │
└───────────────────────────────┬───────────────────────────────────────────┘
                                │
              severity = CRITICAL?
                        │
           ┌────────────┴─────────────┐
           │                          │
         YES                         NO
           │                          │
           ▼                          ▼
     Return to                  Continue to
 NODE 2: Care Planning             HITL
                                     │
                                     ▼
═══════════════════════════════════════════════════════════════════════════════
                HUMAN-IN-THE-LOOP CHECKPOINT 1
═══════════════════════════════════════════════════════════════════════════════

Clinician reviews:

• Predictions
• Explanations
• Recommended actions

Decision:

✓ Approve
✗ Reject
✎ Modify

                                     │
                                     ▼
┌───────────────────────────────────────────────────────────────────────────┐
│ NODE 7: CLINICIAN OVERSIGHT AGENT                                         │
├───────────────────────────────────────────────────────────────────────────┤
│ Tool: hitl_approval                                                       │
│                                                                           │
│ approved = False  → Workflow terminates                                   │
│ approved = True   → Continue                                              │
└───────────────────────────────┬───────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────────────────┐
│ NODE 8: CLINICAL SUMMARY REPORT AGENT                                     │
├───────────────────────────────────────────────────────────────────────────┤
│ Purpose: Assemble clinician-ready documentation                           │
│                                                                           │
│ Outputs:                                                                  │
│ • 16-section PDF report                                                   │
│ • Forecast summaries                                                      │
│ • Explainability findings                                                 │
│ • Intervention recommendations                                            │
│ • Audit information                                                       │
└───────────────────────────────┬───────────────────────────────────────────┘
                                │
                                ▼
═══════════════════════════════════════════════════════════════════════════════
                HUMAN-IN-THE-LOOP CHECKPOINT 2
═══════════════════════════════════════════════════════════════════════════════

Clinician reviews final report:

• Report completeness
• Recommendation quality
• Clinical usefulness

Provides feedback score and comments.

                                │
                                ▼
┌───────────────────────────────────────────────────────────────────────────┐
│ NODE 9: CONTINUOUS LEARNING AGENT                                         │
├───────────────────────────────────────────────────────────────────────────┤
│ Tool: clinical_feedback                                                   │
│                                                                           │
│ Purpose: Capture expert feedback for future improvement                   │
│                                                                           │
│ Outputs:                                                                  │
│ • Feedback repository updates                                             │
│ • Learning summaries                                                      │
│ • Performance monitoring metrics                                          │
└───────────────────────────────┬───────────────────────────────────────────┘
                                │
                                ▼
                      ┌─────────────────────┐
                      │        END          │
                      ├─────────────────────┤
                      │ report_id           │
                      │ patient_id          │
                      │ feedback_summary    │
                      └─────────────────────┘
Key Characteristics
* Agentic Architecture: 9 specialized agents collaborating through LangGraph orchestration.
* Human-Centered AI: Two Human-in-the-Loop checkpoints ensure clinician control.
* Explainable AI: Predictions are supported by feature-level explanations and uncertainty estimates.
* Safety by Design: Guardrails, validation checks, and audit trails are embedded throughout the workflow.
* Continuous Improvement: Clinician feedback drives ongoing optimization of the Neuro Digital Twin ecosystem.
```

```
╔══════════════════════════════════════════════════════════════════════════════════════════════╗
║                    CLINICAL BRAIN TWIN — COMPLETE ARCHITECTURE FLOW                          ║
║                    10 Agents │ 9 LangGraph Nodes │ 2 HITL Pauses │ 1 Reflexion Loop          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                                    USER / CLINICIAN                                         │
│                                                                                             │
│  CLI:  uv run python orchestrator/main.py                                                   │
│        --patient-id P001 --age 72 --sex 0 --mmse 24                                         │
│        --cdr-global 0.5 --cdrsb 2.5 --t1 /path/scan.nii                                     │
│                                                                                             │
│  API:  POST /api/runs  { patient_id, age, sex, mmse, cdr_global, cdrsb, mri_path }          │
└──────────────────────────────────────┬──────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│  ORCHESTRATION LAYER  (Agent 1 — Digital Twin Orchestration Agent)                          │
│  Pattern: ReAct + Routing  │  LLM: None  │  File: orchestrator/graph.py                     │
│                                                                                             │
│  1. Upsert patient visit → PostgreSQL (patient_longitudinal_data)                           │
│  2. Build initial BrainTwinState:                                                           │
│     { patient_input:{...}, errors:[], approved:False, replan_count:0 }                      │
│  3. Compile StateGraph with MemorySaver checkpointer                                        │
│  4. graph.invoke(initial_state, config)                                                     │
└──────────────────────────────────────┬──────────────────────────────────────────────────────┘
                                       │
                                       ▼
╔════════════════════════════════════════════════════════════════════════════════════════════╗
║  PHASE 1 — AUTOMATIC PIPELINE  (Nodes 1 → 6)                                               ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│  NODE 1 ── VIRTUAL PATIENT MODELING AGENT  (Agent 2)                                     │
│  Pattern: CoT + ReAct  │  LLM: Available (not used)  │  Tools called directly            │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│  INPUT: patient_id from state["patient_input"]                                           │
│                                                                                          │
│  STEP 1 ┌───────────────────────────────────────────────────────────────────┐            │
│         │  extract_longitudinal_data(patient_id)                            │            │
│         │  PostgreSQL ──► SELECT * FROM patient_longitudinal_data           │            │
│         │                                                                   │            │
│         │  Returns per visit:                                               │            │
│         │    Cognitive(10) + MRI(20) + Demographics(5)                      │            │
│         │    + CSF(5) + PET(4) + Temporal(3) = 47 features                  │            │
│         │                                                                   │            │
│         │  Also computes:                                                   │            │
│         │    trends{}        → baseline→latest delta for 16 biomarkers      │            │
│         │    completeness{}  → mri/cognitive/csf/pet flags per visit        │            │
│         │    bilstm_ready[]  → flat 47-feat matrix ordered for BiLSTM       │            │
│         └──────────────────────────────┬────────────────────────────────────┘            │
│                                        │ longitudinal_json                               │
│  STEP 2 ┌──────────────────────────────▼────────────────────────────────────┐            │
│         │  fuse_patient_modalities(longitudinal_json)                       │            │
│         │  Takes LATEST visit only                                          │            │
│         │                                                                   │            │
│         │  ClinicalFusionNet (4-branch MLP):                                │            │
│         │  Cognitive(8)  ──► Linear(8,64)   ──► 64-dim  ─┐                  │            │
│         │  MRI(20)       ──► Linear(20,128) ──► 128-dim  ─┼─► stack norms   │            │
│         │  Biomarker(8)  ──► Linear(8,64)   ──► 64-dim  ─┤  Linear(4,4)     │            │
│         │  Demographic(5)──► Linear(5,32)   ──► 32-dim  ─┘  Softmax         │            │
│         │                                                    ↓ attn_weights │            │
│         │  concat(288) ──► Linear(288,256) ──► L2-norm ──► embedding(256)   │            │
│         │  embedding   ──► Linear(256,3)   ──► Softmax ──► P(CN, MCI, AD)   │            │
│         │                                                                   │            │
│         │  Upserts embedding(256) → ChromaDB vector store                   │            │
│         └──────────────────────────────┬────────────────────────────────────┘            │
│                                        │ longitudinal_json + fusion_result_json          │
│  STEP 3 ┌──────────────────────────────▼────────────────────────────────────┐            │
│         │  population_similarity_search(longitudinal, fusion)               │            │
│         │  ChromaDB cosine similarity on embedding(256) → k=5 matches       │            │
│         │  cohort_stats: mean_mmse, mean_age, progression_rate_12m          │            │
│         │  patient_z_scores: z_mmse, z_age, z_fused_risk                    │            │
│         │  RAG: TF-IDF knowledge base → 5 clinical knowledge passages       │            │
│         └───────────────────────────────────────────────────────────────────┘            │
│                                                                                          │
│  STATE UPDATES:                                                                          │
│    state["longitudinal_extractor"] ← 47-feat history, trends, bilstm_ready               │
│    state["multimodal_fusion"]      ← embedding(256), P(CN/MCI/AD), attn_weights          │
│    state["population_similarity"]  ← k=5 similar patients, cohort stats, RAG             │
└──────────────────────────────────────┬───────────────────────────────────────────────────┘
                                       │
                                       ▼
┌────────────────────────────────────────────────────────────────────────────────────────────┐
│  NODE 2 ── CARE PATHWAY PLANNING AGENT  (Agent 3)                                          │
│  Pattern: Plan-and-Execute + Tree-of-Thought  │  LLM: gpt-4o-mini (ACTIVE)                 │
├────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                            │
│  INPUT: patient_input (age/sex/mmse/cdr/cdrsb)                                             │
│         longitudinal_extractor (latest visit + trends + visit_count)                       │
│                                                                                            │
│  PHASE 1 — PLANNING  (CoT + Tree-of-Thought)                                               │
│  ┌────────────────────────────────────────────────────────────────────────────────────┐    │
│  │  LLM (Planner Agent) called with patient profile                                   │    │
│  │                                                                                    │    │
│  │  LLM calls tools autonomously:                                                     │    │
│  │    retrieve_workflow_memory    → recall prior plans for this patient               │    │
│  │    retrieve_clinical_knowledge → search NIA-AA guideline knowledge base            │    │
│  │    record_reasoning_trace      → persist each CoT reasoning step                   │    │
│  │                                                                                    │    │
│  │  7-Step Chain-of-Thought (CoTTemplate):                                            │    │
│  │    1. Interpret cognitive scores (MMSE, CDR, CDRSB trends)                         │    │
│  │    2. Review MRI findings (hippocampal atrophy, ventricular expansion)             │    │
│  │    3. Assess biomarker trends (CSF Aβ42, tau, PET SUVR)                            │    │
│  │    4. Check genetic/familial risk (APOE4, family_history_ad)                       │    │
│  │    5. Consult NIA-AA ATN guidelines                                                │    │
│  │    6. Generate differential diagnosis                                              │    │
│  │    7. Formulate personalized care pathway                                          │    │
│  │                                                                                    │    │
│  │  Returns JSON: { reasoning_steps[7], clinical_plan, tests_ordered[],               │    │
│  │                  risk_factors[], urgency, follow_up_interval_months }              │    │
│  └────────────────────────────────────────────────────────────────────────────────────┘    │
│                                                                                            │
│  PHASE 2 — EXECUTION  (ReAct loop)                                                         │
│  ┌────────────────────────────────────────────────────────────────────────────────────┐    │
│  │  LLM (Executor Agent) iterates over each plan step:                                │    │
│  │    Thought → Action (tool call) → Observation → next Thought                       │    │
│  │                                                                                    │    │
│  │  retrieve_clinical_knowledge → verify each step against guidelines                 │    │
│  │  record_reasoning_trace      → log each ReAct cycle                                │    │
│  │                                                                                    │    │
│  │  Returns: steps_executed, step_results[], pathway_verification,                    │    │
│  │           risk_evaluation[], guideline_references[], execution_summary             │    │
│  └────────────────────────────────────────────────────────────────────────────────────┘    │
│                                                                                            │
│  STATE UPDATE: state["clinical_plan"] ← full care plan + execution results                 │
└──────────────────────────────────────┬─────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│  NODE 3 ── DISEASE PROGRESSION SIMULATION AGENT  (Agent 4)                                  │
│  Pattern: ReAct + Toolformer  │  LLM: None  │  8 tools called in fixed sequence             │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                             │
│  INPUT: longitudinal_extractor (bilstm_ready matrix), multimodal_fusion                     │
│                                                                                             │
│  ┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐                                               │
│  │  T1  │    │  T2  │    │  T3  │    │  T4  │                                               │
│  │BiLSTM│───►│ HMM  │    │  MC  │    │ ABM  │                                               │
│  └──┬───┘    └──┬───┘    └──┬───┘    └──┬───┘                                               │
│     │           │           │           │                                                   │
│     │  Tool 1   │  Tool 2   │  Tool 3   │  Tool 4                                           │
│     │           │           │  uses T1  │  uses T1                                          │
│                                                                                             │
│  Tool 1 ─ forecast_cognitive_trajectory(longitudinal_json)                                  │
│    BiLSTM + Attention model  │  Input: bilstm_ready (T×47)                                  │
│    Output: 5-yr monthly forecast, risk_at_12m/24m, conversion_risk_pct                      │
│                                                                                             │
│  Tool 2 ─ hmm_disease_progression(longitudinal_json)                                        │
│    7-state HMM, Viterbi + Forward algorithm                                                 │
│    Output: state_sequence[], current_state, next_state_probs(+6m/+12m/+24m)                 │
│                                                                                             │
│  Tool 3 ─ monte_carlo_simulation(bilstm_forecast_json)          ◄── uses Tool 1             │
│    10,000 stochastic trajectories seeded from BiLSTM                                        │
│    Output: trajectory_bands(p5/p25/p50/p75/p95), conversion_probabilities                   │
│                                                                                             │
│  Tool 4 ─ abm_intervention_simulation(bilstm_forecast_json)     ◄── uses Tool 1             │
│    Agent-based treatment simulation (medication/lifestyle/cognitive)                        │
│    Output: optimal_combination[], benefit_summary{risk_reduction, months_delayed}           │
│                                                                                             │
│  Tool 5 ─ bayesian_risk_forecast(longitudinal, fusion)                                      │
│    ATN Bayesian model  │  prior × likelihood(biomarkers) → posterior                        │
│    Output: P(CN/MCI/AD), credible_interval_95, biomarker_contributions                      │
│                                                                                             │
│  Tool 6 ─ disease_trajectory_model(longitudinal, bilstm, hmm)  ◄── uses T1+T2               │
│    Jack cascade sigmoid fitting per biomarker                                               │
│    Output: disease_stage_position(0-100), months_to_mci, months_to_ad                       │
│                                                                                             │
│  Tool 7 ─ fusion_engine(longitudinal, bilstm, hmm, mc, abm)    ◄── uses T1+T2+T3+T4         │
│    Weighted Average Ensemble:                                                               │
│    BiLSTM(0.40) + HMM(0.30) + MC(0.20) + CDSS(0.10) × quality_score                         │
│    Output: fused_risk(0-1), fused_stage, BCI per biomarker, confidence, narrative           │
│                                                                                             │
│  Tool 8 ─ cdss_recommendation(longitudinal, bilstm, hmm, mc, abm) ◄── uses T1+T2+T3+T4      │
│    NIA-AA ATN rule engine (config/cdss_guidelines.yaml)                                     │
│    Output: ATN profile(A+/T+/N+), clinical_stage, urgency, ICD-10[], recommendations[]      │
│                                                                                             │
│  STATE UPDATES:                                                                             │
│    state["bilstm_forecast"]    state["hmm_result"]        state["monte_carlo_result"]       │
│    state["abm_result"]         state["bayesian_result"]   state["trajectory_model"]         │
│    state["fusion_result"]      state["cdss_output"]                                         │
└──────────────────────────────────────┬──────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│  NODE 4 ── CLINICAL INSIGHT & EXPLAINABILITY AGENT  (Agent 5)                               │
│  Pattern: Self-Explanation + CoT  │  LLM: gpt-4o-mini (ACTIVE)                              │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                             │
│  INPUT: bilstm_forecast, hmm_result, cdss_output, fusion_result, longitudinal               │
│                                                                                             │
│  LLM calls 3 tools then generates 4 narratives:                                             │
│                                                                                             │
│  compute_shap_explanations(fusion_result)                                                   │
│    KernelSHAP on ClinicalFusionNet                                                          │
│    → top_5_drivers[{feature, shap_value, direction, interpretation}]                        │
│    → modality_shap{cognitive, mri, biomarkers, demographics}                                │
│    → waterfall_data[], bilstm_sensitivity, hmm_emission_sensitivity                         │
│                                                                                             │
│  compute_confidence_score(bilstm, hmm, fusion, longitudinal)                                │
│    5-component weighted score:                                                              │
│    ┌──────────────────────────────────────────────────────┐                                 │
│    │  data_completeness   (0.25) % of 47 features present │                                 │
│    │  bilstm_certainty    (0.20) 1 − BiLSTM uncertainty   │                                 │
│    │  hmm_state_certainty (0.20) Viterbi confidence       │  → overall_confidence           │
│    │  model_agreement     (0.25) cross-model alignment    │     tier: HIGH/MED/LOW          │
│    │  temporal_coverage   (0.10) visit spread & recency   │                                 │
│    └──────────────────────────────────────────────────────┘                                 │
│                                                                                             │
│  uncertainty_calibration(bilstm, hmm, mc, bayesian, fusion)                                 │
│    Temperature scaling + ECE proxy                                                          │
│    → calibrated_risk, calibrated_ci_95, ece, model_agreement(strong/moderate/weak)          │
│                                                                                             │
│  LLM generates:                                                                             │
│    clinician_explanation  → technical markdown with model rationale                         │
│    patient_explanation    → plain English (no clinical jargon)                              │
│    uncertainty_explanation → what is uncertain and why                                      │
│    recommended_additional_data → tests that would improve confidence                        │
│                                                                                             │
│  STATE UPDATE: state["shap_result"], state["confidence_score"],                             │
│                state["uncertainty_calibration"], state["explainability"]                    │
└──────────────────────────────────────┬──────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌────────────────────────────────────────────────────────────────────────────────────────────┐
│  NODE 5 ── CLINICAL SAFETY & VALIDATION AGENT  (Agent 6)                                   │
│  Pattern: Guardrails + Constraints  │  LLM: gpt-4o-mini (ACTIVE)                           │
├────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                            │
│  INPUT: patient_input, cdss_output, fusion_result, clinical_plan                           │
│                                                                                            │
│  LLM calls tools then runs 5 guardrail checks:                                             │
│                                                                                            │
│  ┌──────────────────────────────────────────────────────────────────────────────────────┐  │
│  │ CHECK 1 — DATA COMPLETENESS                                                          │  │
│  │   compute_confidence_score → data_completeness component                             │  │
│  │   Are all 4 modalities present? (MRI / Cognitive / CSF / PET)                        │  │
│  │   Result: pass / fail / warning                                                      │  │
│  ├──────────────────────────────────────────────────────────────────────────────────────┤  │
│  │ CHECK 2 — CLINICAL CONSISTENCY                                                       │  │
│  │   Does urgency align with severity? (severe_AD ≠ "routine")                          │  │
│  │   Does fused_stage align with CDSS clinical_stage?                                   │  │
│  │   Result: pass / fail / warning                                                      │  │
│  ├──────────────────────────────────────────────────────────────────────────────────────┤  │
│  │ CHECK 3 — PLAN COMPLETENESS                                                          │  │
│  │   Were all tests_ordered executed?                                                   │  │
│  │   Were all risk_factors evaluated?                                                   │  │
│  │   Result: pass / fail / warning                                                      │  │
│  ├──────────────────────────────────────────────────────────────────────────────────────┤  │
│  │ CHECK 4 — DATA QUALITY                                                               │  │
│  │   uncertainty_calibration → reliability_score < 0.40?                                │  │
│  │   Missing ICD-10 codes? Null critical fields?                                        │  │
│  │   Result: pass / fail / warning                                                      │  │
│  ├──────────────────────────────────────────────────────────────────────────────────────┤  │
│  │ CHECK 5 — PATHWAY COMPLIANCE                                                         │  │
│  │   retrieve_clinical_knowledge → NIA-AA guideline compliance check                    │  │
│  │   Recommended tests appropriate for diagnosed stage?                                 │  │
│  │   Result: pass / fail / warning                                                      │  │
│  └──────────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                            │
│  log_audit_event → writes governance record                                                │
│                                                                                            │
│  STATE UPDATE: state["validation"] ← {checks_passed, checks_failed,                        │
│                                        overall_valid, blocking_issues[]}                   │
└──────────────────────────────────────┬─────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌────────────────────────────────────────────────────────────────────────────────────────────┐
│  NODE 6 ── DIGITAL TWIN REFLEXION AGENT  (Agent 7)                                         │
│  Pattern: Reflexion + Self-Correction  │  LLM: gpt-4o-mini × 2 (Critic + Refiner)          │
├────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                            │
│  INPUT: cdss_output, fusion_result, replan_count                                           │
│                                                                                            │
│  ┌────────────────────── PASS 1: CRITIC AGENT ──────────────────────────────────────────┐  │
│  │  compute_confidence_score  → assess model reliability                                │  │
│  │  retrieve_clinical_knowledge → check guideline alignment                             │  │
│  │  record_reasoning_trace    → persist critic cycle                                    │  │
│  │                                                                                      │  │
│  │  Audits 6 issue categories:                                                          │  │
│  │    1. Risk score plausibility        4. Model agreement                              │  │
│  │    2. Biomarker-stage consistency    5. Guideline compliance                         │  │
│  │    3. Urgency appropriateness        6. Missing critical data                        │  │
│  │                                                                                      │  │
│  │  Returns: { severity: none│info│warning│critical, needs_refinement: bool }           │  │
│  └───────────────────────────────┬──────────────────────────────────────────────────────┘  │
│                                  │                                                         │
│              ┌───────────────────┴──────────────────────┐                                  │
│              │ severity == CRITICAL?                    │                                  │
│              │ AND replan_count < 2?                    │                                  │
│              └───────┬──────────────────┬───────────────┘                                  │
│                   YES│                NO│                                                  │
│                      │                  │                                                  │
│           _needs_replan=True    needs_refinement=True?                                     │
│           replan_count += 1            │                                                   │
│                      │         YES     │     NO                                            │
│                      │         │       │      │                                            │
│            ┌─────────┘  ┌──────┘       └──────┼──────────────────────────────┐             │
│            │            │                     │                              │             │
│       LOOP BACK    PASS 2: REFINER          PASS THROUGH                     │             │
│       to Node 2    retrieve_clinical_knowledge  final_output = original      │             │
│                    rewrite flagged sections                                  │             │
│                    record_reasoning_trace                                    │             │
│                    Returns: {refined_output, changes_made[]}                 │             │
│                                                                              │             │
│  STATE UPDATE: state["reflection"] ← { critic_result, refine_result,         │             │
│                                         final_output, _needs_replan }        │             │
│               state["replan_count"] += 1  (if replan)                        │             │
└─────────────────────────────────────────────────────┬──────────────────────────────────────┘
                                                      │
                    ┌─────────────────────────────────┤
                    │  CONDITIONAL ROUTING            │
                    │                                 │
            _needs_replan=True              _needs_replan=False
                    │                                 │
                    ▼                                 ▼
             ┌────────────┐                    continues to HITL
             │  LOOP BACK │
             │  Node 2    │◄─────────────────────────────────────
             │  (max 2×)  │         (replan loop)
             └────────────┘

╔══════════════════════════════════════════════════════════════════════════════════════════════╗
║  PHASE 2 — HUMAN-IN-THE-LOOP CHECKPOINT 1  (HITL Pause)                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════════════╝

                    ╔══════════════════════════════════╗
                    ║  GRAPH PAUSES                    ║
                    ║  interrupt_before=               ║
                    ║  ["clinician_oversight_approval"]║
                    ╚══════════════════════════════════╝
                                    │
                    Clinician reviews printed output:
                    ┌───────────────────────────────┐
                    │ FUSION RESULT                 │
                    │   fused_risk: 0.68 (HIGH)     │
                    │   fused_stage: mild_AD        │
                    │   BCI: 0.74                   │
                    │   confidence: probable        │
                    ├───────────────────────────────┤
                    │ CDSS OUTPUT                   │
                    │   clinical_stage: mild_AD     │
                    │   urgency: urgent             │
                    │   ICD-10: F00.1               │
                    │   recommendations: [...]      │
                    ├───────────────────────────────┤
                    │ EXPLAINABILITY                │
                    │   model_consensus: moderate   │
                    │   top driver: mmse (SHAP 0.31)│
                    │   certainty: probable         │
                    └───────────────────────────────┘
                                    │
                    Clinician inputs:
                      reviewed_by, approved (yes/no),
                      comments, modifications_json
                    (e.g. {"urgency":"urgent","clinical_stage":"mild_AD"})
                                    │
                    graph.update_state(config, {hitl_review, approved})

┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│  NODE 7 ── CLINICIAN OVERSIGHT & APPROVAL AGENT  (Agent 8)                                  │
│  Pattern: Approval Workflow  │  LLM: NONE  │  Tool: hitl_approval (direct)                  │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                             │
│  hitl_approval tool:                                                                        │
│    Validates modifications_json against safe field list                                     │
│    Applies overrides → modified_cdss                                                        │
│    Records: review_id (HITL-<pid>-<ts>), reviewed_at (UTC)                                  │
│             modifications_applied[{ field, old_value, new_value }]                          │
│    Sets:    pipeline_action: "proceed_to_report" | "halt_pipeline"                          │
│                                                                                             │
│  STATE UPDATE: state["hitl_review"], state["approved"]                                      │
│                                                                                             │
│                    ┌────────────────────────────────┐                                       │
│                    │  ROUTING after Node 7           │                                      │
│                    └──────┬─────────────────┬────────┘                                      │
│                    approved=True       approved=False                                       │
│                           │                  │                                              │
│                      Node 8              ┌───▼───┐                                          │
│                      (Report)            │  END  │ pipeline halted                          │
│                                          └───────┘                                          │
└──────────────────────────────────────┬──────────────────────────────────────────────────────┘
                                       │ (only if approved=True)

╔══════════════════════════════════════════════════════════════════════════════════════════════╗
║  PHASE 3 — AUTOMATIC REPORT GENERATION  (Node 8)                                             ║
╚══════════════════════════════════════════════════════════════════════════════════════════════╝

┌────────────────────────────────────────────────────────────────────────────────────────────┐
│  NODE 8 ── CLINICAL SUMMARY & REPORTING AGENT  (Agent 9)                                   │
│  Pattern: Structured Output Generation  │  LLM: NONE  │  Tool: generate_final_report       │
├────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                            │
│  INPUT: fusion, cdss, bilstm, longitudinal, hmm, mc, abm, hitl_review                      │
│                                                                                            │
│  generate_final_report assembles 16 sections:                                              │
│                                                                                            │
│  ┌────────────────────────────────────────────────────────────────────────────────────┐    │
│  │ SEC  1  HEADER              report_id(CBT-<pid>-<ts>), generated_at                │    │
│  │ SEC  2  EXECUTIVE SUMMARY   fused_risk, stage, certainty, headline                 │    │
│  │ SEC  3  PATIENT PROFILE     demographics, APOE4, baseline_diagnosis                │    │
│  │ SEC  4  VISIT HISTORY       all visit dates, diagnoses, date_range                 │    │
│  │ SEC  5  MRI FINDINGS        hippocampal volumes, atrophy, cortical thickness       │    │
│  │ SEC  6  COGNITIVE ASSESS    MMSE/CDR/CDRSB trends, ADAS-Cog, MoCA, RAVLT           │    │
│  │ SEC  7  BIOMARKERS          CSF(Aβ42, tau, p-tau), PET SUVR, ATN profile           │    │
│  │ SEC  8  FORECAST SUMMARY    BiLSTM 5-year trajectory, risk_at_12m/24m              │    │
│  │ SEC  9  PROBABILISTIC       Monte Carlo bands, conversion probabilities            │    │
│  │ SEC 10  DISEASE STATE        HMM current_state, Jack cascade position(0-100)       │    │
│  │ SEC 11  INTERVENTION         ABM optimal_combination, benefit_summary              │    │
│  │ SEC 12  CLINICAL DIAGNOSIS   ICD-10 codes, ATN classification, primary_dx          │    │
│  │ SEC 13  TREATMENT PLAN       recommendations[], lifestyle_interventions            │    │
│  │ SEC 14  MONITORING           follow_up_interval_months, monitoring_schedule        │    │
│  │ SEC 15  REFERRALS & SAFETY   referrals[], safety_flags[], HITL comments            │    │
│  │ SEC 16  MODEL METADATA       versions, config_version, pipeline_nodes, run_id      │    │
│  └────────────────────────────────────────────────────────────────────────────────────┘    │
│                                                                                            │
│  Returns: report_id, sections{16}, full_text (all sections concatenated)                   │
│                                                                                            │
│  STATE UPDATE: state["final_report"]                                                       │
└──────────────────────────────────────┬─────────────────────────────────────────────────────┘
                                       │

╔══════════════════════════════════════════════════════════════════════════════════════════════╗
║  PHASE 4 — HUMAN-IN-THE-LOOP CHECKPOINT 2  (Feedback Pause)                                  ║
╚══════════════════════════════════════════════════════════════════════════════════════════════╝

                    ╔══════════════════════════════════╗
                    ║  GRAPH PAUSES                    ║
                    ║  interrupt_before=               ║
                    ║  ["continuous_twin_learning"]    ║
                    ╚══════════════════════════════════╝
                                    │
                    Final report printed to clinician
                                    │
                    Clinician inputs:
                    ┌───────────────────────────────────┐
                    │ rating: like / dislike            │
                    │ reasons (if dislike):             │
                    │   1=NOT_ACCURATE                  │
                    │   2=NOT_RELEVANT                  │
                    │   3=INCOMPREHENSIVE               │
                    │   4=OFFENSIVE_OR_UNSAFE           │
                    │   5=BAD_FORMAT                    │
                    │   6=CITATIONS_WRONG               │
                    │   7=OTHER                         │
                    │ additional_text: free text        │
                    │ section: which section to rate    │
                    └───────────────────────────────────┘
                                    │
                    graph.update_state(config, {feedback})
                    graph.invoke(None, config)  ← resumes

┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│  NODE 9 ── CONTINUOUS TWIN LEARNING AGENT  (Agent 10)                                       │
│  Pattern: Memory-Augmented  │  LLM: NONE  │  Tool: clinical_feedback (direct)               │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                             │
│  INPUT: feedback (from clinician), final_report                                             │
│                                                                                             │
│  clinical_feedback tool:                                                                    │
│    feedback_id: "FB-<patient_id>-<timestamp>"                                               │
│    Maps reason codes → human-readable labels                                                │
│    Sets rating_icon: 👍 (like) or 👎 (dislike)                                               │
│    Sets data_quality_flag if rating=dislike + reason=NOT_ACCURATE                           │
│    Snapshots report_metadata for traceability                                               │
│    Generates display_summary for terminal output                                            │
│                                                                                             │
│  STATE UPDATE: state["feedback"]                                                            │
└──────────────────────────────────────┬──────────────────────────────────────────────────────┘
                                       │
                                       ▼
                               ┌───────────────┐
                               │     E N D     │
                               └───────────────┘

╔══════════════════════════════════════════════════════════════════════════════════════════════╗
║  FINAL OUTPUT TO CLINICIAN                                                                   ║
╠══════════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                              ║
║  Report ID  : CBT-PATIENT-001-20260611T143022                                                ║
║  Patient    : PATIENT-001                                                                    ║
║  Generated  : 2026-06-11T14:30:22Z                                                           ║
║  Feedback   : 👍  like                                                                       ║
║                                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════════════════════╗
║  COMPLETE DATA FLOW — STATE PASSING THROUGH ALL NODES                                        ║
╠══════════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                              ║
║  BrainTwinState (TypedDict) — 19 sections + 4 control fields                                 ║
║                                                                                              ║
║  Node 1 writes ──► longitudinal_extractor, multimodal_fusion, population_similarity          ║
║  Node 2 reads  ──► patient_input, longitudinal_extractor                                     ║
║  Node 2 writes ──► clinical_plan                                                             ║
║  Node 3 reads  ──► longitudinal_extractor, multimodal_fusion                                 ║
║  Node 3 writes ──► bilstm_forecast, hmm_result, monte_carlo_result, abm_result,              ║
║                    bayesian_result, trajectory_model, fusion_result, cdss_output             ║
║  Node 4 reads  ──► bilstm_forecast, hmm_result, cdss_output, fusion_result, longitudinal     ║
║  Node 4 writes ──► shap_result, confidence_score, uncertainty_calibration, explainability    ║
║  Node 5 reads  ──► patient_input, cdss_output, fusion_result, clinical_plan                  ║
║  Node 5 writes ──► validation                                                                ║
║  Node 6 reads  ──► cdss_output, fusion_result, replan_count                                  ║
║  Node 6 writes ──► reflection, replan_count                                                  ║
║  Node 7 reads  ──► hitl_review (injected by clinician)                                       ║
║  Node 7 writes ──► hitl_review (enriched), approved                                          ║
║  Node 8 reads  ──► fusion_result, cdss_output, bilstm_forecast, longitudinal,                ║
║                    hmm_result, monte_carlo_result, abm_result, hitl_review                   ║
║  Node 8 writes ──► final_report                                                              ║
║  Node 9 reads  ──► feedback (injected by clinician), final_report                            ║
║  Node 9 writes ──► feedback (enriched)                                                       ║
║                                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════════════════════╗
║  REFLEXION LOOP DETAIL                                                                       ║
╠══════════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                              ║
║  Node 2 ──► Node 3 ──► Node 4 ──► Node 5 ──► Node 6                                          ║
║                                                  │                                           ║
║                   ◄──────────────────────────────┘  (if severity=CRITICAL, replan_count<2)   ║
║                   replan_count: 0 → 1 → 2 (max)                                              ║
║                                                                                              ║
║  On 3rd pass (replan_count=2), regardless of severity → proceeds to HITL                     ║
║                                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════════════════════╗
║  INFRASTRUCTURE LAYER                                                                        ║
╠══════════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                              ║
║  ┌─────────────────┐  ┌────────────────┐  ┌───────────────────┐  ┌──────────────────────┐    ║
║  │   PostgreSQL    │  │   ChromaDB     │  │   PyTorch Models  │  │   OpenAI API         │    ║
║  │                 │  │                │  │                   │  │                      │    ║
║  │ patients        │  │ patient        │  │ BiLSTM+Attn.pt    │  │ gpt-4o-mini          │    ║
║  │ patient_long..  │  │ embeddings     │  │ FusionNet.pt      │  │ JSON-mode            │    ║
║  │ twin_states     │  │ (256-dim)      │  │ HMM.pkl           │  │ Used by:             │    ║
║  │ run_records     │  │                │  │                   │  │  Agent 3 (Planner)   │    ║
║  │                 │  │ RAG passages   │  │ ADNI population   │  │  Agent 5 (XAI)       │    ║
║  │ Used by:        │  │ (TF-IDF KB)    │  │ reference stats   │  │  Agent 6 (Safety)    │    ║
║  │  Node 1 (read)  │  │                │  │                   │  │  Agent 7 (Reflexion) │    ║
║  │  API (write)    │  │ Used by:       │  │ Used by:          │  │                      │    ║
║  │                 │  │  Node 1 Step2  │  │  Node 1 Step2     │  │                      │    ║
║  │                 │  │  Node 1 Step3  │  │  Node 3 Tool1     │  │                      │    ║
║  └─────────────────┘  └────────────────┘  └───────────────────┘  └──────────────────────┘    ║
║                                                                                              ║
║  ┌─────────────────┐  ┌────────────────┐  ┌───────────────────┐  ┌──────────────────────┐    ║
║  │   FastAPI       │  │   React/TS     │  │   Langfuse        │  │   Config YAMLs/JSON  │    ║
║  │   REST Backend  │  │   Frontend     │  │   Observability   │  │                      │    ║
║  │   /api/runs     │  │                │  │   (optional)      │  │ cdss_guidelines.yaml │    ║
║  │   /api/patients │  │   Dashboard    │  │   LLM tracing     │  │ bayesian_likes.yaml  │    ║
║  │   HITL endpoints│  │   HITL UI      │  │   token/cost/lat  │  │ fusion_engine.json   │    ║
║  └─────────────────┘  └────────────────┘  └───────────────────┘  │ interventions.yaml   │    ║
║                                                                  └──────────────────────┘    ║
╚══════════════════════════════════════════════════════════════════════════════════════════════╝
```