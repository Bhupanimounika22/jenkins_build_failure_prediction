import streamlit as st
import matplotlib.pyplot as plt
from src.predict import predict_failure
from src.risk_engine import compute_adjusted_risk

st.set_page_config(page_title="Jenkins Build Failure Predictor")

st.title("🚀 Predictive Build Failure Analysis in Jenkins")
st.markdown("Predict **build failure risk BEFORE execution** using ML")

st.sidebar.header("Build Parameters")

duration = st.sidebar.slider("Build Duration (sec)", 30, 600, 200)
code_changes = st.sidebar.slider("Lines of Code Changed", 1, 500, 100)
tests_failed = st.sidebar.slider("Failed Tests", 0, 10, 1)
hour = st.sidebar.slider("Build Hour", 0, 23, 12)
prev_failure = st.sidebar.selectbox("Previous Build Failed?", [0, 1])
failure_last_5 = st.sidebar.slider("Failures in Last 5 Builds", 0, 5, 1)

if st.button("Predict Build Outcome"):
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
        prev_failure
    )

    st.subheader("Prediction Result")

    st.write(f"📊 Historical Risk (ML): **{ml_risk:.2%}**")
    st.write(f"🧪 Current Build Quality Score: **{quality_score:.2%}**")

    if adjusted_risk >= 0.65:
        st.error(f"🔴 High Risk ({adjusted_risk:.2%}) – Historically unstable")
    elif adjusted_risk >= 0.35:
        st.warning(f"🟠 Medium Risk ({adjusted_risk:.2%})")
    else:
        st.success(f"🟢 Low Risk ({adjusted_risk:.2%}) – Build likely to succeed")

    fig, ax = plt.subplots()
    ax.bar(["Historical Risk", "Adjusted Risk"], [ml_risk, adjusted_risk])
    ax.set_ylabel("Probability")
    st.pyplot(fig)

st.markdown("---")
st.caption("Hybrid ML-based CI Build Failure Prediction System")
