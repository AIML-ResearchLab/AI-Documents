## 1. Demographics — demographics_generator.py

```
import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
np.random.seed(42)

num_records = 10000

ethnicity = ['Asian', 'White', 'Black', 'Hispanic']
marital_status = ['Single', 'Married', 'Divorced']
smoking = ['Never', 'Former', 'Current']
locations = ['Bangalore', 'Mumbai', 'Delhi', 'Chennai']
blood_groups = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']

records = []

for i in range(num_records):
    age = np.random.randint(18, 90)
    height = round(np.random.normal(165, 10), 1)
    weight = round(np.random.normal(70, 15), 1)
    bmi = round(weight / ((height / 100) ** 2), 1)

    records.append({
        'Patient': f'P{i+1:05d}',
        'Age': age,
        'Gender': np.random.choice(['Male', 'Female']),
        'Date of Birth': fake.date_of_birth(minimum_age=18, maximum_age=90),
        'Ethnicity / Race': np.random.choice(ethnicity),
        'Height': height,
        'Weight': weight,
        'BMI': bmi,
        'Marital Status': np.random.choice(marital_status),
        'Smoking Status': np.random.choice(smoking),
        'Alcohol Consumption': np.random.choice(['Low', 'Moderate', 'High']),
        'Sleep Duration': round(np.random.normal(7, 1.5), 1),
        'Family History of Neurological Disease': np.random.choice(['Yes', 'No']),
        'Geographic Location': np.random.choice(locations),
        'Blood Group': np.random.choice(blood_groups)
    })

pd.DataFrame(records).to_csv('demographics.csv', index=False)
print('demographics.csv generated successfully')
```

## 2. Longitudinal — longitudinal_generator.py

```
import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
np.random.seed(42)

num_records = 10000

records = []

for i in range(num_records):
    records.append({
        'Patient': f'P{i+1:05d}',
        'Visit Date': fake.date_this_decade(),
        'Disease Duration': round(np.random.uniform(0, 15), 1),
        'Disease Stage': np.random.choice(['Early', 'Moderate', 'Advanced']),
        'Symptom Onset Date': fake.date_this_decade(),
        'Hospital Admission History': np.random.randint(0, 10),
        'Cognitive Decline Trend': round(np.random.uniform(0, 1), 2),
        'Mobility Decline Trend': round(np.random.uniform(0, 1), 2),
        'Seizure Timeline': np.random.randint(0, 20),
        'Tremor Progression': round(np.random.uniform(0, 10), 1)
    })

pd.DataFrame(records).to_csv('longitudinal.csv', index=False)
print('longitudinal.csv generated successfully')
```

## 3. Vitals — vitals_generator.py

```
import pandas as pd
import numpy as np

np.random.seed(42)
num_records = 10000

records = []

for i in range(num_records):
    records.append({
        'Patient': f'P{i+1:05d}',
        'Heart Rate': np.random.randint(60, 110),
        'Oxygen Saturation (SpO2)': np.random.randint(90, 100),
        'Blood Pressure (Systolic)': np.random.randint(100, 180),
        'Blood Pressure (Diastolic)': np.random.randint(60, 110),
        'Pulse Rate': np.random.randint(60, 110),
        'Body Temperature': round(np.random.normal(98.6, 1), 1)
    })

pd.DataFrame(records).to_csv('vitals.csv', index=False)
print('vitals.csv generated successfully')
```

## 4. Neurological Score — neurological_score_generator.py

```
import pandas as pd
import numpy as np

np.random.seed(42)
num_records = 10000

records = []

for i in range(num_records):
    records.append({
        'Patient': f'P{i+1:05d}',
        'MMSE Score': np.random.randint(0, 30),
        'MoCA Score': np.random.randint(0, 30),
        'NIH Stroke Scale (NIHSS)': np.random.randint(0, 42),
        'UPDRS Score': np.random.randint(0, 200),
        'Modified Rankin Scale (mRS)': np.random.randint(0, 6),
        'Speech Assessment Score': np.random.randint(0, 100)
    })

pd.DataFrame(records).to_csv('neurological_scores.csv', index=False)
print('neurological_scores.csv generated successfully')
```

## 5. MRI Feature Extraction — mri_feature_generator.py

