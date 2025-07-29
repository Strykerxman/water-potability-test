import numpy as np
import pandas as pd

import pickle
import json

from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

def load_data(filepath: str) -> pd.DataFrame:
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        raise Exception(f"Error loading data from {filepath}: {e}")

# X_test = test_data.iloc[:, 0:-1].values
# y_test = test_data.iloc[:, -1].values
def prepare_data(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    try:
        X = data.drop(columns=["Potability"], axis=1)
        y = data["Potability"]
        return X, y
    except Exception as e:
        raise Exception(f"Error preparing data: {e}")

# model = pickle.load(open("model.pkl", "rb"))
def load_model(filepath: str) -> RandomForestClassifier:
    try:
        with open(filepath, "rb") as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        raise Exception(f"Error loading model from {filepath}: {e}")

def evaluate_model(model: RandomForestClassifier, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
    try:
        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        pre = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        metrics_dict = {
            "accuracy": acc,
            "precision": pre,
            "recall": rec,
            "f1_score": f1
        }
        return metrics_dict
    except Exception as e:
        raise Exception(f"Error evaluating model: {e}")

def save_metrics(metrics: dict, filepath: str) -> None:
    try:
        with open("metrics.json", "w") as f:
            json.dump(metrics, f, indent=4)
    except Exception as e:
        raise Exception(f"Error saving metrics to {filepath}: {e}")

def main():
    test_data_path = "./data/processed/test_processed.csv"
    model_path = "model.pkl"
    metrics_path = "metrics.json"

    try:
        test_data = load_data(test_data_path)
        X_test, y_test = prepare_data(test_data)
        model = load_model(model_path)

        metrics = evaluate_model(model, X_test, y_test)
        save_metrics(metrics, metrics_path
                     )
    except Exception as e:
        raise Exception(f"An error occured: {e}")

if __name__ == "__main__":
    main()