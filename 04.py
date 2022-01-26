"""
Creando un VPC con python
"""
import boto3
cliente = boto3.resource('ec2')
vpc = cliente.create_vpc(CidrBlock='172.18.0.0/16')
vpc.create_tags(Tags=[{"Key":"VPC","Value":"En Python Curso AWS"}])
vpc.wait_until_available()