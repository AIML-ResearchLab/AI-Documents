



| CSV filename                                  | Type of data contained                                                                                  | Raw row count | Columns | Unique subjects | Visit labels | Key usable measurement count                         |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------: | ------: | --------------: | -----------: | ---------------------------------------------------- |
| `PTDEMOG_08Jun2026.csv`                       | Patient demographics: sex, education, birth year, marital/language/background fields                    |         6,149 |      84 |           4,868 |           38 | Gender: 6,019; Education: 6,000                      |
| `APOERES_08Jun2026.csv`                       | APOE genetic result / genotype                                                                          |         3,212 |      16 |           3,212 |            2 | Genotype: 3,212                                      |
| `FHQ_09Jun2026.csv`                           | Family history questionnaire: mother/father/sibling AD/dementia history                                 |         2,952 |      18 |           2,677 |           10 | Mother AD: 1,933; Father AD: 1,549                   |
| `FAMHXSIB_08Jun2026.csv`                      | Sibling family history: sibling dementia/AD details                                                     |         6,766 |      22 |           1,869 |           34 | Sibling dementia: 6,683; Sibling AD: 398             |
| `MMSE_24May2026.csv`                          | MMSE cognitive score and item-level MMSE fields                                                         |        14,732 |      58 |           4,668 |           42 | MMSCORE: 14,577                                      |
| `MOCA_08Jun2026.csv`                          | MoCA cognitive assessment                                                                               |         9,138 |      58 |           2,445 |           41 | MOCA total score: 3,875                              |
| `CDR_24May2026.csv`                           | Clinical Dementia Rating: CDR global and CDR Sum of Boxes                                               |        14,768 |      25 |           4,320 |           43 | CDRSB: 14,517; CDGLOBAL: 14,647                      |
| `FAQ_08Jun2026.csv`                           | Functional Activities Questionnaire: daily function score                                               |        13,464 |      27 |           2,966 |           42 | FAQTOTAL: 13,253                                     |
| `NEUROBAT_08Jun2026.csv`                      | Neuropsychological battery: memory, naming, clock, logical memory, AV delayed recall, etc.              |        17,720 |      83 |           4,706 |           44 | CLOCKSCOR: 12,832; AVDELTOT: 12,764; BNTTOTAL: 8,899 |
| `ITEM.csv`                                    | Detailed ADAS/MMSE item-level questionnaire responses                                                   |         5,341 |     766 |             755 |            7 | MMSE_Q1: 5,341; ADAS fields: 5,341                   |
| `DXSUM_24May2026.csv`                         | Diagnosis summary: CN/MCI/AD diagnosis and conversion-related fields                                    |        16,130 |      41 |           3,711 |           43 | DIAGNOSIS: 16,085                                    |
| `ADSP_PHC_T1_FS_08Jun2026.csv`                | MRI FreeSurfer structural brain features: hippocampus, ventricles, cortical thickness, regional volumes |        10,526 |     411 |           2,964 |           44 | Hippocampus/ICV features: 10,526                     |
| `ADNI1_Annual_2_Yr_3T_3_10_2026.csv`          | MRI image inventory / metadata: image ID, subject, modality, acquisition date, download info            |           306 |      12 |              89 |            3 | Image records: 306                                   |
| `ADSP_PHC_PET_Amyloid_Detailed_08Jun2026.csv` | Amyloid PET detailed regional SUVR features                                                             |         4,756 |     192 |           2,209 |           37 | Tracer: 4,756; hippocampus SUVR: 4,733               |
| `ADSP_PHC_PET_Tau_Detailed_08Jun2026.csv`     | Tau PET detailed regional SUVR features                                                                 |         2,278 |     191 |           1,325 |           35 | Tracer: 2,278; hippocampus SUVR: 2,268               |
| `UCBERKELEYFDG_8mm_02_17_23_08Jun2026.csv`    | FDG PET ROI metabolism values in long format                                                            |         7,524 |      10 |           1,687 |           22 | MEAN FDG value: 7,520                                |
| `UPENNBIOMK_ROCHE_ELECSYS_08Jun2026.csv`      | CSF biomarkers: ABETA40, ABETA42, TAU, PTAU                                                             |         3,174 |      13 |           1,660 |           28 | ABETA42: 3,167; TAU: 3,159; PTAU: 3,147              |
| `BSHRI_PLA_CSF_NULISA_CNS_08Jun2026.csv`      | CSF CNS proteomics / NULISA protein biomarker panel                                                     |       574,435 |      19 |           1,550 |            9 | NPQ: 571,109; protein targets: 134                   |
| `URMC_LABDATA_08Jun2026.csv`                  | General lab test results: test name, result value, units, ranges, flags                                 |       137,834 |      28 |           1,887 |           37 | Lab results: 137,834; unique test names: 136         |



