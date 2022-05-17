import json
import os
import pprint

import boto3 
from botocore.exceptions import ClientError

USERPOOL = os.environ['USERPOOL']
CLIENT = os.environ['CLIENT']
APPLICATION = os.environ['APPLICATION']

def lambda_handler(event, context):
    pprint.pprint(event)
    body = event.get('body', None)

    if body is not None:
        parsed_body = json.loads(body)
        pprint.pprint(parsed_body)
        try:
            response ={
                'message': 'something'
            }
            status = 200
        except ClientError as e:
            response, status = e, 500
        
    else:
        response = {
          'message' : 'No body in request'
        }
        status = 400

    return {
          "isBase64Encoded": False,
          "statusCode": status,
          "headers": {
              "Access-Control-Allow-Headers": "Content-Type",
              "Allow": "OPTIONS, POST",
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Methods": "OPTIONS,POST",
              "Content-Type": "application/json"
          },
          "body": json.dumps(response)
    } 