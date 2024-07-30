import json
import boto3
from datetime import datetime, timezone, timedelta

ec2=boto3.client('ec2')

currentDate = datetime.now(timezone.utc)
print("Today's date is", currentDate)
thresholdDate = (currentDate - (timedelta(days=7)))
print("Threshold date is", thresholdDate)

def lambda_handler(event, context):
    volIds = event["VolumeIds"]
    for vol in volIds:
        descSnapshots(vol)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def descSnapshots(volume):
    response = ec2.describe_snapshots(
        Filters=[
            {'Name': 'volume-id', 'Values': [volume]}
            ]
    )
    date = response['ResponseMetadata']['HTTPHeaders']['date']
    format = '%a, %d %b %Y %H:%M:%S'
    formatedDate = datetime.strptime(date[:-4], format) 
    print(f"VolumeId: {volume} created on {formatedDate}")

