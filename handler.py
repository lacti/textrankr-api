import json
import os
from textrankr import TextRank, ApiPhraser


phraser_api_url = os.environ['PHRASER_API_URL']


def summerize(event, context):
    if not event['body']:
        return {
            "statusCode": 400,
            "body": ""
        }

    textrank = TextRank(event['body'], phraser=ApiPhraser(
        api_url=phraser_api_url).phrases)

    response = {
        "statusCode": 200,
        "body": textrank.summarize(),
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST"
        }
    }
    return response
