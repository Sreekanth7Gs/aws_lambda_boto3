import json
import boto3

def lambda_handler(event, context):
    for record in event['Records']:
        message_body = json.loads(record['body'])
        email_message = f"Message from SQS: {message_body['message']}"
        send_email_via_sns(email_message)

def send_email_via_sns(message):
    sns_topic_arn = "arn:aws:sns:us-east-1:882457892107:Messsage_SNS"

    sns_client = boto3.client('sns')

    sns_response = sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=message,
        Subject="SQS Message",
    )

    print("Message sent via SNS:", sns_response)
