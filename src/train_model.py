# src/train.py
from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import joblib
from preprocess import load_and_preprocess

X, y = load_and_preprocess()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

rf = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    class_weight="balanced",
    random_state=42
)

calibrated_model = CalibratedClassifierCV(rf, method="isotonic")
calibrated_model.fit(X_train, y_train)

probs = calibrated_model.predict_proba(X_test)[:, 1]
print("ROC-AUC:", roc_auc_score(y_test, probs))

joblib.dump(calibrated_model, "models/build_failure_model.pkl")
print("✅ Calibrated model saved")
