import json
import boto3

def lambda_handler(event, context):
    for record in event['Records']:
        message_body = json.loads(record['body'])
        recipient_email = "gssreekanth21@gmail.com"  
        email_message = f"Message from SQS: {message_body['message']}"
        send_email(email_message, recipient_email)

def send_email(message, recipient_email):
    sns_topic_arn = "arn:aws:sns:us-east-1:882457892107:Messsage_SNS"
    ses_sender_email = "gssreekanth016@gmail.com"

    sns_client = boto3.client('sns')
    ses_client = boto3.client('ses')

    sns_response = sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=message,
    )

    ses_response = ses_client.send_email(
        Source=ses_sender_email,
        Destination={'ToAddresses': [recipient_email]},
        Message={'Subject': {'Data': 'SQS Message'},
                 'Body': {'Text': {'Data': message}}},
    )

    print("Message sent:", sns_response, ses_response)
