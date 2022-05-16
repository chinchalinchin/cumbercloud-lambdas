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

    if event['httpMethod'] == 'POST':
        body = event.get('body', None)

        if body is not None:
            try:
                response = get_article_table().put_item(
                    Item=json.loads(body)
                )
                status = 200
            except ClientError as e:
                response, status = e, 500
            
        else:
            response = {
                'message' : 'No body in request'
            }
            status = 400

    elif event['httpMethod'] == 'GET':
        params = event.get('queryStringParameters', None)

        if params is not None and params.get('id', None) is not None:
            response = get_article_table().get_item(
                Key = params
            )
            status = 200
        else:
            response = {
                'message': 'No id provided in query parameters'
            }
            status = 400

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