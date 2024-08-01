import json
import boto3
from datetime import datetime, timezone, timedelta

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # TODO implement
    InstnaceList = getInstances()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def getInstances():
    list=[]
    instances = ec2.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] == 'running':
                launchTime = instance['LaunchTime']
                thresholdTime = datetime.now(timezone.utc) - timedelta(minutes=5)
                if (thresholdTime < launchTime):
                    list.append(instance['InstanceId'])
                    print(f"Instance {instance['InstanceId']} created after {thresholdTime}")
                    attachTags(instance['InstanceId'], launchTime)
    return list
    

def attachTags(instanceId, time):
    ec2.create_tags(
        Resources=[instanceId],
        Tags=[{'Key': 'Launch_Time', 'Value': str(time)},
        {'Key': 'CreatedBy', 'Value': "Auto-Tag-Lambda-By-Yash"}]
        )
    print(f"Tags attached to {instanceId}")
    