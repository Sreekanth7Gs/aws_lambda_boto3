import boto3
import os

def lambda_handler(event, context):
    try:
        print(f"Received event: {event}")

        event_name = event['Records'][0]['eventName']
        if event_name != 'ObjectCreated:Put':
            print(f"Skipping event type: {event_name}")
            return {
                'statusCode': 200,
                'body': f'Skipping event type: {event_name}'
            }

        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']

        folder_name = os.path.dirname(key)

        file_extension = os.path.splitext(key)[1].lower()

        s3 = boto3.client('s3')

        extension_to_folder = {
            '.jpg': 'images',
            '.png': 'images',
            '.txt': 'txt',
            '.pdf': 'pdfs',
        }

        folder_name_extension = extension_to_folder.get(file_extension, 'other')

        new_key = f"{folder_name_extension}/{os.path.basename(key)}"
        copy_source = {'Bucket': bucket, 'Key': key}

        s3.copy_object(Bucket=bucket, CopySource=copy_source, Key=new_key)

        s3.delete_object(Bucket=bucket, Key=key)

        return {
            'statusCode': 200,
            'body': f'File moved to {folder_name_extension} folder successfully!'
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        raise e
