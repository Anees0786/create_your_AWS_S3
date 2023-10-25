# create_your_AWS_S3

# Amazon S3 Bucket Creation Script

This Python script, designed for CGI, allows users to create an Amazon S3 bucket.

## Prerequisites

1. Install the `boto3` library:

    ```bash
    pip install boto3
    ```

2. Configure your AWS credentials:

    Replace `'ACCESS_KEY'` and `'SECRET_KEY'` in the script with your actual AWS access key and secret key.

## Usage

1. Configure your web server to handle CGI scripts.

2. Place the script in the CGI directory of your web server.

3. Access the script through your web browser, providing the bucket name as a parameter:

    ```
    http://your-server/cgi-bin/s3_bucket_create.py?bucket_name=YourBucketName
    ```

    Replace `your-server` with the address of your web server and `YourBucketName` with the desired S3 bucket name.

**Note:** Ensure that you have Python 3 installed on your system and have internet connectivity to create the S3 bucket.
