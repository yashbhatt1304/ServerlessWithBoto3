import boto3
import json

def lambda_handler(event, context):
    # TODO implement
    stopIns = [i['Instances'][0]['InstanceId'] for i in describeInstanceByTag('Auto-Stop')['Reservations']]
    startIns = [i['Instances'][0]['InstanceId'] for i in describeInstanceByTag('Auto-Start')['Reservations']]
    print(stopIns)
    print(startIns)
    stopInstance(stopIns)
    startInstance(startIns)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    

###########  Start Instance  ##########
def startInstance(instances):
    ec2=boto3.client('ec2')
    startResponse = ec2.start_instances(
        InstanceIds=instances,
    )
    print(startResponse)


###########  Stop Instance  ##########
def stopInstance(instances):
    ec2=boto3.client('ec2')
    stopResponse = ec2.stop_instances(
        InstanceIds=instances,
    )
    print(stopResponse)

###########  Getting Instances with specific tags. #########
def describeInstanceByTag(tag):
    ec2=boto3.client('ec2')
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Type',
                'Values': [
                    tag,
                ],
            },
        ],
    )
    return response
