# 01 - Program Overview and Environment Setup

## 1.1 Goal
Build strong Python programming fundamentals required to design, train, evaluate, and deploy AI systems.

## 1.2 Learning Path
1. Python fundamentals
2. Data handling and numerical computing
3. Machine learning workflows
4. Deep learning basics
5. Production and MLOps essentials

## 1.3 Recommended Setup
- Python 3.11+
- VS Code or PyCharm
- Git and GitHub
- Jupyter Notebook + JupyterLab

## 1.4 Environment Setup Commands
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install numpy pandas matplotlib seaborn scikit-learn jupyter torch pytest black ruff
```

## 1.5 Project Structure
```text
project/
  data/
  notebooks/
  src/
  tests/
  requirements.txt
  README.md
```

## 1.6 Reproducibility Basics
- Pin dependencies
- Store random seeds
- Track experiment configuration
- Save model artifacts with version tags

## 1.7 First AI-Ready Python Script
```python
import random
import numpy as np

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

print("Environment is ready for reproducible AI experiments")
```

