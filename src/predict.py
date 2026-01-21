import joblib
import numpy as np

model = joblib.load("models/build_failure_model.pkl")

def predict_failure(features):
    prob = model.predict_proba([features])[0][1]
    return prob
