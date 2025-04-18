import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Initialize
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read from S3
datasource = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://your-bucket/input/"]},
    format="csv",
    format_options={"withHeader": True}
)

# Transform
transformed = ApplyMapping.apply(frame=datasource, mappings=[
    ("CustomerID", "string", "CustomerID", "string"),
    ("TransactionAmount", "double", "TransactionAmount", "double"),
    ("Timestamp", "string", "Timestamp", "timestamp")
])

# Write to Redshift
glueContext.write_dynamic_frame.from_jdbc_conf(
    frame=transformed,
    catalog_connection="your-redshift-conn",
    connection_options={"dbtable": "customer_transactions", "database": "yourdb"},
    redshift_tmp_dir="s3://your-bucket/temp/"
)

job.commit()
