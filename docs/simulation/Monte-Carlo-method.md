## What is Monte Carlo simulation?

A **Monte Carlo simulation** is a `mathematical technique used to estimate the possible outcomes of an uncertain event`. By running thousands or millions of randomized trials, it replaces single-point forecasts with a probability distribution, giving you a clear picture of what might happen and how likely it is.

## How it Works?

**STEP 1 — Assign Ranges (Probability Distribution)**

Instead of `Project Time = 30 days` We define uncertainty:

| Scenario | Probability       |
| -------- | ----------------- |
| 20 days  | Possible          |
| 30 days  | Most likely       |
| 50 days  | Rare but possible |

This becomes a probability distribution.

**Example Using Normal Distribution**

Most values occur near the center.

$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

Where:

- μ = average (mean)

- σ = spread (standard deviation)

Example:

- μ = Average = 30 days

- σ = Typical variation = ±5 days

```
import numpy as np
days = np.random.normal(30, 5, size=10)
for day in days:
  print(round(day))
```

**Generated values:**

```
30
28
31
28
27
37
33
30
38
29
```

- 30 occurs often

- Extreme values are rare

## STEP 2 — Random Sampling

Computer randomly picks values.

**Example:**

| Simulation | Duration |
| ---------- | -------- |
| 1          | 28 days  |
| 2          | 35 days  |
| 3          | 31 days  |
| 4          | 42 days  |

Each row is one possible future.

This is called: `Random Sampling`

## STEP 3 — Repetition

One simulation is not enough.

Monte Carlo repeats:

```
1000 times
10000 times
100000 times
```

Why?

Because more simulations:

- Reduce randomness error

- Improve accuracy

- Reveal hidden risks


## STEP 4 — Massive Dataset Creation

After thousands of runs:

| Simulation | Days |
| ---------- | ---- |
| 1          | 28   |
| 2          | 35   |
| 3          | 31   |
| ...        | ...  |
| 10000      | 33   |


Now we have: `A distribution of possible outcomes`

## STEP 5 — Analysis

Now we ask:

**Average duration?**

Maybe: `31.2 days`

**Best case?**

Maybe: `20 days`

**Worst case?**

Maybe: `49 days`

**Probability project finishes within 35 days?**

Maybe: `82%`

**Visual Understanding**

Instead of: `ONE prediction` Monte Carlo creates: `THOUSANDS of predictions` Then studies the pattern.


### `After generating thousands of predictions, how does the system actually understand the pattern and calculate probabilities?`

## Step 1 — Generate Thousands of Outcomes

Suppose we simulate Alzheimer’s progression risk `10,000` times.
Each simulation produces one result.
Example:

| Simulation | Risk Score |
| ---------- | ---------- |
| 1          | 72         |
| 2          | 65         |
| 3          | 81         |
| 4          | 90         |
| 5          | 58         |

After `10,000 runs`: `[72, 65, 81, 90, 58, 77, 69, 84, ...]`. Now we have a huge dataset.


## Step 2 — Build Distribution of Results

Monte Carlo studies:

- How frequently values occur

- Which outcomes are common

- Which are rare

Example:

| Risk Range | Count |
| ---------- | ----- |
| 0–40       | 500   |
| 40–70      | 3000  |
| 70–100     | 6500  |

This forms a probability distribution.

**Visual Idea**
Imagine a histogram:

```
Low Risk        ███
Medium Risk     ███████████
High Risk       ███████████████████
```

Most simulations landed in High Risk. So: `High risk is more probable`

## Step 3 — Convert Frequency into Probability

Probability is calculated using:

$$
Probability = \frac{\text{Number of Desired Outcomes}}{\text{Total Simulations}}
$$

Example:

Suppose:

- Total simulations = 10,000

- High-risk outcomes = 6,500

Then:

$$
P(\text{High Risk}) = \frac{6500}{10000} = 0.65
$$

So: `Probability of High Risk = 65%`

**How Pattern Is Studied**

Monte Carlo studies patterns using statistics.

**1. Mean (Average)**
$$
\text{Mean} = \frac{\sum x_i}{N}
$$

Let’s understand `Mean (Average)` in Monte Carlo with a real example.

**Suppose We Run 5 Simulations**

We simulate disease risk 5 times.

Results:

| Simulation | Risk Score |
| ---------- | ---------- |
| 1          | 60         |
| 2          | 70         |
| 3          | 80         |
| 4          | 90         |
| 5          | 70         |


These values came from random sampling.

**What Is Mean?**

Mean simply means: `What is the average of all simulation results?`

Where:

- \( x_i \) = each simulation result
- \( N \) = total number of simulations

**Step-by-Step Calculation**

