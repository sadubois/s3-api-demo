
import boto3
import uuid
import sys

s3 = boto3.resource('s3')

bucket_name = "image-pattern"

bucket = s3.Bucket(bucket_name)
for obj in bucket.objects.all():
        print(obj.key)

response = s3.get_bucket_location(
    Bucket=bucket_name
)

# LIST AVAILABLE BUCKETS
for bucket in s3.buckets.all():
    print "Bucket: "+bucket.name
#    for obj in bucket.objects.all():
#        print(obj.key)

sys.exit(0)

# DELETE BUCKET IF AVAILABLE
bucket = s3.Bucket(bucket_name)
if bucket in s3.buckets.all(): 
	bucket.delete()


# CREATE BUCKET 
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2'
    },
)

# LOAD IMAGES PATTERNS
s3.Object(bucket_name, 'pink.jpg').put(Body=open('images/pink.jpg', 'rb'))

