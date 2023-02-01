import boto3 as boto3
from boto3.dynamodb.conditions import Key

dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                               aws_access_key_id='ASIAX2KHRAJAW2ITH2MJ',
                               aws_secret_access_key='1lLl/Jw0Fer4ixg1tAxT13TouifhM9UEdFzaa5S4',
                               aws_session_token='IQoJb3JpZ2luX2VjEEkaCWV1LXdlc3QtMSJGMEQCIBZ6h3L3r+XgDNQNdcZ6lBKRCmaLlJ5P0Nqx7hxoqZ7uAiAxD9K81odhLw5soMek+vVDcM0sDs7oQo6oUVBgjGTiiSqkAwjC//////////8BEAMaDDUzNzU1Nzc5NTM5MyIMT2NbeMyH1pLxPOArKvgCmhJNVZWimy5Hizw62W/TPoZx21ZHReoV/B0fmWypK9OCcNC0cdhrLRfDv7O0eFOOCxWDYgG/mQXAAx6lCMagCRcG+bDODzSvmCriJyyh4MfeZJtQS7gy1W5qABIsGnEznLtszjDe8ciBLgIAqzCs9WTMg1iOHU909ks2/uFXrMfJlJeGI3p69SaKI/pNIfYMsVaMrV9BmsFt8cAEfqIoJpchtL7xaj0qoizrA29Uww61NJGUqX21ULHIskRflvLKNjj3zQBjqT9a5ebZUY8sHn50Ej2qetPvJdmv7me/iGPTPOeGuVKgGToubQciZAWIv1snGI0qyNiGvzAfbz5IUoAaHLNT1oVJrkurC0q5u3VArSdmGFpJAZzTImDMBBHoQqMbmJcGMVXkaTdhpzRA4/3Pk7EdUfveVyHURaGkRbxnpAFpGiuJpQJDu4EzU7B22pQVCjQ4GC7QdkB7bfqE2UmM58FYH+XauTYLpMpewaHj0/k3HzWlWzDFrOqeBjqnAVbN9X/F4jg9XLkdbV13B3flmYryKBdzJKc3MFO3/uuTt2b3ae0M5cG0MPJuU05yNwjTSTtg1ldJ37T7TCczkXFjbMIvnARWSC5ksqek0YhNvI6V8LjrdQNw0CnujV+63H+bvQWpO2oS7iPFpelvEzuNaC6KhpvpGwKn5LQ4srdg1LP4UCatnzxPVNBXK5ogzygl54WmQBYfJSzEhM1JRD2g7MCMyVTj')
__connected_table__ = dynamo_client.Table("freshers-example")

print(__connected_table__.table_status)
print("\n")
