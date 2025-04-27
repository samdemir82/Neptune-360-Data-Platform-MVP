
class Config:
    AWS_REGION = "us-east-1"
    S3_LANDING_BUCKET = "neptune360-landing"
    S3_CLEAN_BUCKET = "neptune360-clean"
    REDSHIFT_DB = "neptune360_redshift"
    REDSHIFT_USER = "admin"
    REDSHIFT_PASSWORD = "password"
    REDSHIFT_ENDPOINT = "redshift-cluster.xxxx.region.redshift.amazonaws.com"
    DYNAMODB_ALERTS_TABLE = "meter_alerts"
    AURORA_DB = "neptune360_metadata"
