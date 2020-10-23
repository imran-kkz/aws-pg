import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Init table
table = dynamodb.Table('users')

# Put item in the DynamoDB table.
table.put_item(
   Item={
        'username': 'janedoe',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
    }
)
