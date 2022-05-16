import json
import os
import pprint

import boto3 
from botocore.exceptions import ClientError

APPLICATION = os.environ['APPLICATION']

def get_article_table():
    dynamodb = boto3.resource('dynamodb')
    return dynamodb.Table(f'{APPLICATION}-articles')

def lambda_handler(event, context):

    pprint.pprint(event)

    if event['httpMethod'] == 'GET':
        params = event.get('queryStringParameters', None)

        if params is None:
            response = get_article_table().scan()
            status = 200
        else:
            response = {
                'message': 'TODO: filter by param'
            }
            status = 200

    else:
        response = {
            'message': 'Method Not Allowed'
        }
        status = 405

    return {
          "isBase64Encoded": False,
          "statusCode": status,
          "headers": {
              "Access-Control-Allow-Headers": "Content-Type",
              "Allow": "OPTIONS, GET, POST",
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Methods": "OPTIONS,GET,POST",
              "Content-Type": "application/json"
          },
          "body": json.dumps(response)
    } 