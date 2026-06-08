## What is Agent-Based Simulation Modeling (ABM)?

Agent-Based Simulation Modeling (ABM) is a computational technique that simulates the actions and interactions of autonomous entities (agents) within a system. By defining individual behavioral rules rather than top-down equations, ABM allows complex, macro-level patterns to emerge naturally from the bottom up. 


With agent-based modeling, active entities, known as agents, must be identified and their behavior defined. They may be people, households, vehicles, equipment, products, or companies, whatever is relevant to the system. Connections between them are established, environmental variables set, and simulations run. The global dynamics of the system then emerge from the interactions of the many individual behaviors.

Individual “agents” interact with each other and the environment according to rules.

Instead of simulating: `One system` , ABM simulates: `Many independent entities behaving together`

**Simple Definition**

`ABM = Simulation of many autonomous agents whose interactions create complex system behavior.`


Agent-Based Modeling (ABM) is a simulation technique where:

- Individual entities `(agents)` act independently
- Each agent follows rules
- Agents interact with:
    - other agents
    - environment
    - time
- Complex system behavior emerges automatically

## Generic Mathematical Representation

ABM is often represented as:

$$
S_i(t+1) = f\big(S_i(t), E(t), I_i(t), R_i(t)\big)
$$

Where:

| Symbol        | Meaning                        |
|----------------|--------------------------------|
| \( S_i(t) \)   | Current state of agent \( i \) |
| \( S_i(t+1) \) | Next state                     |
| \( E(t) \)     | Environment                    |
| \( I_i(t) \)   | Interactions with other agents |
| \( R_i(t) \)   | Rules/behavior                 |
| \( f() \)      | Update function                |

**Meaning in Simple Words**

An agent’s next state depends on:

- its current state
- environment
- interactions
- rules

**Simple Healthcare Example**

Suppose:

- Patient agent
- Doctor agent
- Medication agent

**Patient State**

```
Cognition = 26
Tau = 95
Sleep = 5
```

**Rule Example**

```
If sleep < 5:
    cognition declines faster
```

**Interaction Example**

Doctor gives medication:

`Tau decreases`

## ABM State Update Formula Example

Suppose cognition changes over time:

$$
\text{Cognition}(t+1) =
\text{Cognition}(t)
-
\text{DiseaseProgression}
+
\text{TreatmentEffect}
$$

**Example Numbers**

Current cognition: `26`
Disease progression: `2`
Treatment effect: `+1`
Next cognition: `26−2+1=25`

## Another ABM Formula Example

Tau progression:

$$
\text{Tau}(t+1) =
\text{Tau}(t)
+
\text{StressEffect}
-
\text{SleepEffect}
-
\text{DrugEffect}
$$

**Meaning**

Tau changes due to:

- `stress`
- `sleep`
- `medication`

**In ABM Most Logic Is Rule-Based**

```
if sleep < 5:
    tau += 3
```

```
if medication == True:
    tau -= 5
```


**An ABM is built on three fundamental components:**

- **Agents:** Individual, autonomous decision-makers (e.g., consumers, vehicles, employees, or cells) programmed with specific attributes, memories, and behavioral rules.

- **Environment:** The virtual space or constraints the agents operate within (e.g., a city grid, a physical factory, or a market economy).

- **Topology:** The network mapping how agents interact with one another and the environment. 


## What is an Agent?

**An agent can be:**

- `person`
- `patient`
- `doctor`
- `neuron`
- `robot`
- `vehicle`
- `AI model`
- `hospital`
- `cell`

**Each agent has:**

- `state`
- `behavior`
- `decisions`
- `goals`
- `interactions`


## Simple Real-Life Example

Suppose we simulate a hospital.

**Agents:**

- `Patients`
- `Doctors`
- `Nurses`

Each behaves independently.

**Example Behavior**

**Patient Agent**

Rules: `If fever high → go to hospital`

**Doctor Agent**

Rules: `If patient critical → prioritize treatment`

**Nurse Agent**

Rules: `Monitor patient every 2 hours`


## ABM Core Idea

Complex system behavior emerges from: `Simple interactions between agents`

## Difference Between Monte Carlo vs ABM

