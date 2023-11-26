

AWS Lambda Assignment - SES Email Notifications with SQS
Overview
This repository contains the code for an AWS Lambda function triggering SES email notifications based on SQS messages.
 Three SNS topics handle notifications for different statuses.

Setup
-SQS Queue:
-Create an SQS queue named message2_queue.
Lambda Function:
Create a Lambda function (message2_function) with Python 3.8 runtime.
-Add an SQS trigger.
IAM Role:
- Attach policies for SES, SQS, and SNS permissions to the Lambda function's IAM role.
SNS Topics:
- Create SNS topics for Payments, Returns, and other statuses.
- Note down topic ARNs.
SES Email Verification:
- Verify email addresses in SES for sending notifications.
Lambda Code:
- Replace default code with provided Python script.
Deploy the Lambda function.
- Publish SQS Messages:
Publish messages with different statuses to the SQS queue.
Monitoring:
- Check CloudWatch logs in the Lambda function for troubleshooting.
Sample Messages

Created by : Sreekanth Gs
