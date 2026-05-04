import mlflow
import pandas as pd
import joblib # Tambahkan ini
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import os
import numpy as np
import warnings
import sys

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    file_path = sys.argv[3] if len(sys.argv) > 3 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "train_pca.csv")
    data = pd.read_csv(file_path)

    X_train, X_test, y_train, y_test = train_test_split(
        data.drop("Credit_Score", axis=1),
        data["Credit_Score"],
        random_state=42,
        test_size=0.2
    )
    
    n_estimators = int(sys.argv[1]) if len(sys.argv) > 1 else 505
    max_depth = int(sys.argv[2]) if len(sys.argv) > 2 else 37

    with mlflow.start_run():
        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
        model.fit(X_train, y_train) # Fit Cukup Sekali

        # Simpan ke PKL dengan nama statis agar otomatis terpakai di Docker
        joblib.dump(model, "model.pkl") 

        # Log ke MLflow (untuk riwayat di local/GitHub Actions saja)
        mlflow.sklearn.log_model(sk_model=model, artifact_path="model")
        
        accuracy = model.score(X_test, y_test)
        mlflow.log_metric("accuracy", accuracy)
        print(f"Model berhasil disimpan sebagai model.pkl dengan akurasi: {accuracy}")