"""
Eliminar instancias
"""
import boto3
instancia_ids = ['i-0ae83d5ef7b915be7','i-00096a3dedb1ecf4a']
ec2 = boto3.resource('ec2')
ec2.instances.filter(InstanceIds = instancia_ids).terminate()