| Monte Carlo                       | ABM                                    |
| --------------------------------- | -------------------------------------- |
| Random simulations                | Intelligent interacting agents         |
| Focus on uncertainty              | Focus on behaviors/interactions        |
| Thousands of random futures       | Thousands of interacting entities      |
| Statistical outcomes              | Emergent system behavior               |
| Example: disease risk probability | Example: hospital ecosystem simulation |


## How ABM Works

**STEP 1 — Create Agents**

Example:

- 100 patients
- 20 doctors
- 10 nurses

Each becomes an object.

**STEP 2 — Define Agent Properties**

Patient:

| Property | Example     |
| -------- | ----------- |
| Age      | 65          |
| Disease  | Alzheimer’s |
| Sleep    | 5 hours     |
| Tau      | 95          |


**STEP 3 — Define Behavior Rules**

Example:

```
If cognition declines:
    Increase hospital visits
```

```
If medication taken:
    Reduce disease progression
```

**STEP 4 — Agents Interact**

Example:

- patient visits doctor
- doctor prescribes medicine
- medicine changes biomarker
- cognition improves

**STEP 5 — Run Simulation Over Time**

ABM simulates:

```
Day by day
Month by month
Year by year
```

**STEP 6 — Study Emergent Behavior**

We observe:

- hospital overload
- disease spread
- treatment outcomes
- population-level effects


## Neuro Digital Twin Example

**Agents**

| Agent       | Role                |
| ----------- | ------------------- |
| Patient     | Disease progression |
| Neuron      | Brain activity      |
| Doctor      | Clinical decisions  |
| MRI Scanner | Diagnostic updates  |
| Drug Agent  | Treatment effect    |


**Patient Agent Rules**

Example:

```
If tau > 100:
    cognition declines faster
```

**Drug Agent Rules**

```
If medication active:
    reduce tau growth
```

**Doctor Agent Rules**

```
If MRI worsens:
    change treatment
```

**Simulation Timeline**

```
Month 1
↓
Month 2
↓
Month 3
...
```

Agents continuously interact.

**Emergent Behavior**

ABM may discover:

```
Patients with poor sleep
+
high stress
+
late diagnosis
=
rapid decline
```

Even if not explicitly programmed.

This is called: `Emergent behavior`


### `How do ABM + Monte Carlo + LSTM + Bayesian + Digital Twin work together as one system?`

The answer is: `Each technique solves one part of the problem.`
Together they create: `A living virtual brain simulation system`


```
Real Patient
    ↓
Digital Twin Created
    ↓
AI learns disease progression
    ↓
Monte Carlo simulates uncertainty
    ↓
ABM simulates interactions
    ↓
Bayesian updates probabilities
    ↓
Future brain trajectories generated
```

## USING SINGLE VALUE

