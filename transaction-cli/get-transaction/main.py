import json
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Transactions')
    data = table.scan()['Items']
    print(data)
    response = table.get_item(
        Key={
            'transactionId': '55'
        })
    return {
        "statusCode": 200,
        "body": json.dumps(data)
    }

