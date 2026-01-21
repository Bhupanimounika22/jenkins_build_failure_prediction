import pandas as pd
import numpy as np
import os

np.random.seed(42)
n_builds = 800
df = pd.DataFrame({
    "build_number": range(1, n_builds + 1),
    "duration": np.random.randint(60, 1200, n_builds),
    "code_changes": np.random.randint(1, 1200, n_builds),
    "tests_failed": np.random.poisson(2, n_builds),
    "hour": np.random.randint(0, 24, n_builds),
})

# Base failure probability
failure_prob = (
    0.25 * (df["tests_failed"] > 2).astype(int) +
    0.35 * (df["code_changes"] > 500).astype(int) +
    0.20 * (df["duration"] > 800).astype(int) +
    0.10 * ((df["hour"] >= 0) & (df["hour"] <= 5)).astype(int)
)

df["failure"] = (failure_prob + np.random.rand(n_builds) > 0.6).astype(int)

df["prev_failure"] = df["failure"].shift(1).fillna(0)
df["failure_last_5"] = df["failure"].rolling(5).sum().fillna(0)

df.to_csv("data/jenkins_builds.csv", index=False)
print("✅ Dataset generated successfully")
