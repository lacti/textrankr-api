import json
from textrankr import TextRank


def summerize(event, context):
    if not event['body']:
        return {
            "statusCode": 400,
            "body": ""
        }
        
    textrank = TextRank(event['body'])

    response = {
        "statusCode": 200,
        "body": textrank.summarize()
    }
    return response

