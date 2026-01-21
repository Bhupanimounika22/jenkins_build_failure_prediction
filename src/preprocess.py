import pandas as pd

def load_and_preprocess():
    df = pd.read_csv("data/jenkins_builds.csv")

    X = df[
        ["duration", "code_changes", "tests_failed",
         "hour", "prev_failure", "failure_last_5"]
    ]
    y = df["failure"]

    return X, y
