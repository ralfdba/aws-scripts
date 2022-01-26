"""
Utilizando AWS Api
instalar en nuestro computador
Python
pip install boto3
pip install awscli
aws configure
.aws/config
.aws/credentials
"""
import boto3
#listar las instancias de EC2
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)