```
# ============================================================
# AGENT-BASED MODEL (ABM)
# NEURO DIGITAL TWIN SIMULATION
# ============================================================
#
# PURPOSE
# -------
# This simulation models:
#
# - Patient brain health progression
# - Biomarker evolution
# - Sleep and stress interaction
# - Medication effects
# - Doctor treatment decisions
#
# USING:
# Agent-Based Modeling (ABM)
#
# ============================================================


# ============================================================
# IMPORT LIBRARIES
# ============================================================

# Random library is used for:
# - random disease progression
# - random stress generation
# - random sleep variation
import random


# NumPy is used for:
# - mathematical calculations
# - statistics
import numpy as np


# Pandas is used for:
# - storing simulation results
# - tabular analysis
import pandas as pd


# Matplotlib used for visualization
import matplotlib.pyplot as plt


# ============================================================
# PATIENT AGENT
# ============================================================
#
# This class represents a virtual patient.
#
# Each patient has:
# - cognition
# - tau biomarker
# - sleep
# - stress
# - medication status
#
# ============================================================

class PatientAgent:


    # --------------------------------------------------------
    # INITIALIZE PATIENT
    # --------------------------------------------------------
    #
    # __init__ runs automatically when object is created.
    #
    # ========================================================

    def __init__(self, patient_id):


        # Unique patient identifier
        self.patient_id = patient_id


        # ----------------------------------------------------
        # INITIAL HEALTH STATES
        # ----------------------------------------------------

        # Cognitive score
        # Higher is better
        self.cognition = 28


        # Tau biomarker
        # Higher tau = worse neurodegeneration
        self.tau = 80


        # Sleep hours
        self.sleep = 7


        # Stress level
        self.stress = 2


        # Medication status
        # False = no treatment yet
        self.medication = False


        # Disease stage
        self.stage = "Healthy"


        # Store historical values
        self.history = []


    # ========================================================
    # UPDATE SLEEP
    # ========================================================
    #
    # Sleep changes every month randomly.
    #
    # ========================================================

    def update_sleep(self):


        # Random sleep fluctuation
        #
        # uniform(a, b)
        #
        # Random number between:
        # -1 and +1
        #
        sleep_change = random.uniform(-1, 1)


        # Update sleep
        self.sleep += sleep_change


        # Restrict sleep range
        #
        # max(3, ...)
        # ensures sleep never below 3
        #
        # min(..., 9)
        # ensures sleep never above 9
        #
        self.sleep = max(3, min(self.sleep, 9))


    # ========================================================
    # UPDATE STRESS
    # ========================================================
    #
    # Poor sleep increases stress.
    #
    # ========================================================

    def update_stress(self):


        # If sleep poor
        if self.sleep < 5:


            # Increase stress
            self.stress += 1


        else:

            # Better sleep reduces stress
            self.stress -= 0.5


        # Restrict stress range
        self.stress = max(0, min(self.stress, 10))


    # ========================================================
    # UPDATE TAU BIOMARKER
    # ========================================================
    #
    # Tau affected by:
    # - stress
    # - sleep
    # - medication
    #
    # ========================================================

    def update_tau(self):


        # Base disease progression
        tau_change = 1


        # ----------------------------------------------------
        # STRESS EFFECT
        # ----------------------------------------------------

        # Higher stress increases tau
        tau_change += self.stress * 0.5


        # ----------------------------------------------------
        # SLEEP EFFECT
        # ----------------------------------------------------

        # Poor sleep worsens tau
        if self.sleep < 5:

            tau_change += 2


        # ----------------------------------------------------
        # MEDICATION EFFECT
        # ----------------------------------------------------

        # Medication slows tau growth
        if self.medication:

            tau_change -= 3


        # Update tau biomarker
        self.tau += tau_change


        # Prevent negative tau
        self.tau = max(0, self.tau)


    # ========================================================
    # UPDATE COGNITION
    # ========================================================
    #
    # Cognition worsens as tau increases.
    #
    # ========================================================

    def update_cognition(self):


        # Cognition decline proportional to tau
        cognition_decline = self.tau * 0.01


        # Medication slows decline
        if self.medication:

            cognition_decline *= 0.7


        # Update cognition
        self.cognition -= cognition_decline


        # Prevent negative cognition
        self.cognition = max(0, self.cognition)


    # ========================================================
    # UPDATE DISEASE STAGE
    # ========================================================
    #
    # Convert cognition into disease stage.
    #
    # ========================================================

    def update_stage(self):


        # Healthy stage
        if self.cognition >= 26:

            self.stage = "Healthy"


        # Mild Cognitive Impairment
        elif self.cognition >= 20:

            self.stage = "MCI"


        # Alzheimer's stage
        else:

            self.stage = "Alzheimer"


    # ========================================================
    # DOCTOR INTERACTION
    # ========================================================
    #
    # Doctor decides medication.
    #
    # ========================================================

    def doctor_visit(self):


        # If tau high
        if self.tau > 100:


            # Doctor starts medication
            self.medication = True


    # ========================================================
    # STORE HISTORY
    # ========================================================

    def save_history(self, month):


        # Append current state
        self.history.append({

            "Month": month,

            "PatientID": self.patient_id,

            "Cognition": self.cognition,

            "Tau": self.tau,

            "Sleep": self.sleep,

            "Stress": self.stress,

            "Medication": self.medication,

            "Stage": self.stage
        })


    # ========================================================
    # MAIN MONTHLY UPDATE
    # ========================================================
    #
    # One full simulation cycle.
    #
    # ========================================================

    def step(self, month):


        # Update sleep behavior
        self.update_sleep()


        # Update stress
        self.update_stress()


        # Doctor interaction
        self.doctor_visit()


        # Update biomarker
        self.update_tau()


        # Update cognition
        self.update_cognition()


        # Update disease stage
        self.update_stage()


        # Save patient history
        self.save_history(month)


# ============================================================
# CREATE MULTIPLE PATIENT AGENTS
# ============================================================

patients = []


# Create 100 virtual patients
for i in range(100):


    # Create patient object
    patient = PatientAgent(patient_id=i)


    # Store patient
    patients.append(patient)


# ============================================================
# RUN SIMULATION
# ============================================================
#
# Simulate 24 months.
#
# ============================================================

TOTAL_MONTHS = 24


# Month loop
for month in range(TOTAL_MONTHS):


    # Update every patient
    for patient in patients:


        # Run one monthly step
        patient.step(month)


# ============================================================
# COLLECT RESULTS
# ============================================================

all_results = []


# Extract history from every patient
for patient in patients:


    # Add all patient history rows
    all_results.extend(patient.history)


# ============================================================
# CREATE DATAFRAME
# ============================================================

results_df = pd.DataFrame(all_results)


# ============================================================
# FINAL STAGE ANALYSIS
# ============================================================

latest_month = results_df["Month"].max()


# Get only latest month records
latest_results = results_df[
    results_df["Month"] == latest_month
]


# Count disease stages
stage_counts = latest_results["Stage"].value_counts()


# ============================================================
# PRINT RESULTS
# ============================================================

print("\n")
print("=" * 60)
print("NEURO DIGITAL TWIN ABM RESULTS")
print("=" * 60)


print("\nFINAL DISEASE STAGES:")

print(stage_counts)


# ============================================================
# AVERAGE STATISTICS
# ============================================================

print("\nAVERAGE VALUES:")

print(
    latest_results[
        [
            "Cognition",
            "Tau",
            "Sleep",
            "Stress"
        ]
    ].mean()
)


# ============================================================
# VISUALIZATION
# ============================================================

plt.figure(figsize=(12, 6))


# Histogram of cognition scores
plt.hist(

    latest_results["Cognition"],

    bins=20
)


# X-axis label
plt.xlabel("Cognition Score")


# Y-axis label
plt.ylabel("Number of Patients")


# Graph title
plt.title(
    "Final Cognition Distribution"
)


# Grid
plt.grid(True)


# Show graph
plt.show()


# ============================================================
# TAU TRAJECTORY VISUALIZATION
# ============================================================

plt.figure(figsize=(12, 6))


# Plot first 5 patients
for patient_id in range(5):


    # Get patient rows
    patient_data = results_df[
        results_df["PatientID"] == patient_id
    ]


    # Plot tau over time
    plt.plot(

        patient_data["Month"],

        patient_data["Tau"],

        label=f"Patient {patient_id}"
    )


# Axis labels
plt.xlabel("Month")

plt.ylabel("Tau Biomarker")


# Title
plt.title(
    "Tau Progression Trajectories"
)


# Legend
plt.legend()


# Grid
plt.grid(True)


# Show graph
plt.show()


# ============================================================
# SAVE RESULTS
# ============================================================

results_df.to_csv(

    "neuro_digital_twin_abm_results.csv",

    index=False
)


print("\nSimulation results saved:")
print("neuro_digital_twin_abm_results.csv")


# ============================================================
# END OF PROGRAM
# ============================================================
```



