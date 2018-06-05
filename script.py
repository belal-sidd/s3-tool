from __future__ import print_function
import boto3
import json

# Creating connection to s3
s3 = boto3.client('s3', region_name='ap-south-1', aws_access_key_id='xxxxxxxxxxxx', aws_secret_access_key='xxxxxxxxx')
## Access and secre keys is not required when using instance IAM roles
#s3 = boto3.client('s3', region_name='us-east-1')

s3_bucket = s3.list_buckets()

s3_resosurce =  boto3.resource('s3',region_name='ap-south-1', aws_access_key_id='AKIAJ5UOF2E7SQSPLW4Q', aws_secret_access_key='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')
size = 0
for bucket in s3_bucket["Buckets"]:
	print("Bucket name is: %s" % bucket['Name'])
	print("Bucket creation date is: %s" % bucket['CreationDate'])
	bucket_object = s3_resosurce.Bucket(bucket['Name'])
	size = sum(1 for _ in bucket_object.objects.all())
	print("Number of Object in Bucket: %d" % size)
