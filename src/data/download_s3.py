from src.utils.s3_utils import download_file

def download_raw_data(bucket: str, s3_key: str, local_path: str):
    """
    Descarga el archivo raw desde un bucket S3 a una ruta local.
    Args:
        bucket (str): Nombre del bucket S3.
        s3_key (str): Ruta del archivo en S3.
        local_path (str): Ruta local donde guardar el archivo.
    """
    print(f"Descargando {s3_key} desde el bucket {bucket} a {local_path}")
    download_file(bucket, s3_key, local_path)