## USING 2 YEARS HISTORICAL VISIT DATA

```
# ============================================================
# NEURO DIGITAL TWIN
# AGENT-BASED MODEL (ABM)
# USING 2 YEARS HISTORICAL VISIT DATA
# ============================================================
#
# PURPOSE
# -------
# This simulation:
#
# 1. Uses historical patient visit data
# 2. Learns patient disease trends
# 3. Creates personalized patient agents
# 4. Simulates future neuro progression
#
# DATA USED
# ---------
# - Biomarkers
# - MRI features
# - EHR data
# - Sleep
# - Cognition
#
# ============================================================


# ============================================================
# IMPORT LIBRARIES
# ============================================================

# Random number generation
import random


# Numerical computation
import numpy as np


# Dataframe handling
import pandas as pd


# Visualization
import matplotlib.pyplot as plt


# ============================================================
# STEP 1 — CREATE HISTORICAL VISIT DATA
# ============================================================
#
# In real systems:
# This data comes from:
# - EHR systems
# - MRI systems
# - Biomarker labs
#
# Here we manually create example data.
#
# ============================================================

historical_data = pd.DataFrame({

    # --------------------------------------------------------
    # VISIT DATE
    # --------------------------------------------------------

    "VisitDate": [

        "2024-01",
        "2024-04",
        "2024-07",
        "2024-10",
        "2025-01",
        "2025-04",
        "2025-07",
        "2025-10"
    ],


    # --------------------------------------------------------
    # BIOMARKERS
    # --------------------------------------------------------

    # Tau increasing over time
    "Tau": [
        80,
        85,
        90,
        96,
        102,
        108,
        115,
        120
    ],


    # --------------------------------------------------------
    # COGNITIVE SCORE
    # --------------------------------------------------------

    # Cognition decreasing
    "Cognition": [
        28,
        27,
        27,
        26,
        25,
        24,
        23,
        22
    ],


    # --------------------------------------------------------
    # SLEEP HOURS
    # --------------------------------------------------------

    "Sleep": [
        7,
        6.5,
        6,
        5.5,
        5,
        5,
        4.5,
        4
    ],


    # --------------------------------------------------------
    # MRI FEATURE
    # --------------------------------------------------------

    # Hippocampus shrinking
    "HippocampusVolume": [
        3400,
        3360,
        3330,
        3290,
        3250,
        3200,
        3150,
        3100
    ],


    # --------------------------------------------------------
    # STRESS LEVEL
    # --------------------------------------------------------

    "Stress": [
        2,
        3,
        3,
        4,
        5,
        6,
        6,
        7
    ]
})


# ============================================================
# CONVERT DATE COLUMN
# ============================================================

historical_data["VisitDate"] = pd.to_datetime(
    historical_data["VisitDate"]
)


# ============================================================
# SORT BY DATE
# ============================================================

historical_data = historical_data.sort_values(
    "VisitDate"
)


# ============================================================
# STEP 2 — LEARN HISTORICAL TRENDS
# ============================================================
#
# We calculate:
# - Tau trend
# - Cognition trend
# - Sleep trend
# - MRI trend
#
# This makes simulation personalized.
#
# ============================================================


# Create numerical timeline
time_index = np.arange(len(historical_data))


# ------------------------------------------------------------
# TAU TREND
# ------------------------------------------------------------
#
# polyfit() learns line trend:
#
# y = mx + c
#
# slope (m) tells:
# How fast biomarker changes.
#
# ============================================================

tau_trend = np.polyfit(

    # X values
    time_index,

    # Y values
    historical_data["Tau"],

    # Linear fit
    1

)[0]


# ------------------------------------------------------------
# COGNITION TREND
# ------------------------------------------------------------

cognition_trend = np.polyfit(

    time_index,

    historical_data["Cognition"],

    1

)[0]


# ------------------------------------------------------------
# SLEEP TREND
# ------------------------------------------------------------

sleep_trend = np.polyfit(

    time_index,

    historical_data["Sleep"],

    1

)[0]


# ------------------------------------------------------------
# MRI TREND
# ------------------------------------------------------------

mri_trend = np.polyfit(

    time_index,

    historical_data["HippocampusVolume"],

    1

)[0]


# ============================================================
# PRINT LEARNED TRENDS
# ============================================================

print("\n")
print("=" * 60)
print("LEARNED HISTORICAL TRENDS")
print("=" * 60)

print(f"Tau Trend          : {tau_trend:.2f}")

print(f"Cognition Trend    : {cognition_trend:.2f}")

print(f"Sleep Trend        : {sleep_trend:.2f}")

print(f"MRI Trend          : {mri_trend:.2f}")


# ============================================================
# STEP 3 — CREATE DIGITAL TWIN AGENT
# ============================================================

class NeuroDigitalTwin:


    # --------------------------------------------------------
    # INITIALIZE AGENT
    # --------------------------------------------------------

    def __init__(self, patient_history):


        # Store patient history
        self.history_df = patient_history


        # ----------------------------------------------------
        # GET LATEST VISIT
        # ----------------------------------------------------

        latest = patient_history.iloc[-1]


        # ----------------------------------------------------
        # INITIALIZE CURRENT STATE
        # ----------------------------------------------------

        # Latest tau value
        self.tau = latest["Tau"]


        # Latest cognition
        self.cognition = latest["Cognition"]


        # Latest sleep
        self.sleep = latest["Sleep"]


        # Latest MRI volume
        self.hippocampus = latest[
            "HippocampusVolume"
        ]


        # Latest stress
        self.stress = latest["Stress"]


        # Medication status
        self.medication = False


        # ----------------------------------------------------
        # STORE LEARNED TRENDS
        # ----------------------------------------------------

        self.tau_trend = tau_trend

        self.cognition_trend = cognition_trend

        self.sleep_trend = sleep_trend

        self.mri_trend = mri_trend


        # ----------------------------------------------------
        # STORE FUTURE HISTORY
        # ----------------------------------------------------

        self.future_history = []


    # ========================================================
    # DOCTOR INTERACTION
    # ========================================================

    def doctor_visit(self):


        # If tau too high
        if self.tau > 130:


            # Start medication
            self.medication = True


    # ========================================================
    # UPDATE SLEEP
    # ========================================================

    def update_sleep(self):


        # Historical trend effect
        self.sleep += self.sleep_trend


        # Random fluctuation
        self.sleep += random.uniform(-0.3, 0.3)


        # Medication improves sleep slightly
        if self.medication:

            self.sleep += 0.2


        # Restrict realistic range
        self.sleep = max(3, min(self.sleep, 9))


    # ========================================================
    # UPDATE STRESS
    # ========================================================

    def update_stress(self):


        # Poor sleep increases stress
        if self.sleep < 5:

            self.stress += 0.5


        else:

            self.stress -= 0.3


        # Restrict range
        self.stress = max(0, min(self.stress, 10))


    # ========================================================
    # UPDATE TAU
    # ========================================================

    def update_tau(self):


        # Base progression from history
        self.tau += self.tau_trend


        # Stress effect
        self.tau += self.stress * 0.3


        # Poor sleep worsens tau
        if self.sleep < 5:

            self.tau += 1


        # Medication reduces tau
        if self.medication:

            self.tau -= 3


        # Random biological variability
        self.tau += random.uniform(-1, 1)


    # ========================================================
    # UPDATE COGNITION
    # ========================================================

    def update_cognition(self):


        # Historical cognition decline
        self.cognition += self.cognition_trend


        # Tau damages cognition
        self.cognition -= self.tau * 0.005


        # Medication slows decline
        if self.medication:

            self.cognition += 0.5


        # Prevent negative cognition
        self.cognition = max(0, self.cognition)


    # ========================================================
    # UPDATE MRI
    # ========================================================

    def update_mri(self):


        # MRI shrinkage trend
        self.hippocampus += self.mri_trend


        # Tau accelerates shrinkage
        self.hippocampus -= self.tau * 0.2


        # Medication slows shrinkage
        if self.medication:

            self.hippocampus += 5


    # ========================================================
    # DETERMINE DISEASE STAGE
    # ========================================================

    def disease_stage(self):


        if self.cognition >= 26:

            return "Healthy"


        elif self.cognition >= 20:

            return "MCI"


        else:

            return "Alzheimer"


    # ========================================================
    # SAVE CURRENT STATE
    # ========================================================

    def save_state(self, month):


        self.future_history.append({

            "Month": month,

            "Tau": self.tau,

            "Cognition": self.cognition,

            "Sleep": self.sleep,

            "Stress": self.stress,

            "MRI": self.hippocampus,

            "Medication": self.medication,

            "Stage": self.disease_stage()
        })


    # ========================================================
    # MAIN MONTHLY SIMULATION STEP
    # ========================================================

    def step(self, month):


        # Doctor evaluation
        self.doctor_visit()


        # Update sleep
        self.update_sleep()


        # Update stress
        self.update_stress()


        # Update tau
        self.update_tau()


        # Update cognition
        self.update_cognition()


        # Update MRI
        self.update_mri()


        # Save future state
        self.save_state(month)


# ============================================================
# STEP 4 — CREATE DIGITAL TWIN
# ============================================================

twin = NeuroDigitalTwin(historical_data)


# ============================================================
# STEP 5 — RUN FUTURE SIMULATION
# ============================================================

FUTURE_MONTHS = 24


for month in range(FUTURE_MONTHS):


    twin.step(month)


# ============================================================
# STEP 6 — CREATE FUTURE DATAFRAME
# ============================================================

future_df = pd.DataFrame(twin.future_history)


# ============================================================
# STEP 7 — PRINT RESULTS
# ============================================================

print("\n")
print("=" * 60)
print("FINAL FUTURE STATE")
print("=" * 60)

print(future_df.tail())


# ============================================================
# STEP 8 — VISUALIZE TAU TRAJECTORY
# ============================================================

plt.figure(figsize=(12, 6))


plt.plot(

    future_df["Month"],

    future_df["Tau"]
)


plt.xlabel("Future Month")

plt.ylabel("Tau Biomarker")


plt.title(
    "Future Tau Progression"
)

plt.grid(True)

plt.show()


# ============================================================
# STEP 9 — VISUALIZE COGNITION
# ============================================================

plt.figure(figsize=(12, 6))


plt.plot(

    future_df["Month"],

    future_df["Cognition"]
)


plt.xlabel("Future Month")

plt.ylabel("Cognition Score")


plt.title(
    "Future Cognition Decline"
)

plt.grid(True)

plt.show()


# ============================================================
# STEP 10 — VISUALIZE MRI SHRINKAGE
# ============================================================

plt.figure(figsize=(12, 6))


plt.plot(

    future_df["Month"],

    future_df["MRI"]
)


plt.xlabel("Future Month")

plt.ylabel("Hippocampus Volume")


plt.title(
    "Future MRI Brain Atrophy"
)

plt.grid(True)

plt.show()


# ============================================================
# STEP 11 — SAVE RESULTS
# ============================================================

future_df.to_csv(

    "neuro_digital_twin_future_simulation.csv",

    index=False
)


print("\n")
print("Results saved:")
print("neuro_digital_twin_future_simulation.csv")


# ============================================================
# END OF PROGRAM
# ============================================================
```

