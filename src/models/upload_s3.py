from src.utils.s3_utils import upload_file

def upload_model(local_path: str, bucket: str, s3_key:str):
    """
    Sube el archivo de modelo a S3.
    """
    print(f"Subiendo modelo de {local_path} a s3://{bucket}/{s3_key}")
    upload_file(local_path, bucket, s3_key)