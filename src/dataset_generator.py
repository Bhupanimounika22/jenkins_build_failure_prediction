import pandas as pd
import numpy as np

np.random.seed(42)

n_builds = 500

data = {
    "build_number": range(1, n_builds + 1),
    "duration": np.random.randint(30, 600, n_builds),  # seconds
    "code_changes": np.random.randint(1, 500, n_builds),
    "tests_failed": np.random.randint(0, 10, n_builds),
    "hour": np.random.randint(0, 24, n_builds),
}

df = pd.DataFrame(data)

# Failure logic (realistic)
df["failure"] = (
    (df["tests_failed"] > 2) |
    (df["code_changes"] > 300)
).astype(int)

df["prev_failure"] = df["failure"].shift(1).fillna(0)
df["failure_last_5"] = df["failure"].rolling(5).sum().fillna(0)

df.to_csv("data/jenkins_builds.csv", index=False)
print("Dataset created: data/jenkins_builds.csv")
 
