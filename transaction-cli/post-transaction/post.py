import json
import boto3

dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table('Transactions')

def lambda_handler(event, context):
    # TODO implement
    table.put_item(Item={"transactionId":"166",
        "type":"Purchase"
    })
    return  {
        'statusCode': 200,
        'body': json.dumps('Done')
            }
