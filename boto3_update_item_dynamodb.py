import boto3_helper

session = boto3_helper.init_aws_session()
dynamodb = session.resource('dynamodb')
print ('Successfully connected to DynamoDB')
table = dynamodb.Table('unbiased_coder')
item = {
    'name': 'Unbiased Coder X', 
    'id': 5,
}
db_item = table.update_item(
                            Key=item, 
                            UpdateExpression="set #nickname_attr = :nickname_val",
                            ExpressionAttributeValues={
                                ':nickname_val': 'unbiasedCoder'
                            },
                            ExpressionAttributeNames={
                                '#nickname_attr': 'nickname'
                            },
                            ReturnValues="UPDATED_NEW"
)
print ('Successfully updated item: ', item)
