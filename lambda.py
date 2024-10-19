import os
import boto3
import gzip
import shutil

def event_handler(event, context):

    s3 = boto3.client('s3', region_name='us-west-2')

    bucket_name = 'tarun-test-12345678'

    directories = [
        s3.list_objects_v2(Bucket=bucket_name, Prefix='fandom/'),
        s3.list_objects_v2(Bucket=bucket_name, Prefix='game-changers/esports-data/'),
        s3.list_objects_v2(Bucket=bucket_name, Prefix='vct-challengers/esports-data/'),
        s3.list_objects_v2(Bucket=bucket_name, Prefix='vct-international/esports-data/')
    ]

    for directory in directories:
        if 'Contents' in directory:
            for obj in directory['Contents']:
                key = obj['Key']
                print(f"Processing {key}")

                if key.endswith('.gz'):
                    local_temp_path = '/tmp/' + os.path.basename(key)
                    s3.download_file(bucket_name, key, local_temp_path)

                    unzipped_key = key[:-3]

                    unzipped_temp_path = local_temp_path[:-3]  # Remove the .gz from temp path
                    with gzip.open(local_temp_path, 'rb') as f_in:
                        with open(unzipped_temp_path, 'wb') as f_out:
                            shutil.copyfileobj(f_in, f_out)

                    s3.upload_file(unzipped_temp_path, bucket_name, unzipped_key)

                    # Delete the original .gz file from S3
                    print(f"Deleting original .gz file: {key}")
                    s3.delete_object(Bucket=bucket_name, Key=key)
                    print(f"Deleted: {key}")

                    # Optionally, delete the temporary files
                    os.remove(local_temp_path)
                    os.remove(unzipped_temp_path)

                else:
                    print(f"File {key} is not a gzip file, skipping.")
        else:
            print("No files found in the directory")

    return {
        "statusCode": 200,
        "body": "Executed Successfully"
    }
