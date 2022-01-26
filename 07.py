import boto3

ORIGEN = 'us-east-2'
DESTINO = 'us-east-1'

#Origen
cliente_origen = boto3.client('ec2',region_name=ORIGEN)
snapshot = cliente_origen.describe_snapshots(OwnerIds=['self'])
s_organizados = sorted([(s['SnapshotId'],s['StartTime']) for s in snapshot['Snapshots']], key=lambda k:k[1])

if s_organizados is None:
    print("No hay snapshots para mover")
else:
    print("Snapshots organizados %s" % s_organizados)
    ultimo_s = s_organizados[-1][0]
    cliente_destino = boto3.client('ec2',region_name=DESTINO)

    response = cliente_destino.copy_snapshot(SourceSnapshotId=ultimo_s,SourceRegion=ORIGEN,Description="Snapshot copiado desde: "+ORIGEN)

    print(response)