```
import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
np.random.seed(42)

num_records = 10000

brain_regions = ['Frontal', 'Temporal', 'Parietal', 'Occipital']

records = []

for i in range(num_records):
    records.append({
        'Patient': f'P{i+1:05d}',
        'MRI Scan Date': fake.date_this_decade(),
        'Hippocampal volume': round(np.random.normal(3500, 500), 2),
        'Cortical thickness': round(np.random.normal(2.5, 0.5), 2),
        'Brain atrophy': round(np.random.uniform(0, 1), 2),
        'White matter lesions': np.random.randint(0, 20),
        'Ventricular enlargement': round(np.random.uniform(0, 1), 2),
        'Stroke lesion size': round(np.random.uniform(0, 100), 2),
        'Brain connectivity': round(np.random.uniform(0, 1), 2),
        'DTI white matter integrity': round(np.random.uniform(0, 1), 2),
        'Microbleeds': np.random.randint(0, 10),
        'Tumor region': np.random.choice(brain_regions),
        'Lesion Count': np.random.randint(0, 20),
        'Lesion Volume': round(np.random.uniform(0, 200), 2),
        'Tumor Size': round(np.random.uniform(0, 80), 2),
        'Tumor Location': np.random.choice(brain_regions),
        'Amyloid PET-MRI Correlation': round(np.random.uniform(0, 1), 2)
    })

pd.DataFrame(records).to_csv('mri_features.csv', index=False)
print('mri_features.csv generated successfully')
```

## 6. Symptoms — symptoms_generator.py

```
import pandas as pd
import numpy as np

np.random.seed(42)
num_records = 10000

records = []

for i in range(num_records):
    records.append({
        'Patient': f'P{i+1:05d}',
        'Memory Loss': np.random.randint(0, 10),
        'Tremor Severity': np.random.randint(0, 10),
        'Seizure Frequency': np.random.randint(0, 20),
        'Weakness / Paralysis': np.random.randint(0, 10),
        'Sleep Disturbance': np.random.randint(0, 10),
        'Headache Severity': np.random.randint(0, 10)
    })

pd.DataFrame(records).to_csv('symptoms.csv', index=False)
print('symptoms.csv generated successfully')
```

## 7. EEG  — eeg_generator.py

```
import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
np.random.seed(42)

num_records = 10000
waveforms = ['Normal', 'Abnormal', 'Epileptic']

records = []

for i in range(num_records):
    records.append({
        'Patient': f'P{i+1:05d}',
        'EEG Recording Date': fake.date_this_decade(),
        'EEG Signal Waveform': np.random.choice(waveforms),
        'Delta Wave Power': round(np.random.uniform(0, 100), 2),
        'Theta Wave Power': round(np.random.uniform(0, 100), 2),
        'Beta Wave Power': round(np.random.uniform(0, 100), 2),
        'Gamma Wave Activity': round(np.random.uniform(0, 100), 2),
        'Spike Detection': np.random.choice(['Yes', 'No']),
        'EEG Complexity Metrics': round(np.random.uniform(0, 1), 3)
    })

pd.DataFrame(records).to_csv('eeg.csv', index=False)
print('eeg.csv generated successfully')
```

## 8. Biomarker — biomarker_generator.py

```
import pandas as pd
import numpy as np

np.random.seed(42)
num_records = 10000

records = []

for i in range(num_records):
    records.append({
        'Patient': f'P{i+1:05d}',
        'Amyloid-beta': round(np.random.normal(500, 100), 2),
        'Tau Protein': round(np.random.normal(80, 20), 2),
        'Alpha-synuclein': round(np.random.normal(50, 15), 2),
        'Neurofilament Light (NfL)': round(np.random.normal(25, 5), 2),
        'Phosphorylated Tau (p-Tau)': round(np.random.normal(30, 8), 2),
        'Alpha-synuclein.1': round(np.random.normal(50, 15), 2),
        'GFAP': round(np.random.normal(100, 20), 2),
        'UCH-L1': round(np.random.normal(120, 30), 2),
        'p-Tau181': round(np.random.normal(40, 10), 2)
    })

pd.DataFrame(records).to_csv('biomarkers.csv', index=False)
print('biomarkers.csv generated successfully')
```

## 9. Laboratory — laboratory_generator.py

