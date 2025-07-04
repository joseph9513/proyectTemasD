from src.data.download_s3 import download_raw_data
from src.data.preprocess import preprocess_data
from src.data.upload_s3 import upload_processed_data
from src.models.train_model import train_model
from src.models.upload_s3 import upload_model

BUCKET = "ta2-temasd-bucket-789159"

if __name__ == "__main__":
    raw_local = "data/raw/raw_dataset.csv"
    processed_local = "data/processed/processed_dataset.csv"
    model_local = "models/final_model.pkl"

    download_raw_data(bucket=BUCKET, s3_key="data/raw/raw_dataset.csv", local_path=raw_local)

    preprocess_data(input_path=raw_local, output_path=processed_local)

    upload_processed_data(bucket=BUCKET, s3_key="data/processed/processed_dataset.csv", local_path=processed_local)
    
    train_model(inputh_data_path=processed_local, ouputh_model_path=model_local)

    upload_model(local_path=model_local, bucket=BUCKET, s3_key="models/final_model.pkl")
