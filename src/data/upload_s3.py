from src.utils.s3_utils import upload_file

def upload_processed_data(local_path: str, bucket: str, s3_key: str):
    """
    Sube el archivo de datos procesados a S3.
    """
    print(f"Subiendo datos procesados a s3://{bucket}/{s3_key}")
    upload_file(local_path, bucket, s3_key)