```
import pandas as pd
import numpy as np

np.random.seed(42)
num_records = 10000

records = []

for i in range(num_records):
    records.append({
        'Patient': f'P{i+1:05d}',
        'Blood Glucose / HbA1c': round(np.random.normal(100, 20), 2),
        'C-Reactive Protein (CRP)': round(np.random.normal(5, 2), 2),
        'Total Cholesterol': round(np.random.normal(180, 30), 2),
        'LDL Cholesterol': round(np.random.normal(100, 20), 2),
        'HDL Cholesterol': round(np.random.normal(50, 10), 2),
        'Triglycerides': round(np.random.normal(150, 40), 2),
        'ESR (Erythrocyte Sedimentation Rate)': round(np.random.normal(20, 5), 2),
        'Blood Urea Nitrogen': round(np.random.normal(15, 4), 2),
        'ALT': round(np.random.normal(35, 10), 2),
        'AST': round(np.random.normal(30, 10), 2),
        'Bilirubin': round(np.random.normal(1, 0.5), 2),
        'Hemoglobin': round(np.random.normal(14, 2), 2),
        'WBC Count': round(np.random.normal(7000, 1500), 2),
        'Platelet Count': round(np.random.normal(250000, 50000), 2),
        'RBC Count': round(np.random.normal(5, 1), 2),
        'TSH': round(np.random.normal(2, 1), 2),
        'T3': round(np.random.normal(120, 20), 2),
        'T4': round(np.random.normal(8, 2), 2),
        'Vitamin B12': round(np.random.normal(500, 100), 2),
        'Vitamin D': round(np.random.normal(30, 10), 2),
        'D-Dimer': round(np.random.normal(0.5, 0.2), 2),
        'PT/INR': round(np.random.normal(1, 0.1), 2),
        'aPTT': round(np.random.normal(30, 5), 2),
        'Homocysteine': round(np.random.normal(10, 3), 2)
    })

pd.DataFrame(records).to_csv('laboratory.csv', index=False)
print('laboratory.csv generated successfully')
```

## 10. Medication — medication_generator.py

```
import pandas as pd
import numpy as np

np.random.seed(42)
num_records = 10000

medications = ['Donepezil', 'Levodopa', 'Memantine', 'Valproate']
side_effects = ['Nausea', 'Headache', 'Dizziness', 'None']

records = []

for i in range(num_records):
    records.append({
        'Patient': f'P{i+1:05d}',
        'Medication Name': np.random.choice(medications),
        'Dosage': np.random.choice(['5mg', '10mg', '20mg']),
        'Frequency of Administration': np.random.choice(['Once Daily', 'Twice Daily']),
        'Medication Duration': np.random.randint(1, 365),
        'Medication Adherence': round(np.random.uniform(0, 100), 2),
        'Missed Dose Count': np.random.randint(0, 20),
        'Medication Response Score': round(np.random.uniform(0, 10), 2),
        'Side Effects': np.random.choice(side_effects)
    })

pd.DataFrame(records).to_csv('medication.csv', index=False)
print('medication.csv generated successfully')
```

## 11. Lifestyle — lifestyle_generator.py

```
import pandas as pd
import numpy as np

np.random.seed(42)
num_records = 10000

records = []

for i in range(num_records):
    records.append({
        'Patient': f'P{i+1:05d}',
        'Smoking Status': np.random.choice(['Never', 'Former', 'Current']),
        'Physical Activity': np.random.choice(['Low', 'Moderate', 'High']),
        'Smoking Duration': np.random.randint(0, 40),
        'Alcohol Consumption': np.random.choice(['Low', 'Moderate', 'High']),
        'Alcohol Frequency': np.random.randint(0, 7),
        'Exercise Frequency': np.random.randint(0, 7),
        'Sleep Duration': round(np.random.normal(7, 1.5), 1),
        'Screen Time': round(np.random.uniform(1, 12), 1)
    })

pd.DataFrame(records).to_csv('lifestyle.csv', index=False)
print('lifestyle.csv generated successfully')
```

## Required Installation

`pip install pandas numpy faker`

## Suggested Folder Structure

```
synthetic_data_project/
│
├── demographics_generator.py
├── longitudinal_generator.py
├── vitals_generator.py
├── neurological_score_generator.py
├── mri_feature_generator.py
├── symptoms_generator.py
├── eeg_generator.py
├── biomarker_generator.py
├── laboratory_generator.py
├── medication_generator.py
├── lifestyle_generator.py
│
└── generated_data/
```