**OUTPUT**

```
============================================================
LEARNED HISTORICAL TRENDS
============================================================
Tau Trend          : 5.83
Cognition Trend    : -0.86
Sleep Trend        : -0.41
MRI Trend          : -42.62


============================================================
FINAL FUTURE STATE
============================================================
    Month         Tau  Cognition  Sleep  Stress          MRI  Medication  \
19     19  258.373648        0.0    3.0    10.0  1560.797403        True   
20     20  265.654974        0.0    3.0    10.0  1470.047360        True   
21     21  273.174180        0.0    3.0    10.0  1377.793477        True   
22     22  279.273166        0.0    3.0    10.0  1284.319796        True   
23     23  285.826572        0.0    3.0    10.0  1189.535434        True   

        Stage  
19  Alzheimer  
20  Alzheimer  
21  Alzheimer  
22  Alzheimer  
23  Alzheimer  
```



## How does the system use 2 years of historical data to simulate the next 5 years?

The system does:

```
Past Patient History
        ↓
Learn Disease Pattern
        ↓
Estimate Disease Trends
        ↓
Use Those Trends To Simulate Future
```

**STEP 1 — Historical Data (2 Years)**

Suppose patient visited hospital every 3 months.

| Visit | Tau | Cognition | Sleep | MRI  |
| ----- | --- | --------- | ----- | ---- |
| V1    | 80  | 28        | 7     | 3400 |
| V2    | 85  | 27        | 6.5   | 3360 |
| V3    | 90  | 27        | 6     | 3330 |
| V4    | 96  | 26        | 5.5   | 3290 |
| V5    | 102 | 25        | 5     | 3250 |
| V6    | 108 | 24        | 5     | 3200 |
| V7    | 115 | 23        | 4.5   | 3150 |
| V8    | 120 | 22        | 4     | 3100 |


