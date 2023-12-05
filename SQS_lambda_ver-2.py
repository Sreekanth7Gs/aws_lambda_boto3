import json
import boto3

def lambda_handler(event, context):
    sns_client = boto3.client('sns', region_name='us-east-1')

    for record in event['Records']:
        try:
            print(f"Record Body: {record['body']}")

            message_body = json.loads(record['body'])
            
            status = message_body.get('status').lower()

            if status == 'refund':
                sns_topic_arn = 'arn:aws:sns:us-east-1:882457892107:refund_sns' 
                publish_message(sns_client, sns_topic_arn, message_body)

            elif status == 'order':
                sns_topic_arn = 'arn:aws:sns:us-east-1:882457892107:order_sns'
                publish_message(sns_client, sns_topic_arn, message_body)

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
           
        except Exception as e:
            print(f"Unexpected error: {e}")
            

def publish_message(sns_client, sns_topic_arn, message_body):
    try:
        sns_response = sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=json.dumps(message_body),
        )

        print(f"Message published to {sns_topic_arn}. Response: {sns_response}")

    except Exception as e:
        print(f"Error publishing message: {e}")
       
