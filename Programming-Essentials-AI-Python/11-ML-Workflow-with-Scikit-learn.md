# 11 - ML Workflow with Scikit-learn

## 11.1 End-to-End Workflow
1. Define objective and metric
2. Load and clean data
3. Split train/validation/test
4. Build preprocessing + model pipeline
5. Evaluate and tune
6. Save model and inference contract

## 11.2 Train/Validation/Test Split
Use stratification for imbalanced classes when needed.

## 11.3 Pipelines
Pipelines reduce leakage and make training/inference consistent.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([
    ("scale", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000))
])
```

## 11.4 Cross-Validation
Use k-fold CV for robust estimates before deployment.

## 11.5 Hyperparameter Tuning
- Grid search
- Random search
- Bayesian optimization (advanced)

## 11.6 Model Evaluation
- Confusion matrix
- ROC curve
- Precision-recall curve
- Error analysis by segment

## 11.7 Model Persistence
Use `joblib` to save model and preprocessing pipeline together.

