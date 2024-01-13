
1. Create AWS S3 Bucket
In this case, I'll use `my-content-engine`.


2. Create an IAM Policy

Use the following and replease `my-content-engine` with your bucket name.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets"
            ],
            "Resource": "arn:aws:s3:::*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:*Object*",
                "s3:ListBucket",
                "s3:GetBucketLocation",
                "s3:ListBucketMultipartUploads",
                "s3:ListBucketVersions"
            ],
            "Resource": [
                "arn:aws:s3:::my-content-engine"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:*Object*",
                "s3:ListMultipartUploadParts",
                "s3:AbortMultipartUpload"
            ],
            "Resource": [
                "arn:aws:s3:::my-content-engine/*"
            ]
        }
    ]
}
```

3. Attach Policy to IAM User or Group