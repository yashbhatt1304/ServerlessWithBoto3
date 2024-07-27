import boto3

###########  Creating 2 EC2 Instance  ##########
amiId="ami-062cf18d655c0b1e8"
keyPair="Yash_HV"
def createEC2():
    ec2=boto3.client('ec2')
    res = ec2.create_instances(
        ImageId=amiId,
        MinCount=2,
        MaxCount=2,
        InstanceType='t2.micro',
        KeyName=keyPair
    )
    print(res)
    instance1 = res[0].id
    instance2 = res[1].id
    print(instance1)
    print(instance2)

