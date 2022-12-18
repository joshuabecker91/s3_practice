

# If using a public S3 - no key required, must need unsigned

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