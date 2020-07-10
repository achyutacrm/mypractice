import boto3
import json

ec2 = boto3.client('ec2')
# It is my first programme test
def lambda_handler(event, context):
    response = ec2.describe.availability.zones()
    return{"statuscode":200, "body":json.dumps(response)}   