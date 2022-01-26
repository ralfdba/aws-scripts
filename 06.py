"""
Eliminar snapshot antiguos de una región en particular
"""
import boto3
import datetime

region = 'us-east-2'
cliente = boto3.client('ec2',region_name=region)
snapshot = cliente.describe_snapshots(OwnerIds=['self'])

for s in snapshot['Snapshots']:
    a = s['StartTime']
    fecha_sns = a.date()
    fecha_actual = datetime.datetime.now().date()
    diferencia = fecha_sns - fecha_actual

    if diferencia.days > 30:
        id = s['SnapshotId']
        cliente.delete_snapshot(SnapshotId=id)
    else:
        print("No se elimina %s" % str(id))

