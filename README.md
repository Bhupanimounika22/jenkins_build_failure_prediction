Got it 👍
Below is a **FINAL, CORRECT, and SAFE `README.md`** that **matches EXACTLY**:

* ✅ Your **current `train.py`**
* ✅ Single **Calibrated RandomForest**
* ✅ Dataset generator
* ✅ Streamlit app
* ✅ **Model folder creation requirement**

You can **copy–paste this directly**.

---

# 🚀 Jenkins Build Failure Prediction System

**Calibrated Machine Learning + Rule-Aware Risk Analysis**

---

## 📌 Project Overview

This project predicts **Jenkins CI build failures** using a **calibrated Random Forest classifier** and a **rule-aware risk adjustment engine**.
It helps DevOps teams assess **build risk before execution** and take informed decisions.

The system combines:

* Machine Learning (Random Forest)
* Probability Calibration (Isotonic)
* Historical build behavior
* Rule-based risk scoring
* Interactive Streamlit dashboard

---

## 🎯 Objectives

* Predict probability of build failure
* Improve trust using calibrated probabilities
* Use historical signals (previous failures)
* Provide actionable risk levels
* Support CI/CD decision-making

---

## 🧠 System Architecture

```
Jenkins Build Data
        ↓
Feature Engineering
        ↓
Random Forest Classifier
        ↓
Probability Calibration (Isotonic)
        ↓
Rule-Aware Risk Adjustment
        ↓
Streamlit Dashboard
```

---

## 📊 Features Used

| Feature        | Description                  |
| -------------- | ---------------------------- |
| duration       | Build duration in seconds    |
| code_changes   | Number of code lines changed |
| tests_failed   | Count of failed tests        |
| hour           | Build execution hour         |
| prev_failure   | Previous build failure flag  |
| failure_last_5 | Failures in last 5 builds    |

---

## 📁 Project Structure

```
jenkins_build_failure_prediction/
│
├── data/
│   └── jenkins_builds.csv         # Generated dataset
│
├── src/
    ├── dataset_generator.py  
│   ├── train.py                   # Model training & calibration
│   ├── preprocess.py              # Data loading & preprocessing
│   ├── predict.py                 # Prediction logic
│   └── risk_engine.py             # Rule-based risk adjustment
│
├── models/
│   └── build_failure_model.pkl    # Trained calibrated model
│
├── app.py                         # Streamlit web application
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Bhupanimounika22/jenkins_build_failure_prediction.git
cd jenkins_build_failure_prediction
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python3 -m venv venv        # macOS / Linux
python -m venv venv         #Windows
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate          # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project

### Step 1: Create Required Folders (IMPORTANT)

From the project root:

```bash
mkdir data
mkdir models
```

> These folders are required to save the dataset and trained model.

---

### Step 2: Generate Dataset

```bash
python3 src/dataset_generator.py # Macos
python src/dataset_generator.py  #Windows
```

This will create:

```
data/jenkins_builds.csv
```

---

### Step 3: Train the Model

```bash
python3 src/train_model.py #Macos
python src/train_model.py #Windows
```

Expected output:

```
ROC-AUC: 0.70xx and 0.80xx 
✅ Calibrated model saved
```

The trained model is saved to:

```
models/build_failure_model.pkl
```

---

### Step 4: Run the Web Application

```bash
streamlit run app.py
```

---

## 🖥️ Application Functionality

The Streamlit dashboard displays:

* 📊 **ML Failure Risk**
* 🧪 **Build Quality Score**
* ⚠️ **Adjusted Risk**
* 📈 **Risk Comparison Chart**
* 🚦 **Decision Recommendation**

### Risk Levels

* 🟢 **Low Risk** → Safe to proceed
* 🟠 **Medium Risk** → Proceed with caution
* 🔴 **High Risk** → Block or review build

---

## 📈 Model Performance

* **Model:** Random Forest (Calibrated)
* **Metric:** ROC-AUC
* **Score:** ~0.70
* Well-suited for **noisy CI/CD data**

---

## 🔬 Key Contributions

* Probability calibration for trustworthy predictions
* Integration of ML and domain rules
* Interpretable risk scoring
* Lightweight and extensible design

---

## 🧪 Dataset Description

* Synthetic Jenkins build data
* Simulates realistic CI behavior
* Includes temporal and historical signals

---

## 🛠️ Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Matplotlib
* Joblib

---

 
