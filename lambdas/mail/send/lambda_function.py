import os
import json

import boto3
from botocore.exceptions import ClientError


sender = os.environ['MailSender']
recipient = os.environ['MailRecipient']

def ses():
    return boto3.client('ses')

def format_msg(body):
    msg = body['message']
    reason = body['reason'] if body['subreason'] == 'None' else body['reason'] + ' ' + body['subreason']
    name = body['first'] + ' ' + body['last']
    email = body['email']
    return f"""
    Dear Cumberland Cloud,

        The reason for this message is: {reason}.

        {msg}

        Please contact me at {email} at your earliest convenience.

    Regards,
    
    {name}
    """

def lambda_handler(event, context):
    raw = event.get('body', None)
    
    if raw is not None:
        body = json.loads(raw)
        try:
            ses_response = ses().send_mail(
                Source=sender,
                Destination={
                    'ToAddresses': [
                        recipient,
                    ],
                    'CcAddresses': [
                        body['email'],
                    ],
                },
                Message={
                    'Subject': {
                        'Data': 'Message for the Cumberland Cloud',
                    },
                    'Body': {
                        'Text': {
                            'Data': format_msg(body),
                        }
                    }
                }
            )
            response, status = ses_response, 200

        except ClientError as e:
            response, status = e, 500

    else:
        response = {
            'message': 'No body in POST'
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