**STEP 2 — Learn Trends**

The system studies: `How values changed over time`

**Example Tau Progression**

`80 → 85 → 90 → 96 → 102 → 108 → 115 → 120`

**System learns:**

`Tau increasing continuously`

**How Trend Is Calculated**

`y=mx+c`

| Symbol | Meaning                    |
| ------ | -------------------------- |
| y      | Output value               |
| x      | Input value                |
| m      | Slope (rate of change)     |
| c      | Intercept (starting value) |


Where:

- `m = slope (trend speed)`
- `c = intercept`

**Simple Real-Life Example**

Suppose:

- You save ₹100 every day
- Initially you already have ₹500

Then:

| Variable | Meaning        |
| -------- | -------------- |
| x        | Number of days |
| y        | Total money    |
| m        | 100/day        |
| c        | 500            |


Equation: `y = 100x + 500`

**Calculate Values**

- **Day 1:** `y=100(1)+500 = 600`
- **Day 2:** `y=100(2)+500 = 700`
- **Day 3:** `y=100(3)+500 = 800`
- **Day 4:** `y=100(4)+500 = 900`
- **Day 5:** `y=100(5)+500 = 1000`

**What is Slope (m)?**

**Slope means:** `How fast y changes when x changes`

`When x increases by 1, y increases by 100.`

