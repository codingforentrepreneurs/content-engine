from dataclasses import dataclass
import boto3
from botocore.client import Config

@dataclass
class S3Client:
    """
    client = S3Client(
        aws_access_key_id="...",
        aws_secret_access_key="...",
        default_bucket_name="...",
    ).client
    """
    aws_access_key_id: str
    aws_secret_access_key: str
    default_bucket_name: str

    def __post_init__(self):
        self.client = self.create_s3_client()

    def create_s3_client(self):
        """
        Create and return a boto3 S3 client
        """
        return boto3.client(
            's3',
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            config=Config(signature_version='s3v4')
        )

    # def list_objects(self):
    # self.client.get_paginator()
    # return