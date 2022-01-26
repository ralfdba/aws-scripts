S3 PutObject Role
---
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": "*"
        }
    ]
}

AWSLambdaBasicExecution Role
---
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}

Python Code
---
#Talk python to me

import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
	bucket ='aws-simplified-transactions'

	transactionToUpload = {}
	transactionToUpload['transactionId'] = '12345'
	transactionToUpload['type'] = 'PURCHASE'
	transactionToUpload['amount'] = 20
	transactionToUpload['customerId'] = 'CID-11111'

	fileName = 'CID-11111' + '.json'

	uploadByteStream = bytes(json.dumps(transactionToUpload).encode('UTF-8'))

	s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStream)

	print('Put Complete')