So slope: `m = 100`

**What is Intercept (c)?**

Intercept means: `Starting value when x = 0`

When `x = 0:`

`y=100(0)+500 = 600`

`So line starts at 600.`


**Positive Slope:** `y = 100x + 1`
Line goes upward.

**Negative Slope:** `y = -100x + 1`
Line goes downward.

**Example**

Suppose:

| Time | Tau |
| ---- | --- |
| 0    | 80  |
| 1    | 85  |
| 2    | 90  |
| 3    | 96  |


polyfit learns: `TauTrend≈+5.7`

Meaning: `Tau increases ~5.7 units per visit period`


**Same for Cognition**

History: `28 → 27 → 27 → 26 → 25 → 24`

Trend: `CognitionTrend≈−0.8`

Meaning: `Cognition drops ~0.8 points each step`

**STEP 3 — Create Current Digital Twin State**

Latest visit becomes: `Starting point for future simulation`

Latest values:

| Variable  | Latest |
| --------- | ------ |
| Tau       | 120    |
| Cognition | 22     |
| Sleep     | 4      |
| MRI       | 3100   |

**STEP 4 — Future Simulation Starts**

Now system simulates: `Month 1 → Month 2 → Month 3 ...`

**Example Tau Update**

`self.tau += self.tau_trend`

