import boto3
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    resultado = ec2.describe_volumes( Filters=[{'Name': 'tag:status', 'Values': ['in-use']}])
    for volume in resultado['Volumes']:
        print( volume['VolumeId'], volume['AvailabilityZone'] )
        resultado2 = ec2.create_snapshot(VolumeId=volume['VolumeId'],Description='Creado por lambda')
        ec2resource = boto3.resource('ec2')
        snapshot = ec2resource.Snapshot(resultado2['SnapshotId'])
        if 'Tags' in volume:
            for tags in volume['Tags']:
                if tags["Key"] == 'Name':
                    nombredisco = tags["Value"]
        else:
            nombredisco = 'SN'
        snapshot.create_tags(Tags=[{'Key': 'Name','Value': nombredisco}])
