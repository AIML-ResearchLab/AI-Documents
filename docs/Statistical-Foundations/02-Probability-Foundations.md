# 02 - Probability Foundations

## 2.1 Probability Axioms
1. `P(A) >= 0`
2. `P(S) = 1`
3. For disjoint events, `P(A U B) = P(A) + P(B)`

## 2.2 Event Operations
- Union `A U B`
- Intersection `A ∩ B`
- Complement `A^c`

## 2.3 Conditional Probability
`P(A|B) = P(A ∩ B) / P(B)` for `P(B) > 0`.

## 2.4 Independence
A and B are independent if `P(A ∩ B) = P(A)P(B)`.

## 2.5 Bayes Theorem
`P(A|B) = P(B|A)P(A) / P(B)`

Used in AI for belief updates as new evidence arrives.

## 2.6 Total Probability
`P(B) = sum_i P(B|A_i)P(A_i)` over partition `{A_i}`.

## 2.7 Real-Time Example
Fraud detection:
- Prior fraud rate low
- Alert model has false positives
- Bayes update is required to interpret alert probability correctly

## 2.8 Common Mistakes
- Confusing `P(A|B)` with `P(B|A)`
- Ignoring base rates
- Assuming correlation implies causal dependence

