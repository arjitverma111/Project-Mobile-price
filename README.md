# 📱 Mobile Price Range Predictor

A machine learning web app that predicts a mobile phone's price category based on its hardware specifications. Trained on 8 different algorithms using GridSearchCV to find the best-performing model.

🔗 **[Live Demo →](https://project-mobile-price.streamlit.app/)**

---

## 📊 Results

| Metric | Score |
|---|---|
| Training Accuracy | 96.88% |
| Test Accuracy | 98.60% |
| Cross-Validation | 5-Fold |
| Best Model | LogisticRegression(C=10, max_iter=5000, penalty='l1',random_state=42, solver='saga')|

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

- **LogisticRegression** (L1, L2, ElasticNet) ← best performer
- KNeighborsClassifier
- DecisionTreeClassifier
- RandomForestClassifier
- RidgeClassifier
- AdaBoostClassifier
- GradientBoostingClassifier
- XGBClassifier

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

## 📂 Project Structure

​```
project-mobile-price/
├── app.py                      # Streamlit web app
├── mobile_price_model.joblib   # Saved trained model
├── requirements.txt            # Python dependencies
├── README.md
└── extra files/                # Notebooks & data used during development
    ├── cleaning-EDA.ipynb      # Data cleaning & exploratory analysis
    ├── Model.ipynb             # Model training + evaluation
    ├── train.csv                # Training dataset
    ├── test.csv                 # Test dataset
    └── test_cleaned.csv         # Cleaned test dataset
​```

---

## ⚡ Quickstart

​```bash
# 1. Clone the repo
git clone https://github.com/arjitverma111/Project-Mobile-price
cd project-mobile-price

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
​```
> 💡 The trained model (`mobile_price_model.joblib`) is already included, so you can run the app right away.
> If you'd like to retrain it yourself, open `extra files/Model.ipynb` in Jupyter and run all cells.

---

## 🛠 Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| scikit-learn | ML models + Pipeline + GridSearchCV |
| LogisticRegression | Best performing classifier |
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
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/111-arjit-verma)

---

## 📄 License

MIT License — free to use and modify.
