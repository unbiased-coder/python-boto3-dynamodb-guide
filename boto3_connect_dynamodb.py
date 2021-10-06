import boto3_helper

session = boto3_helper.init_aws_session()
dynamodb = session.resource('dynamodb')
print ('Successfully connected to DynamoDB')
table = dynamodb.Table('unbiased_coder')
print ('Found table: ', table.table_name)
print ('Table Item Count: ', table.item_count)
print ('Table Key schema: ', table.key_schema)
