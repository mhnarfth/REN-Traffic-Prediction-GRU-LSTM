# REN Traffic Prediction using Ensemble GRU-LSTM

[
[

## Overview

This repository implements traffic forecasting for Research and Education Networks (RENs) using real-world Internet2 data from Atlanta and Dallas routers. The project includes a hybrid GRU-LSTM model with multi-step forecasting capabilities (1, 2, 5, and 10 steps ahead) and anomaly detection using Isolation Forest and LOF.

## Repository Structure

```
REN-Traffic-Prediction-GRU-LSTM/
├── notebooks/
│   ├── (1 step) LSTM-GRU_and_Prophet.ipynb           # Single-step forecasting
│   ├── (2,5,10 step) LSTM-GRU_and_Prophet copy.ipynb # Multi-horizon forecasting
│   └── EDA plots needed only.ipynb                   # Data exploration
├── Preprocessing/                                     # Data processing scripts
├── datasets/                                          # Dataset storage
├── plots/                                            # Generated plots
└── data/                                             # Place your parquet file here
```


## Quick Start

### 1. Install Dependencies

```bash
pip install tensorflow pandas numpy scikit-learn matplotlib prophet pyarrow jupyter
```


### 2. Prepare Data

Place your combined router data here:

```
data/combined_router_dallas_atla_data.parquet
```

**Required columns**: `t_first` (datetime), `router` (string), `in_packets` (int64)

### 3. Run Notebooks

**Step 1**: Data exploration

```bash
jupyter lab "EDA plots needed only.ipynb"
```

**Step 2**: Single-step prediction (1 hour ahead)

```bash
jupyter lab "(1 step) LSTM-GRU_and_Prophet.ipynb"
```

**Step 3**: Multi-step prediction (2, 5, 10 hours ahead)

```bash
jupyter lab "(2,5,10 step) LSTM-GRU_and_Prophet copy.ipynb"
```


## Data Pipeline

1. **Source**: NetFlow data from Internet2 backbone (Atlanta \& Dallas routers)
2. **Storage**: Fetched from UNL Holland Computing Center (HCC)
3. **Processing**: Unzip → Combine routers → Convert to Parquet → Hourly resampling
4. **Modeling**: GRU-LSTM ensemble vs Prophet baseline
5. **Output**: Traffic predictions + anomaly detection

## Key Features

- **Multi-horizon forecasting**: 1, 2, 5, and 10-step ahead predictions
- **Hybrid architecture**: GRU + LSTM ensemble model
- **Baseline comparison**: Prophet model for benchmarking
- **Anomaly detection**: Isolation Forest and Local Outlier Factor
- **Real REN data**: Internet2 backbone traffic analysis


## Model Performance

- GRU-LSTM outperforms Prophet across all lead times
- Maintains accuracy up to 10-step ahead predictions
- Successfully identifies network traffic anomalies


## File Path Fix

Update the data path in notebooks from absolute to relative:

```python
# Change this line in notebooks:
file_path = '/Users/maushariff/Downloads/.../combined_router_dallas_atla_data.parquet'

# To this:
file_path = 'data/combined_router_dallas_atla_data.parquet'
```


## Citation

```bibtex
@article{shariff2024traffic,
  title={Traffic Prediction for Research and Education Networks using an Ensemble GRU-LSTM with Varying Lead Times},
  author={Shariff, Mohammad Arafath Uddin and Karanam, Venkat Sai Suman Lamba and Ramamurthy, Byrav},
  institution={University of Nebraska-Lincoln},
  year={2024}
}
```


## Contact

- Mohammad Arafath Uddin Shariff - mshariff2@unl.edu

***


