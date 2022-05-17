from ctypes import Union
import json
import os
import pprint

import requests
import jwt
import boto3 

from jwt.algorithms import RSAAlgorithm
from botocore.exceptions import ClientError

ACCOUNT=os.environ['ACCOUNT']
API=os.environ['API']
USERPOOL = os.environ['USERPOOL']
CLIENT = os.environ['CLIENT']
APPLICATION = os.environ['APPLICATION']
REGION = os.environ['REGION']

def key_url() -> str:
    return 'https://cognito-idp.{}.amazonaws.com/{}/.well-known/jwks.json'.format(REGION, USERPOOL)

def lambda_handler(event: dict, context: dict):
    pprint.pprint(event)
    pprint.pprint(context)
    token = event['authorizationToken'].split(' ')[-1]
    header = jwt.get_unverified_header(token)

    keys = requests.get(key_url()).json()
    kid = header['kid']

    jwk = find_key(keys, kid)

    if jwk is not None:
        public_key = RSAAlgorithm.from_jwk(json.dumps(jwk))

        try:
            decoded = decode_token(token, public_key)
            pprint.pprint(decoded)

        except Exception as e:
            return

def policy(context: dict, deny: bool) -> dict:
    return {
        "principalId": context['authorizer']['principalId'],
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
            {
                "Action": "execute-api:Invoke",
                "Effect": "Deny" if deny else "Allow",
                "Resource": f"arn:aws:execute-api:{REGION}:{ACCOUNT}:{API}/*"
            }
            ]
        }
    }

def find_key(keys, kid) -> Union[dict,None]:
    for key in keys:
        if key['kid'] == kid:
            return key
    return None

def decode_token(token: str, publicKey: str)->dict:
    return jwt.decode(token, publicKey, algorithms=['RS256'], audience=CLIENT)
