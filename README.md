# Failure-modes-and-load-bearing-capacity-prediction-for-CFST-columns-under-axial-compression
# Probabilistic Prediction Tool for CFST Columns under Axial Compression

This repository hosts a user-friendly web application for probabilistically predicting the failure modes and load-bearing capacities of Concrete-Filled Steel Tube (CFST) columns under axial compression. Built on advanced machine learning models, this tool provides engineers and researchers with uncertainty-aware predictions to support structural design and safety assessment.


![Uploading 5.3 GUI.jpg…]()

*Figure 1: Web interface for probabilistic prediction of CFST columns.*

## Features

- **Probabilistic Failure Mode Prediction**: Classifies columns into three failure modes:
  - Local Buckling Failure
  - Flexural Instability Failure
  - Combined Failure
- **Load-Bearing Capacity Estimation**: Predicts axial capacity with uncertainty quantification (mean, standard deviation, 95% confidence interval).
- **Cascaded Model Architecture**: Integrates a random forest classifier for failure modes and NGBoost regressors for capacity prediction.
- **Interactive Web Interface**: Intuitive 2x3 input grid with pre-filled default values for quick testing.
- **Structured Results Display**: Clear separation of failure mode and load capacity predictions in a two-column layout.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/zhongxueqi/failure-modes-prediction-and-load-bearing-capacity-of-CFST-columns-under-axial-compression.git
   cd failure-modes-prediction-and-load-bearing-capacity-of-CFST-columns-under-axial-compression
   ```

2. **Install dependencies** (preferably in a virtual environment):
   ```bash
   pip install flask numpy pandas scikit-learn ngboost joblib
   ```

3. **Download pre-trained models** (automatically included in the repository).

## Usage

1. **Start the application**:
   ```bash
   Run Main.py
   ```

2. **Access the web interface** in your browser at `http://localhost:5000`.

3. **Input parameters**:
   - H (mm): Column height
   - L/B ratio: Slenderness ratio
   - fy (MPa): Steel yield strength
   - fck (MPa): Concrete compressive strength
   - Acfck (N): Concrete cross-sectional area × fck
   - Asfy (N): Steel cross-sectional area × fy

4. **Click "Predict"** to obtain results.

## Model Architecture

The prediction framework employs a two-stage approach:
1. **Failure Mode Classification**: NGBoost classifier trained on 6 input parameters.
2. **Load Capacity Regression**: NGBoost probabilistic regressors, one for each failure mode, providing both point estimates and uncertainty quantification.


## Citation

If you use this tool in your research, please cite our paper:
```bibtex
@article{your-paper-citation,
  title = {Probabilistic Prediction of Failure Modes and Load-Bearing Capacity for CFST Columns under Axial Compression},
  author = {Zhong Xueqi and [Co-authors]},
  journal = {Journal Name},
  year = {2025},
  volume = {XX},
  pages = {XXX-XXX},
  doi = {10.XXXX/XXXXXX}
}
```

## Contact

For questions or support, please contact:
- Xueqi Zhong (zhong_xueqi@fafu.edu.cn)
