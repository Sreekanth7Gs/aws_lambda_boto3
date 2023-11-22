import json
import boto3

def lambda_handler(event, context):
    sns_client = boto3.client('sns', region_name='us-east-1')
    ses_client = boto3.client('ses', region_name='us-east-1')

    for record in event['Records']:
        message_body = json.loads(record['body'])
        
        status = message_body.get('status', 'default')
        message_content = message_body.get('content', 'No content')

        if status == 'Payments':
            sns_topic_arn = 'arn:aws:sns:us-east-1:882457892107:payments_sns'
            to_email = 'manoj11223s@gmail.com'
        elif status == 'Returns':
            sns_topic_arn = 'arn:aws:sns:us-east-1:882457892107:return_sns'
            to_email = 'gssreekanth21@gmail.com'
        else:
            sns_topic_arn = 'arn:aws:sns:us-east-1:882457892107:orders-88df3011-59e9-46ac-ac2c-8c0327f85ae2'
            to_email = 'manojkumar052023@gmail.com'
    
        send_email(ses_client, to_email, message_body)

        sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=json.dumps(message_body),
        )

def send_email(ses_client, to_email, message_body):
    ses_sender_email = "gssreekanth016@gmail.com"

    subject = f"Notification for status: {message_body.get('status', 'Unknown')}"
    body = f"Message Content:\n{message_body.get('content', 'No content')}"


    response = ses_client.send_email(
        Source=ses_sender_email,
        Destination={'ToAddresses': [to_email]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': body}}
        }
    )

    print(f"Email sent to {to_email}. Response: {response}")