Suppose:

- `Current tau = 120`
- `Trend = +5.7`

Next month:

- `120+5.7=125.7`

**But Real Life Is Uncertain**

So simulation also adds:

- `stress effect`
- `sleep effect`
- `medication effect`
- `random variability`

**Full Tau Equation**

Used in code:

$$
\text{Tau}_{next}
=
\text{Tau}_{current}
+
\text{Trend}
+
\text{StressEffect}
+
\text{SleepEffect}
-
\text{MedicationEffect}
+
\text{RandomNoise}
$$

**Example Calculation**

- Current tau: `120`
- Trend: `+5.7`
- Stress effect:: `+2`
- Poor sleep: `+1`
- Medication: `-3`
- Random noise: `+0.5`
- Next tau: `120+5.7+2+1−3+0.5 = 126.2`


**STEP 5 — Cognition Updated**

Equation:

$$
\text{Cognition}_{next}
=
\text{Cognition}_{current}
+
\text{Trend}
-
\text{TauDamage}
+
\text{MedicationBenefit}
$$


Example:

- Current cognition: `22`
- Historical decline: `-0.8`
- Tau damage: `-0.6`
- Medication: `+0.3`
- Next cognition: `22−0.8−0.6+0.3 = 20.9`

**STEP 6 — Repeat for 5 Years**

If monthly simulation: `5 years=60 months`

Loop runs: `for month in range(60):`

Each month:

- update biomarkers
- update cognition
- update MRI
- apply interactions
- save future state

**STEP 7 — Disease Evolution Emerges**

Over time:

```
Tau ↑
MRI ↓
Sleep ↓
Stress ↑
Cognition ↓
```

Simulation creates: `Future disease trajectory`

**STEP 8 — Final Output**

After 5 years:

| Month | Tau | Cognition | Stage       |
| ----- | --- | --------- | ----------- |
| 0     | 120 | 22        | MCI         |
| 12    | 150 | 18        | Alzheimer's |
| 24    | 180 | 14        | Severe      |
| 36    | 210 | 10        | Severe      |
| 60    | 250 | 5         | Severe      |


**Important Insight**

The simulation does NOT simply: `Copy past values`

It:

1. Learns historical trends
2. Uses interaction rules
3. Applies biological dynamics
4. Adds uncertainty
5. Evolves system month-by-month


This Is Why It Is Called `Dynamic Longitudinal Simulation`

## Real Neuro Digital Twin Systems Add Even More

Advanced systems additionally use:

| Technique   | Purpose                        |
| ----------- | ------------------------------ |
| LSTM        | Learn nonlinear progression    |
| Transformer | Multimodal temporal learning   |
| Bayesian    | Probability updates            |
| Monte Carlo | Thousands of uncertain futures |
| HMM         | Disease state transitions      |
| ABM         | Interaction modeling           |















