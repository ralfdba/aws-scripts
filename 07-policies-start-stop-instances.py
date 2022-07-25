Creando policys aws
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "logs:FilterLogEvents",
            "Resource": "*",
            "Condition": {
                "DateGreaterThan": {
                    "aws:CurrentTime": "2020-12-02T00:00:00Z"
                },
                "DateLessThan": {
                    "aws:CurrentTime": "2020-01-02T00:00:00Z"
                }
            }
        }
    ]
}
------------------------------------
Policy para lambda function detener instancias y dejarlas en cloudwatch para hacer rules despues
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
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:Start*",
        "ec2:Stop*"
      ],
      "Resource": "*"
    }
  ]
}


Stops the EC2 instances
import boto3
region = 'ap-south-1'
instances = ['i-12345', 'i-2345']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))

Starts the EC2 instances

import boto3
region = 'ap-south-1'
instances = ['i-12345', 'i-2345']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))
-------------------------------------------------------------
Policy para lambda function para ec2 y s3 y luego crear la regla para la automatización
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogStream",
        "ec2:DescribeInstances",
        "ec2:CreateTags",
		"ec2:CreateSnapshot",
		"logs:CreateLogGroup",
		"logs:PutLogEvents"
      ],
      "Resource": "*"
    }
  ]
}
ver contenido en python