**1. Demographics:** `AGE_AT_VISIT, PTGENDER, PTEDUCAT`
**2. Genetics:** `APOE4_COUNT`
**3. Family History:** `PARENT_AD_HISTORY`
**4. Cognitive Assessment Features:** `MMSCORE, MOCA, LIMMTOTAL, LDELTOTAL, AVDELTOT, BNTTOTAL, CLOCKSCOR, DIGITSCOR`
**5. Disease Severity Features:** `CDRSB, FAQTOTAL, TRABSCOR`
**6. MRI Features:** `EstimatedTotalIntraCranialVol_combat, BrainSegVol_combat, BrainSegVol_to_eTIV_combat, Left_Hippocampus_combat, Right_Hippocampus_combat, Left_Lateral_Ventricle_combat, Right_Lateral_Ventricle_combat, lh_entorhinal_thickness_combat, rh_entorhinal_thickness_combat, lh_middletemporal_thickness_combat, rh_middletemporal_thickness_combat, lh_fusiform_thickness_combat`
**7. CSF Biomarkers:** `ABETA40, ABETA42, TAU, PTAU, ABETA42_TAU_RATIO, PTAU_ABETA42_RATIO`
**8. PET Biomarkers:** `AMYLOID_GAAIN_SUMMARY_SUVR, AMYLOID_CTX_PRECUNEUS_SUVR, TAU_META_TEMPORAL_SUVR, TAU_CTX_ENTORHINAL_SUVR, FDG_METAROI_MEAN`

**Target Variables:** `FUTURE_MMSCORE_24M, FUTURE_DIAGNOSIS_24M, PROGRESSION_FLAG`

**Total input parameters:** `3 + 1 + 1 + 8 + 3 + 12 + 6 + 5 = 39`

| Target                 | Meaning                                  |
| ---------------------- | ---------------------------------------- |
| `FUTURE_MMSCORE_24M`   | MMSE after 24 months                     |
| `FUTURE_DIAGNOSIS_24M` | CN / MCI / AD after 24 months            |
| `PROGRESSION_FLAG`     | Example: MMSE drop greater than 3 points |


```
39 multimodal input parameters
        ↓
Digital Twin model
        ↓
24-month MMSE prediction
Diagnosis prediction
Progression risk
Agentic explanation + what-if simulation
```


**1. Demographics, use this CSV:**

| Parameter      | CSV file                | Column name / derivation                       |
| -------------- | ----------------------- | ---------------------------------------------- |
| `PTGENDER`     | `PTDEMOG_08Jun2026.csv` | Direct column: `PTGENDER`                      |
| `PTEDUCAT`     | `PTDEMOG_08Jun2026.csv` | Direct column: `PTEDUCAT`                      |
| `AGE_AT_VISIT` | `PTDEMOG_08Jun2026.csv` | Derived from `VISDATE` and `PTDOBYY` / `PTDOB` |

Use these join keys: `RID + VISCODE2`

For AGE_AT_VISIT, create it like: `AGE_AT_VISIT = visit year - birth year` (`VISDATE - PTDOBYY`)



**2. Genetics, use this CSV:**

