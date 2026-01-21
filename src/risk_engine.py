def normalize(value, max_value):
    return min(value / max_value, 1.0)

def compute_adjusted_risk(
    ml_risk,
    tests_failed,
    code_changes,
    prev_failure,
    alpha=0.4
):
    # Normalize inputs
    tf = normalize(tests_failed, 10)
    cc = normalize(code_changes, 500)
    pf = prev_failure

    # Current Build Quality Score
    CBQS = 1 - (0.4*tf + 0.4*cc + 0.2*pf)
    CBQS = max(0, min(1, CBQS))

    # Adjusted risk
    adjusted_risk = ml_risk * (1 - CBQS * alpha)

    return adjusted_risk, CBQS
