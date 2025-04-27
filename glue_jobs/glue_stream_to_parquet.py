
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType, TimestampType
from utils.config import Config

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

schema = StructType()\
    .add("meter_id", StringType())\
    .add("usage", DoubleType())\
    .add("pressure", DoubleType())\
    .add("timestamp", TimestampType())

# Load raw JSON from landing zone
raw_dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://" + Config.S3_LANDING_BUCKET]},
    format="json"
)

# Transform
raw_df = raw_dyf.toDF()
parsed_df = raw_df.select("meter_id", "usage", "pressure", "timestamp")

# Save as Parquet to clean zone
parsed_df.write.partitionBy("meter_id").format("parquet").mode("append").save("s3://" + Config.S3_CLEAN_BUCKET)