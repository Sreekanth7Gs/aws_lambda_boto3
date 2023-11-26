import boto3
import os

def upload_to_s3(local_file_path, s3_bucket_name):
    s3 = boto3.client('s3')
    file_name = os.path.basename(local_file_path)
    s3.upload_file(local_file_path, s3_bucket_name, file_name)
    print(f"File {file_name} uploaded to lambda4bucket")

if __name__ == "__main__":
    upload_directory = 'uploads'
    s3_bucket = "lambda4bucket"

    for filename in os.listdir(upload_directory):
        file_path = os.path.join(upload_directory, filename)
        upload_to_s3(file_path, s3_bucket)

