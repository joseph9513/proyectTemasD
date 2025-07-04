import pandas as pd
from pathlib import Path

def preprocess_data(input_path: str, output_path: str):
    """
    Preprocesa el dataset raw y guarda el archivo procesado localmente
    Args:
        input_path (str): Ruta local del archivo raw descargado.
        output_path (str): Ruta local donde guardar el archivo procesado.
    """
    print(f"Preprocesando datos de {input_path} y enviando datos a {output_path}")
    # Leer el archivo
    df = pd.read_csv(input_path)

    # Validar la columna 'Machine failure' según las otras fallas
    df.loc[(df['TWF'] == 1) | (df['HDF'] == 1) | (df['PWF'] == 1) | (df['OSF'] == 1) | (df['RNF'] == 1), 'Machine failure'] = 1
    df.loc[(df['TWF'] == 0) & (df['HDF'] == 0) & (df['PWF'] == 0) & (df['OSF'] == 0) & (df['RNF'] == 0), 'Machine failure'] = 0

    # Eliminar columnas no necesarias
    df = df.drop(['Product ID', 'UDI', 'TWF', 'HDF', 'PWF', 'OSF', 'RNF'], axis=1)

    # One-hot encoding
    df = pd.get_dummies(df)

    # Convertir booleanos a enteros
    dummy_columns = df.select_dtypes(include=['bool']).columns
    df[dummy_columns] = df[dummy_columns].astype(int)

    # Guardar el procesado localmente
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
