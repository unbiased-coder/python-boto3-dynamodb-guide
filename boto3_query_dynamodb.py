import boto3_helper
from boto3.dynamodb.conditions import Key

session = boto3_helper.init_aws_session()
dynamodb = session.resource('dynamodb')
print ('Successfully connected to DynamoDB')
table = dynamodb.Table('unbiased_coder')
res = table.query(KeyConditionExpression=Key('name').eq('Unbiased Coder'))
print ('Query results from table unbiased_coder using expression: name="Unbiased Coder"')
for item in res['Items']:
    print (item['name'], item['id'])
