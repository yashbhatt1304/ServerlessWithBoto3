import json
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # TODO implement
    getInstance()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def getInstances(throsholdTime):
    print(f"Fetching List of Instances created after {throsholdTime}")
    
def attachTags(instanceId):
    print(f"Tags attached to {instanceId}")
