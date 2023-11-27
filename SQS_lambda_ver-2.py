import json
import boto3

def lambda_handler(event, context):
    sns_client = boto3.client('sns', region_name='us-east-1')
    ses_client = boto3.client('ses', region_name='us-east-1')

    for record in event['Records']:
        try:
            print(f"Record Body: {record['body']}")

            message_body = json.loads(record['body'])
            
            status = message_body.get('status', 'default').lower()
            message_content = message_body.get('content', 'No content')

            if status == 'refund':
                sns_topic_arn = 'arn:aws:sns:us-east-1:882457892107:refund_sns' 
                to_email = 'manoj11223s@gmail.com'
                send_email(ses_client, to_email, message_body)
                sns_client.publish(
                    TopicArn=sns_topic_arn,
                    Message=json.dumps(message_body),
                )

            elif status == 'order':
                sns_topic_arn = 'arn:aws:sns:us-east-1:882457892107:order_sns'
                to_email = 'gssreekanth21@gmail.com'
                send_email(ses_client, to_email, message_body)
                sns_client.publish(
                    TopicArn=sns_topic_arn,
                    Message=json.dumps(message_body),
                )

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            # Handle JSON decoding error
        except Exception as e:
            print(f"Unexpected error: {e}")
            # Handle other unexpected errors

def send_email(ses_client, to_email, message_body):
    ses_sender_email = "gssreekanth016@gmail.com"

    subject = f"Notification for status: {message_body.get('status', 'Unknown')}"
    body = f"Message Content:\n{message_body.get('content', 'No content')}"

    try:
        response = ses_client.send_email(
            Source=ses_sender_email,
            Destination={'ToAddresses': [to_email]},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': body}}
            }
        )

        print(f"Email sent to {to_email}. Response: {response}")

    except Exception as e:
        print(f"Error sending email: {e}")
        # Handle email sending error
