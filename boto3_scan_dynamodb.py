import boto3_helper

session = boto3_helper.init_aws_session()
dynamodb = session.resource('dynamodb')
print ('Successfully connected to DynamoDB')
table = dynamodb.Table('unbiased_coder')
res = table.scan()
print ('Scan results from table unbiased_coder: ')
for item in res['Items']:
    print (item['name'], end='')
    if 'nickname' in item:
        print (' has nickname: ', item['nickname'])
    else:
        print ('')
