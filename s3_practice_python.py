import os
from dotenv import load_dotenv
load_dotenv()
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_BUCKET_NAME = os.environ.get("AWS_BUCKET_NAME")

import requests
import boto3

# --------------------------------------------------------------------------------------------

# pip install boto3
# pip install python-dotenv

# --------------------------------------------------------------------------------------------

# Normal S3 with key required
s3 = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# --------------------------------------------------------------------------------------------

bucket_name = AWS_BUCKET_NAME
all_objects = s3.list_objects(Bucket=bucket_name)
all_object_contents = all_objects['Contents']
print(all_objects)
print(all_object_contents)
# response = s3.list_objects_2(Bucket=bucket_name)
# files = response.get('Contents')
# print(files)

for file in all_object_contents:
    print(file['Key'])

# -----------------------------------------CRUD ----------------------------------------------

# READ ---------------------------------------------------------------------------------------

# # List all buckets
buckets_resp = s3.list_buckets()
for bucket in buckets_resp["Buckets"]:
    print(bucket)

# # List all objects in a bucket
response = s3.list_objects_v2(Bucket=bucket_name)
for obj in response["Contents"]:
    print(obj)

# # Download File
s3.download_file(bucket_name, "joshua_becker_resume.pdf", "Joshua Becker Resume Downloaded from S3.pdf")
# s3.download_file(bucket_name, "burger.jpg", "this burger was downloaded from s3.jpg")

# CREATE -------------------------------------------------------------------------------------

# # Create a New Bucket
# bucket_location = s3.create_bucket(ACL="public-read", Bucket="new-bucket-created-via-boto3")
# print(bucket_location)

# CREATE / UPDATE FILE -----------------------------------------------------------------------

# Upload file to bucket [Show with public-read, and without it too]
# with open("./Joshua Becker - Software Engineer 2023 Resume.pdf", "rb") as f:
#     print(f.name)
#     s3.upload_fileobj(f, bucket_name, "joshua_becker_resume.pdf", ExtraArgs={"ACL": "public-read"})

# with open("./burger.jpg", "rb") as f:
#     print(f.name)
#     s3.upload_fileobj(f, bucket_name, "burger.jpg", ExtraArgs={"ACL": "public-read"})

# DELETE -------------------------------------------------------------------------------------

# Delete File
# obj = bucket.Object(key='burger.jpg') 
# obj.delete()




# OTHER / NOTES ------------------------------------------------------------------------------

# # Download File with reference
# with open("downloaded_burger.jpg", "wb") as f:
#     s3.download_fileobj(bucket_name, "burger.jpg", f)

# # Presigned URL to give limited access to an unauthorized user
# url = s3.generate_presigned_url(
#     "get_object", Params={"Bucket": bucket_name, "Key": "burger.jpg"}, ExpiresIn=30
# )
# print(url)

# # Copy object
# response = s3.copy_object(
#     ACL="public-read",
#     Bucket="new-copy-destination-123",
#     CopySource=f"/{BUCKET_NAME}/burger.jpg",
#     Key="CopiedBurger.jpg",
# )
# print(response)

# # Get Object
# response = s3.get_object(Bucket=bucket_name, Key="burger.jpg")
# print(response)

# with open("./burger.jpg", "rb") as f:
#     s3.put_object








# NOTES below--------------------------------------------------------------------------

# BUCKET_NAME = "boto-tutorial-bucket"

# s3 = boto3.client("s3")

# # List all buckets
# buckets_resp = s3.list_buckets()
# for bucket in buckets_resp["Buckets"]:
#     print(bucket)

# # List all objects in a bucket
# response = s3.list_objects_v2(Bucket=BUCKET_NAME)
# for obj in response["Contents"]:
#     print(obj)

# # Upload file to bucket [Show with public-read, and without it too]
# with open("./burger.jpg", "rb") as f:
#     print(f.name)
#     s3.upload_fileobj(f, BUCKET_NAME, "burger.jpg", ExtraArgs={"ACL": "public-read"})

# # Download File
# s3.download_file(BUCKET_NAME, "burger.jpg", "downloaded_burger.jpg")

# # Download File with reference
# with open("downloaded_burger.jpg", "wb") as f:
#     s3.download_fileobj(BUCKET_NAME, "burger.jpg", f)

# # Presigned URL to give limited access to an unauthorized user
# url = s3.generate_presigned_url(
#     "get_object", Params={"Bucket": BUCKET_NAME, "Key": "burger.jpg"}, ExpiresIn=30
# )
# print(url)


# # Create Bucket
# bucket_location = s3.create_bucket(ACL="public-read", Bucket="new-copy-destination-123")
# print(bucket_location)

# # Copy object
# response = s3.copy_object(
#     ACL="public-read",
#     Bucket="new-copy-destination-123",
#     CopySource=f"/{BUCKET_NAME}/burger.jpg",
#     Key="CopiedBurger.jpg",
# )
# print(response)

# # Get Object
# response = s3.get_object(Bucket=BUCKET_NAME, Key="burger.jpg")
# print(response)








# If using a public S3 - no key required, must need unsigned- ------------------------------------------------------------------

# Making a bucket public
# {
#     "Version": "2012-10-17",
#     "Id": "Policy1664768163631",
#     "Statement": [
#         {
#             "Sid": "Stmt1664768156196",
#             "Effect": "Allow",
#             "Principal": "*",
#             "Action": "s3:GetObject",
#             "Resource": "arn:aws:s3:::s3practiceboto3/*"
#         }
#     ]
# }

# from botocore import UNSIGNED
# from botocore.client import Config
# s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED)) # public s3


# , region_name = 'us-west-2'

# s3.connect_s3()


# Creating the low level functional client
# client = boto3.client(
#     's3', aws_access_key_id = 'AKIA46SFIWN5AMWMDQVB', aws_secret_access_key = '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', region_name = 'ap-south-1'
# )