| Parameter     | CSV file                | Source column | How to create                          |
| ------------- | ----------------------- | ------------- | -------------------------------------- |
| `APOE4_COUNT` | `APOERES_08Jun2026.csv` | `GENOTYPE`    | Count how many `4` alleles are present |

Your file has columns like:

```
RID
PTID
VISCODE
GENOTYPE
APTESTDT
```

Example conversion:

| `GENOTYPE` | `APOE4_COUNT` |
| ---------- | ------------: |
| `2/2`      |             0 |
| `2/3`      |             0 |
| `3/3`      |             0 |
| `2/4`      |             1 |
| `3/4`      |             1 |
| `4/4`      |             2 |



Use join key mainly: `RID`

Because APOE genotype is static, not visit-changing.

Final genetics table: `RID, APOE4_COUNT`


**3. Family History, use this CSV:**

| Parameter           | CSV file            | Source columns         | How to create                                    |
| ------------------- | ------------------- | ---------------------- | ------------------------------------------------ |
| `PARENT_AD_HISTORY` | `FHQ_09Jun2026.csv` | `FHQMOMAD`, `FHQDADAD` | `1` if mother or father has AD history, else `0` |


file has these useful columns:

```
RID
VISCODE
VISCODE2
VISDATE
FHQMOMAD
FHQDADAD
FHQSIB
```

| Column     | Meaning                                               |
| ---------- | ----------------------------------------------------- |
| `FHQMOMAD` | Mother Alzheimer’s disease history                    |
| `FHQDADAD` | Father Alzheimer’s disease history                    |
| `FHQSIB`   | Sibling history available / sibling history indicator |


selected parameter, use only parents:

```
PARENT_AD_HISTORY = 1 if FHQMOMAD == 1 or FHQDADAD == 1
PARENT_AD_HISTORY = 0 if both are 0
```

`Handle -4 as missing/unknown.`

Use join key: `RID + VISCODE2`

Final feature: `RID, PARENT_AD_HISTORY`


**4. Cognitive Assessment Features, use these CSV files:**

| Parameter   | CSV file                 | Column name | What it represents                            |
| ----------- | ------------------------ | ----------- | --------------------------------------------- |
| `MMSCORE`   | `MMSE_24May2026.csv`     | `MMSCORE`   | Mini-Mental State Examination total score     |
| `MOCA`      | `MOCA_08Jun2026.csv`     | `MOCA`      | Montreal Cognitive Assessment total score     |
| `LIMMTOTAL` | `NEUROBAT_08Jun2026.csv` | `LIMMTOTAL` | Logical Memory Immediate total                |
| `LDELTOTAL` | `NEUROBAT_08Jun2026.csv` | `LDELTOTAL` | Logical Memory Delayed total                  |
| `AVDELTOT`  | `NEUROBAT_08Jun2026.csv` | `AVDELTOT`  | Auditory Verbal Learning delayed recall total |
| `BNTTOTAL`  | `NEUROBAT_08Jun2026.csv` | `BNTTOTAL`  | Boston Naming Test total                      |
| `CLOCKSCOR` | `NEUROBAT_08Jun2026.csv` | `CLOCKSCOR` | Clock drawing score                           |
| `DIGITSCOR` | `NEUROBAT_08Jun2026.csv` | `DIGITSCOR` | Digit symbol / attention score                |


So this group uses mainly 3 CSV files:

```
MMSE_24May2026.csv
MOCA_08Jun2026.csv
NEUROBAT_08Jun2026.csv
```

Use join keys: `RID + VISCODE2`

Final cognitive feature table:

| Join keys         | Cognitive features                                                                            |
| ----------------- | --------------------------------------------------------------------------------------------- |
| `RID`, `VISCODE2` | `MMSCORE`, `MOCA`, `LIMMTOTAL`, `LDELTOTAL`, `AVDELTOT`, `BNTTOTAL`, `CLOCKSCOR`, `DIGITSCOR` |


**5. Disease Severity Features, use these CSV files:**

