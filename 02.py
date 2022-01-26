"""
Crearemos instancias de EC2
Utilizando Python
"""
import boto3
ec2 = boto3.resource('ec2')
ec2.create_instances(ImageId='ami-0a91cd140a1fc148a', MinCount = 1, MaxCount = 2, InstanceType='t2.micro')