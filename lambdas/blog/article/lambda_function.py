import json
import os
import pprint

import boto3 
from botocore.exceptions import ClientError

def lambda_handler(event, context):

    pprint.pprint(event)

    body = event.get('body', None)

    if body is not None:
        response = json.loads(body)
        try:
            response = {
                'something'
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
              "Allow": "OPTIONS, GET, POST",
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Methods": "OPTIONS,GET,POST",
              "Content-Type": "application/json"
          },
          "body": json.dumps(response)
    } 