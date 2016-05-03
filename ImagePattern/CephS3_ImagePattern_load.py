import boto
import boto.s3.connection

access_key = 'YCK52X2AE07AG5U5KS8Q'
secret_key = 'HrVhOq9sIk/kHexLgZZM16vuB7sn4Kn3Y8865swO'

conn = boto.connect_s3(
	aws_access_key_id = access_key,
	aws_secret_access_key = secret_key,
	host = '192.168.15.200',
	port = 80,
	is_secure=False,
	calling_format = boto.s3.connection.OrdinaryCallingFormat(),
	)

list = ['beige.jpg', 'blue.jpg', 'green.jpg', 'pink.jpg', 'white.jpg'];

bucket = conn.create_bucket('image-pattern')

bucket = conn.get_bucket("image-pattern")

#print "list[0]: ", list[0]
#print "list: ", list
print "Adding Pattern to Bucket: image-pattern"
for pattern in list:
  file = "images/"+pattern
  key = bucket.new_key(pattern)
  key.set_contents_from_filename(file)
  print "Adding Pattern: ", file

# LIST BUCKET CONTENT
for key in bucket.list():
        print "{name}\t{size}\t{modified}".format(
                name = key.name,
                size = key.size,
                modified = key.last_modified,
                )


#key = bucket.new_key('/etc/hosts')
#key.set_contents_from_filename('/etc/hosts')
#
#for key in bucket.list():
#        print "{name}\t{size}\t{modified}".format(
#                name = key.name,
#                size = key.size,
#                modified = key.last_modified,
#                )
