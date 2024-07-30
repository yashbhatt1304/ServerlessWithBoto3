import json
import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')

currentDate = datetime.now(timezone.utc)
print("Today's date is", currentDate)
thresholdDate = (currentDate - (timedelta(days=7)))
print("Threshold date is", thresholdDate)


def lambda_handler(event, context):
    bucket = event['bucket']
    try:
        modifyDate=listObjectsInS3(bucket)
    except Exception as e:
        print(e)
        raise e

def listObjectsInS3(bucket):
    response = s3.list_objects_v2(Bucket=bucket)
    content=[i for i in response['Contents']]
    print(content)
    for data in content:
        key = data['Key']
        keyDate = data['LastModified']
        print(f"Object: {key} and Modified Date: {keyDate}")
        if (keyDate<thresholdDate):
            deleteObject(key, bucket)

def deleteObject(objKey, bucketName):
    s3.delete_object(
    Bucket=bucketName,
    Key=objKey,)
    print(f"Deleting the Object: {objKey}, as it passes retention period date.")