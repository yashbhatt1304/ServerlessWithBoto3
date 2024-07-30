import boto3
from datetime import datetime, timezone, timedelta

ec2=boto3.client('ec2')

currentDate = datetime.strptime(datetime.today().strftime('%d %b %Y %H:%M:%S'), '%d %b %Y %H:%M:%S')
print("Today's date is", currentDate)
thresholdDate = (currentDate - (timedelta(days=1)))
print("Threshold date is", thresholdDate)

def lambda_handler(event, context):
    volIds = event["VolumeIds"]
    for vol in volIds:
        # createSnapshots(vol)
        descSnapshots(vol)


def descSnapshots(volume):
    response = ec2.describe_snapshots(
        Filters=[
            {'Name': 'volume-id', 'Values': [volume]}
            ]
    )
    # print(response)
    for snapshot in response['Snapshots']:
        date = snapshot["StartTime"].replace(tzinfo=None)
        # format = '%a, %d %b %Y %H:%M:%S'
        # formatedDate = datetime.strptime(date[:-4], format) 
        print(f"SnapshotId: {snapshot['SnapshotId']} created on {date}")
        if (date<thresholdDate):
            deleteSnapshot(snapshot['SnapshotId'])
            print(f"Snapshot {snapshot['SnapshotId']} has passed the retention period.")

def createSnapshots(volume):
    ec2.create_snapshot(
        VolumeId=volume,
        Description=f"Snapshot of volume {volume} by Yash"
            )

def deleteSnapshot(snapshot):
    ec2.delete_snapshot(SnapshotId=snapshot)
    print(f"Deleted {snapshot}")