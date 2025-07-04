import boto3
from pathlib import Path

def download_file(bucket: str, s3_key: str, local_path: str):
    """
    Descarga un archivo desde S3 a una ruta local.
    Args:
        local_path (str): Ruta local del archivo.
        bucket (str): Nombre del bucket.
        s3_key (str): Ruta destino dentro del bucket.
    """
    s3 = boto3.client("s3")
    Path(local_path).parent.mkdir(parents=True, exist_ok=True)
    s3.download_file(bucket, s3_key, local_path)

def upload_file(local_path: str, bucket: str, s3_key: str):
    """
    Sube un archivo local a un bucket S3.
    Args:
        local_path (str): Ruta local del archivo.
        bucket (str): Nombre del bucket.
        s3_key (str): Ruta destino dentro del bucket.
    """
    s3 = boto3.client('s3')
    s3.upload_file(bucket, s3_key, local_path)