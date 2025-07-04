import pandas as pd
from pathlib import Path
import joblib
from sklearn.model_selection import train_test_split
from imblearn.combine import SMOTETomek
from sklearn.ensemble import RandomForestClassifier

def train_model(inputh_data_path: str, ouputh_model_path: str):
    """
    Entrena un modelo RandomForest con datos balanceados y guarda el modelo entrenado.

    Args:
        inputh_data_path (str): Ruta local al dataset procesado.
        ouputh_model_path (str): Ruta local donde guardar el modelo entrenado.
    """
    print(f"Entrenando modelo de {inputh_data_path} y guardando modelo en {ouputh_model_path}")    
    # 1. Leer el dataset procesado
    df = pd.read_csv(inputh_data_path)

    # 2. Separar features y target
    X = df.drop('Machine failure', axis=1)
    y = df['Machine failure']

    # 3. Split train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # 4. Balancear datos con SMOTETomek
    os_us = SMOTETomek()
    X_train_resampled, y_train_resampled = os_us.fit_resample(X_train, y_train)

    # 5. Entrenar RandomForest
    model = RandomForestClassifier()
    model.fit(X_train_resampled, y_train_resampled)

    # 6. Guardar el modelo entrenado
    Path(ouputh_model_path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, ouputh_model_path)
