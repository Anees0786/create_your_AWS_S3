#!/usr/bin/python3

import boto3
import cgi

def create_s3_bucket(bucket_name):
    # Replace 'ACCESS_KEY' and 'SECRET_KEY' with your AWS credentials
    s3_client = boto3.client('s3', aws_access_key_id='ACCESS_KEY', aws_secret_access_key='SECRET_KEY')

    response_s3 = s3_client.create_bucket(
        ACL='private',
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'
        }
    )

    return response_s3

def main():
    print("Content-type: text/html")
    print()

    form = cgi.FieldStorage()

    # Get the bucket name from the form
    bucket_name = form.getvalue("bucket_name")

    if not bucket_name:
        print("<pre>")
        print("Error: Bucket name not provided.")
        print("</pre>")
        return

    response_s3 = create_s3_bucket(bucket_name)

    print("<pre>")
    print("Below is your Response")
    print(bucket_name)
    print(response_s3)
    print("</pre>")

if __name__ == "__main__":
    main()
