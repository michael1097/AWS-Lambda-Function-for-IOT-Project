import math
import boto3
from decimal import Decimal

# Get dynamodb resource
dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):
   
    # JSON object from IoT core has timestamp field
    if 'timestamp' in event:
        # Get table
        table = dynamodb.Table('Iot_team_table')
        
        # Put item into table
        response = table.put_item(
        Item={
        'app_id': "IoT", # Primary key
        'timestamp': event['timestamp'], # Sort key
        'sensor': Decimal(str(event['sensor']))
        }
        )
        
        # Print put_item response
        print(response)
        
        # Get recently written item
        response = table.get_item(
        Key={'app_id': "IoT", 'timestamp': event['timestamp']}
        )
        
        # Print get_item response
        print(response)
        
        # Print table scan results
        #print(table.scan()['Items'])
        
        
        # Return
        return "DB updated"
    
    
