import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    response = ec2.describe_volumes( Filters=[ { 'Name': 'tag:Name','Values': ['srv01'] } ] )
    for volume in response['Volumes']:
        ec2.create_snapshot( 
            VolumeId=volume['VolumeId'], 
            Description="Desde lambda",
            TagSpecifications=[
                {
                    'ResourceType':'snapshot',
                    'Tags':[
                        {
                            'Key': 'Name',
                            'Value': 'desde-lambda-sp'
                        }
                    ]
                }
            ]
        )
