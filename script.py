import boto3
import json
from datetime import datetime, timedelta

# Creating connection to s3
s3 = boto3.client('s3', region_name='ap-south-1', aws_access_key_id='xxxxxxxx', aws_secret_access_key='xxxxxxxxxxx')
## Access and secret keys is not required when using instance IAM roles
#s3 = boto3.client('s3', region_name='us-east-1')

s3_bucket = s3.list_buckets()

s3_resosurce =  boto3.resource('s3',region_name='ap-south-1', aws_access_key_id='xxxxxxx',aws_secret_access_key='xxxxxxxx')

cloudwatch = boto3.client('cloudwatch',region_name='ap-south-1', aws_access_key_id='xxxxxxx',aws_secret_access_key='xxxxxxxxxxxxx')

for bucket in s3_bucket["Buckets"]:
   print("Bucket name is: %s" % bucket['Name'])
   print("Bucket creation date is: %s" % bucket['CreationDate'])
   bucket_object = s3_resosurce.Bucket(bucket['Name'])
   object_count = sum(1 for _ in bucket_object.objects.all())
   print("Number of Object in Bucket: %d" % object_count)
   cloudwatch_response = cloudwatch.get_metric_statistics(
     Namespace="AWS/S3",
       MetricName="BucketSizeBytes",
     Dimensions=[
         {
         "Name": "BucketName",
           "Value": bucket['Name']
           },
           {
           "Name": "StorageType",
           "Value": "StandardStorage"
           }
         ],
         StartTime=datetime.now() - timedelta(days=1),
         EndTime=datetime.now(),
         Period=86400,
         Statistics=['Average']
           )
   bucket_size_bytes = cloudwatch_response['Datapoints'][-1]['Average']
   print("Bucket Size is: %d" % bucket_size_bytes)
   ## 1 GB s3 storage cost is 0.000000610351562 $ in mumbai region_name
   bucket_cost = bucket_size_bytes * 0.000000610351562
   print("Bucket cost is: %d" % bucket_cost)
