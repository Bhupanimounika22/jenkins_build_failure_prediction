# app.py
import streamlit as st
import matplotlib.pyplot as plt
from src.predict import predict_failure
from src.risk_engine import compute_adjusted_risk

st.set_page_config(
    page_title="Jenkins Failure Predictor",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Jenkins Build Failure Predictor")
st.caption("AI-Driven CI/CD Risk Intelligence")

# ================= SIDEBAR =================
st.sidebar.header("⚙️ Build Parameters")

duration = st.sidebar.slider("⏱️ Build Duration (sec)", 60, 1200, 300)
code_changes = st.sidebar.slider("🧩 Lines Changed", 1, 1200, 200)
tests_failed = st.sidebar.slider("🧪 Failed Tests", 0, 20, 2)
hour = st.sidebar.slider("🕒 Build Hour", 0, 23, 12)
prev_failure = st.sidebar.radio("❗ Previous Build Failed?", ["No", "Yes"])
failure_last_5 = st.sidebar.slider("📉 Failures in Last 5 Builds", 0, 5, 1)

prev_failure = 1 if prev_failure == "Yes" else 0

# ================= MAIN =================
if st.sidebar.button("🔍 Analyze Build Risk"):
    features = [
        duration,
        code_changes,
        tests_failed,
        hour,
        prev_failure,
        failure_last_5
    ]

    ml_risk = predict_failure(features)
    adjusted_risk, quality_score = compute_adjusted_risk(
        ml_risk,
        tests_failed,
        code_changes,
        prev_failure,
        failure_last_5
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("📊 ML Failure Risk", f"{ml_risk:.1%}")
    col2.metric("🧪 Build Quality Score", f"{quality_score:.1%}")
    col3.metric("⚠️ Adjusted Risk", f"{adjusted_risk:.1%}")

    st.progress(min(adjusted_risk, 1.0))

    if adjusted_risk > 0.65:
        st.error("🔴 High Risk – Block or Review Build")
    elif adjusted_risk > 0.35:
        st.warning("🟠 Medium Risk – Proceed with caution")
    else:
        st.success("🟢 Low Risk – Safe to proceed")

    st.subheader("📈 Risk Comparison")
    fig, ax = plt.subplots()
    ax.bar(["ML Risk", "Adjusted Risk"], [ml_risk, adjusted_risk])
    ax.set_ylim(0, 1)
    ax.set_ylabel("Probability")
    st.pyplot(fig)

st.markdown("---")
st.caption("Hybrid ML + Rule-Aware CI Failure Prediction System")
