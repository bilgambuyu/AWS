import os
import boto3
import io

def lambda_handler(event, context):
    bucket_name = event['bucket_name']
    file_name = event['file_name']
    
    file = io.BytesIO(bytes(event['file_content'], encoding='utf-8'))
    
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    bucket_object = bucket.Object(file_name)
    bucket_object.upload_fileobj(file)
    
    return {
        'statusCode': 200,
        'body': f"Upload succeeded: {file_name} has been uploaded to Amazon S3 in bucket {bucket_name}"
    }