| Parameter  | CSV file                 | Column name | What it represents                                                            |
| ---------- | ------------------------ | ----------- | ----------------------------------------------------------------------------- |
| `CDRSB`    | `CDR_24May2026.csv`      | `CDRSB`     | Clinical Dementia Rating Sum of Boxes; measures dementia severity             |
| `FAQTOTAL` | `FAQ_08Jun2026.csv`      | `FAQTOTAL`  | Functional Activities Questionnaire total; measures daily function impairment |
| `TRABSCOR` | `NEUROBAT_08Jun2026.csv` | `TRABSCOR`  | Trail Making Test B score; executive function / cognitive flexibility         |


So this group uses 3 CSV files:

```
CDR_24May2026.csv
FAQ_08Jun2026.csv
NEUROBAT_08Jun2026.csv
```

Use join keys: `RID + VISCODE2`

Final disease severity feature table:

| Join keys         | Disease severity features       |
| ----------------- | ------------------------------- |
| `RID`, `VISCODE2` | `CDRSB`, `FAQTOTAL`, `TRABSCOR` |



**6. MRI Features, use this CSV file:**

`ADSP_PHC_T1_FS_08Jun2026.csv`

| Parameter                              | CSV file                       | Column name | Meaning                                        |
| -------------------------------------- | ------------------------------ | ----------- | ---------------------------------------------- |
| `EstimatedTotalIntraCranialVol_combat` | `ADSP_PHC_T1_FS_08Jun2026.csv` | Same        | Estimated total intracranial volume            |
| `BrainSegVol_combat`                   | `ADSP_PHC_T1_FS_08Jun2026.csv` | Same        | Total segmented brain volume                   |
| `BrainSegVol_to_eTIV_combat`           | `ADSP_PHC_T1_FS_08Jun2026.csv` | Same        | Brain volume normalized by intracranial volume |
| `Left_Hippocampus_combat`              | `ADSP_PHC_T1_FS_08Jun2026.csv` | Same        | Left hippocampal volume                        |
| `Right_Hippocampus_combat`             | `ADSP_PHC_T1_FS_08Jun2026.csv` | Same        | Right hippocampal volume                       |
| `Left_Lateral_Ventricle_combat`        | `ADSP_PHC_T1_FS_08Jun2026.csv` | Same        | Left lateral ventricle volume                  |
| `Right_Lateral_Ventricle_combat`       | `ADSP_PHC_T1_FS_08Jun2026.csv` | Same        | Right lateral ventricle volume                 |
| `lh_entorhinal_thickness_combat`       | `ADSP_PHC_T1_FS_08Jun2026.csv` | Same        | Left entorhinal cortex thickness               |
| `rh_entorhinal_thickness_combat`       | `ADSP_PHC_T1_FS_08Jun2026.csv` | Same        | Right entorhinal cortex thickness              |
| `lh_middletemporal_thickness_combat`   | `ADSP_PHC_T1_FS_08Jun2026.csv` | Same        | Left middle temporal cortex thickness          |
| `rh_middletemporal_thickness_combat`   | `ADSP_PHC_T1_FS_08Jun2026.csv` | Same        | Right middle temporal cortex thickness         |
| `lh_fusiform_thickness_combat`         | `ADSP_PHC_T1_FS_08Jun2026.csv` | Same        | Left fusiform cortex thickness                 |


Use join keys: `RID + VISCODE2`
Useful date/visit columns in this MRI file:

```
RID
PTID
VISCODE
VISCODE2
PHC_SCANDATE
PHC_Age_T1
```

Final MRI feature table:

```
RID
VISCODE2
EstimatedTotalIntraCranialVol_combat
BrainSegVol_combat
BrainSegVol_to_eTIV_combat
Left_Hippocampus_combat
Right_Hippocampus_combat
Left_Lateral_Ventricle_combat
Right_Lateral_Ventricle_combat
lh_entorhinal_thickness_combat
rh_entorhinal_thickness_combat
lh_middletemporal_thickness_combat
rh_middletemporal_thickness_combat
lh_fusiform_thickness_combat
```


