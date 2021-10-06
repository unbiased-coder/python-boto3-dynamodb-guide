import boto3_helper

session = boto3_helper.init_aws_session()
dynamodb = session.resource('dynamodb')
print ('Successfully connected to DynamoDB')
table = dynamodb.Table('unbiased_coder')
item = {
    'name': 'Unbiased Coder X', 
    'id': 5
}
db_item = table.delete_item(Key=item)
print ('Successfully deleted item: ', item)
