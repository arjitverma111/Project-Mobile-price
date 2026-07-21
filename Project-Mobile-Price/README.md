# 📱 Mobile Price Range Predictor

A machine learning web app that predicts a mobile phone's price category based on its hardware specifications. Trained on 8 different algorithms using GridSearchCV to find the best-performing model.

🔗 **[Live Demo →](https://arjit-verma.streamlit.app/mobile-price-predictor)**

---

## 📊 Results

| Metric | Score |
|---|---|
| Training Accuracy | 98% |
| Test Accuracy | 96% |
| Cross-Validation | 5-Fold |
| Best Model | XGBoost / Random Forest |

---

## 🏷 Price Categories

| Class | Label | Estimated Price |
|---|---|---|
| 0 | Low Cost | Under ₹12,000 |
| 1 | Medium Cost | ₹12,000 – ₹20,000 |
| 2 | High Cost | ₹20,000 – ₹35,000 |
| 3 | Very High Cost | ₹35,000+ |

---

## 🧠 Models Compared

GridSearchCV was used to compare 8 classifiers with hyperparameter tuning:

- Logistic Regression (L1, L2, ElasticNet)
- K-Nearest Neighbours
- Decision Tree
- Random Forest
- Ridge Classifier
- AdaBoost
- Gradient Boosting
- **XGBoost** ← best performer

---

## 📋 Features Used (20 total)

| Feature | Description |
|---|---|
| `battery_power` | Battery capacity (mAh) |
| `ram` | RAM in MB |
| `px_height` / `px_width` | Screen resolution |
| `int_memory` | Internal storage (GB) |
| `n_cores` | Number of CPU cores |
| `clock_speed` | Processor speed (GHz) |
| `pc` / `fc` | Primary / Front camera (MP) |
| `mobile_wt` | Weight in grams |
| `sc_h` / `sc_w` | Screen dimensions (cm) |
| `talk_time` | Battery talk time (hrs) |
| `m_dep` | Phone depth (cm) |
| `blue` | Bluetooth (0/1) |
| `dual_sim` | Dual SIM (0/1) |
| `four_g` / `three_g` | Network support (0/1) |
| `touch_screen` | Touch screen (0/1) |
| `wifi` | WiFi (0/1) |

---

## 🗂 Project Structure

```
mobile-price-predictor/
├── data/
│   ├── train.csv              # Training dataset
│   └── test.csv               # Test dataset
├── train.py                   # Model training + GridSearchCV
├── app.py                     # Streamlit web app
├── mobile_price_model.joblib  # Saved best model
├── requirements.txt
└── README.md
```

---

## ⚡ Quickstart

```bash
# 1. Clone the repo
git clone https://github.com/Arjit-Verma/mobile-price-predictor
cd mobile-price-predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train the model
python train.py

# 4. Run the app
streamlit run app.py
```

---

## 🛠 Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| scikit-learn | ML models + Pipeline + GridSearchCV |
| XGBoost | Best performing classifier |
| Pandas / NumPy | Data processing |
| Matplotlib | Visualisation |
| Streamlit | Web interface |
| joblib | Model saving |

---

## 📦 Dataset

[Mobile Price Classification — Kaggle](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification)

2,000 mobile phones with 20 hardware features and a price range label.

---

## 👤 Author

**Arjit Verma** — BTech CSE @ GGSIPU (2025–2029)

[![GitHub](https://img.shields.io/badge/GitHub-Arjit--Verma-black?logo=github)](https://github.com/arjitverma111)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](www.linkedin.com/in/111-arjit-verma)

---

## 📄 License

MIT License — free to use and modify.