**7. CSF Biomarkers, use this CSV:**

`UPENNBIOMK_ROCHE_ELECSYS_08Jun2026.csv`

| Parameter            | CSV file                                 | Source column / derivation | Meaning            |
| -------------------- | ---------------------------------------- | -------------------------- | ------------------ |
| `ABETA40`            | `UPENNBIOMK_ROCHE_ELECSYS_08Jun2026.csv` | `ABETA40`                  | Amyloid beta 40    |
| `ABETA42`            | `UPENNBIOMK_ROCHE_ELECSYS_08Jun2026.csv` | `ABETA42`                  | Amyloid beta 42    |
| `TAU`                | `UPENNBIOMK_ROCHE_ELECSYS_08Jun2026.csv` | `TAU`                      | Total tau          |
| `PTAU`               | `UPENNBIOMK_ROCHE_ELECSYS_08Jun2026.csv` | `PTAU`                     | Phosphorylated tau |
| `ABETA42_TAU_RATIO`  | Derived                                  | `ABETA42 / TAU`            | Amyloid-tau ratio  |
| `PTAU_ABETA42_RATIO` | Derived                                  | `PTAU / ABETA42`           | pTau-amyloid ratio |

`ADSP_PHC_PET_Tau_Detailed_08Jun2026.csv`

Use join keys: `RID + VISCODE2`

Final CSF table:

```
RID
VISCODE2
ABETA40
ABETA42
TAU
PTAU
ABETA42_TAU_RATIO
PTAU_ABETA42_RATIO
```

**8. PET Biomarkers, use these CSV files:**

| Parameter                    | CSV file                                      | Source column / filter           | Meaning                            |
| ---------------------------- | --------------------------------------------- | -------------------------------- | ---------------------------------- |
| `AMYLOID_GAAIN_SUMMARY_SUVR` | `ADSP_PHC_PET_Amyloid_Detailed_08Jun2026.csv` | `GAAIN_SUMMARY_SUVR`             | Global amyloid PET burden          |
| `AMYLOID_CTX_PRECUNEUS_SUVR` | `ADSP_PHC_PET_Amyloid_Detailed_08Jun2026.csv` | `CTX_PRECUNEUS_SUVR`             | Amyloid burden in precuneus cortex |
| `TAU_META_TEMPORAL_SUVR`     | `ADSP_PHC_PET_Tau_Detailed_08Jun2026.csv`     | `META_TEMPORAL_SUVR`             | Tau burden in meta-temporal region |
| `TAU_CTX_ENTORHINAL_SUVR`    | `ADSP_PHC_PET_Tau_Detailed_08Jun2026.csv`     | `CTX_ENTORHINAL_SUVR`            | Tau burden in entorhinal cortex    |
| `FDG_METAROI_MEAN`           | `UCBERKELEYFDG_8mm_02_17_23_08Jun2026.csv`    | `MEAN` where `ROINAME = MetaROI` | FDG metabolism in MetaROI          |


Use join keys: `RID + VISCODE2`

Final PET table:

```
RID
VISCODE2
AMYLOID_GAAIN_SUMMARY_SUVR
AMYLOID_CTX_PRECUNEUS_SUVR
TAU_META_TEMPORAL_SUVR
TAU_CTX_ENTORHINAL_SUVR
FDG_METAROI_MEAN
```

Small note: FDG file is long format, so first filter: `ROINAME == "MetaROI"`. Then rename: `MEAN → FDG_METAROI_MEAN`






```
CSV files
  ↓
Clean RID + VISCODE2
  ↓
Convert VISCODE2 to VISIT_MONTH
  ↓
Create current visit row
  ↓
Find +24 month target
  ↓
Split by RID
  ↓
Scale/impute train-only
  ↓
Create modality tensors
  ↓
Modality encoders
  ↓
Transformer fusion
  ↓
Patient embedding
  ↓
3 prediction heads
  ↓
MMSE + Diagnosis + Progression loss
  ↓
Backpropagation
  ↓
Save best model
```

