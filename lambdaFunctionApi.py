import json
import boto3
from decimal import Decimal

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)

def lambda_handler(event, context):
    # Get dynamodb resource
    dynamodb = boto3.resource('dynamodb')

    if event['resource']=='/energy_consumption':
        # Get table
        table = dynamodb.Table('Iot_team_table')
        # Print table scan results
        body=table.scan()['Items']
        return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(body,cls=JSONEncoder)
        }
        
    if event['resource']=='/last_entry':
        # Get table
        table = dynamodb.Table('Iot_team_table')
        # Print table scan results
        body = table.scan()['Items']
        i=0
        aux = body[0]['timestamp']
        for item in body:
            value = item['timestamp']
            if value > aux:
                aux = value
                last = i
            i+=1
        return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(body[last],cls=JSONEncoder)
        }
        
    if event['resource']=='/max':
        # Get table
        table = dynamodb.Table('Iot_team_table')
        # Print table scan results
        body = table.scan()['Items']
        i=0
        aux = body[0]['sensor']
        for item in body:
            value = item['sensor']
            if value > aux:
                aux = value
                max = i
            i+=1
        return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(body[max],cls=JSONEncoder)
        }
        
    if event['resource']=='/min':
        # Get table
        table = dynamodb.Table('Iot_team_table')
        # Print table scan results
        body = table.scan()['Items']
        i=0
        aux = body[0]['sensor']
        for item in body:
            value = item['sensor']
            if value < aux:
                aux = value
                min = i
            i+=1
        return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(body[min],cls=JSONEncoder)
        }
