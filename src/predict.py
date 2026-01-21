import joblib
import numpy as np

# Load trained calibrated model once
model = joblib.load("models/build_failure_model.pkl")

def predict_failure(features):
    """
    Predict probability of build failure.

    Parameters:
        features (list): 
        [duration, code_changes, tests_failed,
         hour, prev_failure, failure_last_5]

    Returns:
        float: failure probability (0–1)
    """

    features = np.array(features).reshape(1, -1)

    # Probability of failure (class = 1)
    prob = model.predict_proba(features)[0][1]

    return prob
