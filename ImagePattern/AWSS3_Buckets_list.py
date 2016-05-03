#!/usr/bin/python
# =====================================================================
#        File:  AWSS3_Buckets_list.py
#    Location:  https://github.com/sadubois/s3-api-demo.git
#   Launguage:  Python
#    Category:  s3-api
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

print "# AWS RADOSGW7S3 CONECCTION DETAILS"
print "ACCESS_KEY='"+access_key+"'"
print "SECRET_KEY='"+secret_key+"'"
print ""

from boto3.session import Session

session = Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key)
s3 = session.resource('s3', region_name='us-west-2')

# --- LIST BUCKET AND OBJECTS ---
for bucket in s3.buckets.all():
    print "Bucket: "+bucket.name
    for obj in bucket.objects.all():
        key = s3.Object(bucket.name, obj.key)
        print "  %s %s" % (str(obj.last_modified), str(key.key))

sys.exit(0)
