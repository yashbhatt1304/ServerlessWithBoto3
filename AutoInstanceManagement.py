import boto3

###########  Creating 2 EC2 Instance  ##########
amiId="ami-062cf18d655c0b1e8"
keyPair="Yash_HV"
def createEC2():
    ec2=boto3.client('ec2')
    res = ec2.run_instances(
        ImageId=amiId,
        MinCount=2,
        MaxCount=2,
        InstanceType='t2.micro',
        KeyName=keyPair
    )
    # print(res)
    return res
instances = createEC2()
print("Successfully launched EC2 Instances")
instance1 = instances['Instances'][0]['InstanceId']
instance2 = instances['Instances'][1]['InstanceId']
print("First Instance: "+instance1)
print("Second Instance: "+instance2)

########### Attaching Tag to EC2 Instances  ###########
def attachTagToInstance():
    ec2=boto3.client('ec2')
    autoStart = ec2.create_tags(
        Resources=[instance1],
        Tags=[
            {'Key': 'Name', 'Value': 'Yash-Auto-Start'},
            {'Key': 'Type', 'Value': 'Auto-Start'}
        ]
    )
    # print(autoStart)
    print("Successfully attached auto start tag")
    autoStop = ec2.create_tags(
        Resources=[instance2],
        Tags=[
            {'Key': 'Name', 'Value': 'Yash-Auto-Stop'},
            {'Key': 'Type', 'Value': 'Auto-Stop'}
        ]
    )
    # print(autoStart)
    print("Successfully attached auto stop tag")
attachTagToInstance()