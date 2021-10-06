import boto3_helper

session = boto3_helper.init_aws_session()
dynamodb = session.resource('dynamodb')
print ('Successfully connected to DynamoDB')
table = dynamodb.Table('unbiased_coder')
item = {
    'name': 'Unbiased Coder X', 
    'id': 5
}
table.put_item(Item=item)
print ('Successfully added item: ', item)

