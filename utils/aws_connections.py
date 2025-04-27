
import boto3
from utils.config import Config

class AWSConnections:
    def __init__(self):
        self.session = boto3.Session(region_name=Config.AWS_REGION)

    def s3_client(self):
        return self.session.client('s3')

    def dynamodb_client(self):
        return self.session.client('dynamodb')

    def redshift_client(self):
        return self.session.client('redshift-data')

    def cloudwatch_client(self):
        return self.session.client('cloudwatch')
    

