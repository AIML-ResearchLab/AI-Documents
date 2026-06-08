## What is Hidden Markov Model (HMM)?

A Hidden Markov Model (HMM) is a probabilistic model used when:

`The real system state is hidden, but we can observe indirect signals.`

**Simple Idea**

In healthcare:

We cannot directly see: `True brain degeneration state`

But we can observe:

- MRI scans
- Tau biomarkers
- Cognitive scores
- Symptoms

**HMM tries to infer:** `What hidden disease state most likely caused these observations`

**Why “Hidden”?**

Because: `Actual disease stage is not directly observable`

Example:

- neurons dying internally
- hidden neurodegeneration
- hidden inflammation

Doctors only observe indirect evidence.

**Real-Life Analogy**

Suppose weather is hidden inside a closed room.You cannot directly see weather.

But you observe:

- umbrella
- wet clothes
- dark clouds

**You infer:** `Probably raining`

**Similarly:** 

- MRI shrinkage
- high tau
- cognition decline

suggest: `Possible Alzheimer’s progression`

## Core Components of HMM

HMM has 5 important parts.

**1. Hidden States**

Actual disease conditions.

Example:

```
Healthy
↓
Mild Cognitive Impairment (MCI)
↓
Alzheimer’s
```

These are hidden.

**2. Observations**

What we can measure.

Example:

| Observation     | Example |
| --------------- | ------- |
| Tau biomarker   | 120     |
| MRI shrinkage   | Severe  |
| Cognition score | 22      |


**3. Transition Probabilities**

Probability of moving between hidden states.

Example:

| Current State | Next State  | Probability |
| ------------- | ----------- | ----------- |
| Healthy       | Healthy     | 0.85        |
| Healthy       | MCI         | 0.15        |
| MCI           | Alzheimer’s | 0.40        |

**Meaning**

If patient currently in: `MCI`

Then: `40% chance progresses to Alzheimer’s`

**4. Emission Probabilities**

Probability of observing data given a hidden state.

Example:

| Hidden State | Observation Probability |
| ------------ | ----------------------- |
| Healthy      | Low tau likely          |
| Alzheimer’s  | High tau likely         |


Example:

If hidden state: `Alzheimer’s`

then:

- `Tau = 120 is highly probable`
- `MRI shrinkage probable`

**5. Initial Probabilities**

Starting probabilities.

Example:

| State       | Probability |
| ----------- | ----------- |
| Healthy     | 70%         |
| MCI         | 20%         |
| Alzheimer’s | 10%         |


**Full HMM Flow**

```
Hidden State
     ↓
Generates
     ↓
Observed Measurements
```

## Example Neuro Digital Twin

**Hidden States**

```
Healthy
MCI
Alzheimer’s
```

**Observations**

| Tau | MRI       | Cognition |
| --- | --------- | --------- |
| 80  | Normal    | 28        |
| 110 | Shrinking | 22        |
| 140 | Severe    | 15        |


**STEP-BY-STEP EXAMPLE**

**STEP 1 — Define Hidden States**

```
states = [
    "Healthy",
    "MCI",
    "Alzheimer"
]
```

**STEP 2 — Define Observations**

Observed tau categories:

```
observations = [
    "LowTau",
    "MediumTau",
    "HighTau"
]
```

**STEP 3 — Define Transition Matrix**

This controls disease progression.

$$
P =
\begin{bmatrix}
0.8 & 0.2 & 0 \\
0 & 0.7 & 0.3 \\
0 & 0 & 1
\end{bmatrix}
$$


Meaning:

- Healthy → Healthy = 80%
- Healthy → MCI = 20%
- MCI → Alzheimer’s = 30%

**STEP 4 — Define Emission Probabilities**

Probability of observations from states.

**Example**

| State     | LowTau | MediumTau | HighTau |
| --------- | ------ | --------- | ------- |
| Healthy   | 0.8    | 0.2       | 0.0     |
| MCI       | 0.2    | 0.6       | 0.2     |
| Alzheimer | 0.0    | 0.3       | 0.7     |


**Meaning**

If patient hidden state: `Alzheimer’s`

Then: `High tau likely (70%)`

**STEP 5 — Observe Patient Data**

Suppose observed: `HighTau`
Question: `What hidden state most likely caused this?`

HMM computes probabilities.

**STEP 6 — Probabilistic Inference**

Using:

- transition probabilities
- emission probabilities
- previous states


HMM estimates:

| Hidden State | Probability |
| ------------ | ----------- |
| Healthy      | 5%          |
| MCI          | 30%         |
| Alzheimer    | 65%         |


**Final Prediction**

`Patient most likely in Alzheimer’s hidden state`

**HMM Mathematics**

HMM computes: `P(HiddenState∣Observations)`

Meaning: `Probability of hidden state given observed data`

**Key Algorithms in HMM**

**1. Forward Algorithm**

Calculates: `Probability of observation sequence`

**2. Viterbi Algorithm**

Finds: `Most likely hidden state sequence`

**Example**

Observed: `LowTau → MediumTau → HighTau`

Viterbi may predict: `Healthy → MCI → Alzheimer’s`

**3. Baum-Welch Algorithm**

Learns:

- transition probabilities
- emission probabilities

from data automatically.

**Why HMM Is Powerful in Healthcare**

Because: `Disease biology is mostly hidden`

We only observe:

- symptoms
- biomarkers
- scans


**In Neuro Digital Twin**

HMM can infer:

- hidden neurodegeneration stage
- hidden disease severity
- hidden treatment response state


## HMM vs Markov

| Markov               | HMM                          |
| -------------------- | ---------------------------- |
| State visible        | State hidden                 |
| Direct observation   | Indirect observation         |
| Simpler              | More realistic               |
| Example: known stage | Example: hidden degeneration |


## HMM + Monte Carlo

HMM predicts: `Current hidden disease state`
Monte Carlo simulates: `Thousands of future trajectories`


## HMM + LSTM

LSTM predicts: `Future biomarker values`
HMM predicts: `Disease stages`

Together: `Continuous + discrete disease modeling`

## Simple Python Example

```
import numpy as np

# Hidden states
states = ["Healthy", "MCI", "Alzheimer"]

# Observations
observations = ["LowTau", "MediumTau", "HighTau"]

# Transition matrix
transition = np.array([
    [0.8, 0.2, 0.0],
    [0.0, 0.7, 0.3],
    [0.0, 0.0, 1.0]
])

# Emission matrix
emission = np.array([
    [0.8, 0.2, 0.0],
    [0.2, 0.6, 0.2],
    [0.0, 0.3, 0.7]
])

# Initial probabilities
initial = np.array([0.7, 0.2, 0.1])

# Observed patient sequence
observed = [0, 1, 2]

# Simple probability calculation
prob = initial

for obs in observed:

    prob = np.dot(prob, transition)

    prob = prob * emission[:, obs]

    prob = prob / np.sum(prob)

    print(prob)
```

**What This Does**

It continuously updates: `Probability of hidden disease states`

based on observations.


```
MRI + Biomarkers + EHR
            ↓
           HMM
    (infer hidden stage)
            ↓
     Monte Carlo
(simulate uncertain futures)
            ↓
Probability of future trajectories
```


