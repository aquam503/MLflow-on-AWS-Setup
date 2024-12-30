import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import mlflow
import mlflow.sklearn

# Set MLflow tracking URI
os.environ["MLFLOW_TRACKING_URI"] = "http://<EC2_PUBLIC_IP>:5000"
def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2
if __name__ == "__main__":
    # Load dataset
    csv_url = "https://raw.githubusercontent.com/mlflow/mlflow/master/tests/datasets/winequality-red.csv"
    data = pd.read_csv(csv_url, sep=";")
    # Split into training and test sets
    train, test = train_test_split(data, test_size=0.25, random_state=42)
    train_x = train.drop("quality", axis=1)
    test_x = test.drop("quality", axis=1)
    train_y = train["quality"]
    test_y = test["quality"]
    # ElasticNet model parameters
    alpha = 0.5
    l1_ratio = 0.5
    with mlflow.start_run():
        model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
        model.fit(train_x, train_y)
        predictions = model.predict(test_x)
        (rmse, mae, r2) = eval_metrics(test_y, predictions)
        print(f"ElasticNet model (alpha={alpha}, l1_ratio={l1_ratio}):")
        print(f"  RMSE: {rmse}")
        print(f"  MAE: {mae}")
        print(f"  R2: {r2}")
        # Log parameters and metrics
        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)
        # Log model
        mlflow.sklearn.log_model(model, "model")