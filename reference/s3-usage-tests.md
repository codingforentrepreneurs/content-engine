
```
python manage.py shell
```



```python
from pprint import pprint
import s3
from cfehome.env import config


AWS_ACCESS_KEY_ID=config("AWS_ACCESS_KEY_ID", default=None)
AWS_SECRET_ACCESS_KEY=config("AWS_SECRET_ACCESS_KEY", default=None)
AWS_BUCKET_NAME=config("AWS_BUCKET_NAME", default=None)


client = s3.S3Client(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        default_bucket_name=AWS_BUCKET_NAME,
    ).client

paginator = client.get_paginator("list_objects_v2")
pag_gen = paginator.paginate(
        Bucket=AWS_BUCKET_NAME,
        Prefix="projects/10/items/46/"
)
for page in pag_gen:
    #print(page.get('Contents'))
    for c in page.get('Contents', []):
        pprint(c)
        # print(c.get('Key'), c.get('filename'))
```