**Step 1 — Add all results:** 

`60+70+80+90+70 = 370`

**Step 2 — Divide by total simulations**

Total simulations:

`N = 5`

So:

$$
\text{Mean} = \frac{370}{5} = 74
$$

**Final Meaning** `Average disease risk = 74`

This means:

If we simulate many possible futures, the expected average risk is around 74.

**Real Interpretation**

Monte Carlo produced:

```
60
70
80
90
70
```

Some futures were:

- lower risk
- higher risk

But overall:

`Typical expected risk ≈ 74`

**Why Mean Is Important**

Mean gives: `The center of all possible outcomes`

It helps answer:

- Expected project duration
- Expected disease risk
- Expected stock return
- Expected future value

**In Neuro Digital Twin**

Suppose 10,000 simulations predict brain decline scores.

Some patients:

- decline slowly
- decline rapidly
- remain stable

Mean tells: `Average expected progression level`


## 2. Variance

Measures spread of results.

- Small variance: `Predictions are stable`
- Large variance: `Future is highly uncertain`

**What is Variance?**

Variance tells us: `How far the simulation results are spread from the average (mean).`

**Simple Intuition**

Suppose two doctors predict disease risk.

**Case 1 — Stable Predictions**

Results:

| Simulation | Risk |
| ---------- | ---- |
| 1          | 73   |
| 2          | 74   |
| 3          | 75   |
| 4          | 74   |
| 5          | 74   |


Mean: `74`

Notice: 

- `All values are close to 74` 
- `Very little variation`

This means: `Future predictions are stable`

So: `Variance is SMALL`

**Case 2 — Unstable Predictions**

Results:

| Simulation | Risk |
| ---------- | ---- |
| 1          | 20   |
| 2          | 95   |
| 3          | 40   |
| 4          | 85   |
| 5          | 130  |


Mean may still be around: `74`

BUT:

- Values are wildly different
- Some very low
- Some very high

This means: `Future is uncertain`
So: `Variance is LARGE`

**Key Insight**

Both cases may have: `Same mean = 74`

But:

- Case 1 = predictable future
- Case 2 = unpredictable future

Variance measures this uncertainty.


**Mathematical Meaning**

Variance calculates: `Average squared distance from the mean.`

Formula:

$$
\text{Variance} = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2
$$

Where:

- \( x_i \) = each value
- \( \mu \) = mean
- \( N \) = total simulations

**Let’s Calculate Step-by-Step**

**Example: Small Variance**

Values: `73, 74, 75`

Mean: `74`

**Step 1 — Distance from mean**

| Value | Distance from 74 |
| ----- | ---------------- |
| 73    | -1               |
| 74    | 0                |
| 75    | +1               |


**Step 2 — Square distances**

| Distance | Squared |
| -------- | ------- |
| -1       | 1       |
| 0        | 0       |
| 1        | 1       |


**Step 3 — Average**

$$
\text{Variance} = \frac{1 + 0 + 1}{3} = 0.67
$$

Small variance.

**Example: Large Variance**

Values: `20, 74, 128`
Mean: `74`

**Distances**

| Value | Distance |
| ----- | -------- |
| 20    | -54      |
| 74    | 0        |
| 128   | +54      |


**Squared**

| Distance | Squared |
| -------- | ------- |
| -54      | 2916    |
| 0        | 0       |
| +54      | 2916    |


**Average**

$$
\text{Variance} = \frac{2916 + 0 + 2916}{3} = 1944
$$

**Real Meaning in Monte Carlo**

Variance tells: `How uncertain future outcomes are`


## 3. Standard Deviation

Measures uncertainty level.

$$
\sigma = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2}
$$

Higher standard deviation means: `More unpredictability`


## 4. Confidence Interval

Example:

`95% probability risk lies between 70–85`

This is more useful than a single prediction.

**Step 4 — Classification into Categories**

Sometimes outputs are converted into labels.

Example:

| Risk Score | Category |
| ---------- | -------- |
| 0–40       | Low      |
| 40–70      | Moderate |
| 70–100     | High     |


Now Monte Carlo counts category frequency.

Example:

After 10,000 simulations:

| Category | Count |
| -------- | ----- |
| Low      | 800   |
| Moderate | 2700  |
| High     | 6500  |


Probabilities:

| Category | Probability |
| -------- | ----------- |
| Low      | 8%          |
| Moderate | 27%         |
| High     | 65%         |


## Step 5 — Final Output Generation

Monte Carlo produces outputs like:

```
Average Risk: 74
High Risk Probability: 65%
Worst Case Risk: 96
Best Case Risk: 32
95% Confidence Interval: 68–85
```

