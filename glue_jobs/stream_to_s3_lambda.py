
import json
import boto3
from utils.config import Config

s3 = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        payload = json.loads(record['body'])
        device_id = payload['meter_id']
        timestamp = payload['timestamp']

        key = f"meter_readings/{device_id}/{timestamp}.json"
        s3.put_object(Bucket=Config.S3_LANDING_BUCKET, Key=key, Body=json.dumps(payload))

    return { 'statusCode': 200 }