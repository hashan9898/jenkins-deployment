import boto3
region = 'ap-south-1'
instances = ['i-02083b819c731ec2d']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))
