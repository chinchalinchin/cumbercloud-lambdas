import os
import json

import boto3


def lambda_handler(event, context):
    raw = event.get('body', None)
    
    if raw is not None:
        body = json.loads(raw)
        
        print(body)

    response = {
        "mesasge": "Email Sent"
    }
    
    return {
          "isBase64Encoded": False,
          "statusCode": 200,
          "headers": {
              "Access-Control-Allow-Headers": "Content-Type",
              "Allow": "OPTIONS, POST",
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Methods": "OPTIONS,POST",
              "Content-Type": "application/json"
          },
          "body": json.dumps(response)
    } 