#!/usr/bin/python
# =====================================================================
#        File:  AWSS3_ImagePattern_load.py
#    Location:  https://github.com/sadubois/ceph-s3-api.git
#   Launguage:  Python
#    Category:  s3-api-demo
#     Purpose:  Demonstrates Red Hat Ceph Storage RadowsGw/S3 Interface
#      Author:  Sacha Dubois, Red Hat
#
# Copyright (c) 2010 - 2012 Red Hat, Inc.
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
# Red Hat trademarks are not licensed under GPLv2. No permission is
# granted to use or replicate Red Hat trademarks that are incorporated
# in this software or its documentation.
# =====================================================================
# 18.04.2015  Sacha Dubois  new
# =====================================================================

import boto3
import uuid
import sys
import os

# --- CHECK S3 ACCESS_KEY ---
if os.environ.has_key("ACCESS_KEY"):
        access_key = os.environ['ACCESS_KEY']
else:
        print "ERROR: environment variable ACCESS_KEY is not set"
        print "  ie. export ACCESS_KEY=\"F8T4P40OCX8KD96SVDX0\""
        sys.exit(0)

# --- CHECK S3 SECRET_KEY ---
if os.environ.has_key("SECRET_KEY"):
        secret_key = os.environ['SECRET_KEY']
else:
        print "ERROR: environment variable SECRET_KEY is not set"
        print "  ie. export SECRET_KEY=\"mSTz7NNOpsn27cc03Rfez+FpHdV2lHn4BinLGG3N\""
        sys.exit(0)

print "# AWS RADOSGW7S3 CONECCTION DETAILLS"
print "SECRET_KEY='"+secret_key+"'"
print "ACCESS_KEY='"+access_key+"'"
print ""


from boto3.session import Session

session = Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key)
s3 = session.resource('s3', region_name='us-west-2')

bucket_name = "image-pattern"

# DELETE image-pattern BUCKET AND OBJECTS IF AVAILABLE
bucket = s3.Bucket(bucket_name)
if bucket in s3.buckets.all(): 
  print "=> Cleanup Previous Bucket: image-pattern with objects"
  for obj in bucket.objects.all():
    key = s3.Object(bucket.name, obj.key)
    key.delete()
  bucket.delete()


# CREATE BUCKET
print "=> Create Bucket: image-pattern"
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2'
    },
)

# LOAD IMAGES PATTERNS
list = ['beige.jpg', 'blue.jpg', 'green.jpg', 'pink.jpg', 'white.jpg'];
print "=> Adding Pattern to Bucket: image-pattern"
for pattern in list:
  file = "images/"+pattern
  s3.Object(bucket_name, "Background/"+pattern).put(Body=open(file, 'rb'))
  print "  Adding Pattern: ", file

# --- LIST BUCKETS AND OBJECTS ---
bucket = s3.Bucket(bucket_name)
print "\n=> List Objects in Bucket: "+bucket.name
for obj in bucket.objects.all():
    key = s3.Object(bucket.name, obj.key)
    print "  %s %s" % (str(obj.last_modified), str(key.key))


# ---------------------------------------------------------------------------


sys.exit(0)
#for bucket in s3_resource.buckets.all():
#    for obj in bucket.objects.all():
#        key = s3_resource.Object(bucket.name, obj.key)
#	key.delete()
#
sys.exit(0)

s3 = boto3.resource('s3')

bucket_name = "image-pattern"
bucket = s3.Bucket(bucket_name)
for obj in bucket.objects.all():
        print(obj.key)

# LIST AVAILABLE BUCKETS
#for bucket in s3.buckets.all():
#    print "Bucket: "+bucket.name
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

# --- LIST BUCKETS AND OBJECTS ---
bucket = s3.Bucket(bucket_name)
print "Bucket: "+bucket.name
for obj in bucket.objects.all():
    key = s3.Object(bucket.name, obj.key)
    print "  %s %s" % (str(obj.last_modified), str(key.key))


