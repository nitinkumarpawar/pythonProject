import boto3 as boto3
from boto3.dynamodb.conditions import Key

dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                               aws_access_key_id='ASIAX2KHRAJAVWC2I65P',
                               aws_secret_access_key='Rf8NJInodIISLGdzpKgL+igxFNktl6/iR9LlU0fn',
                               aws_session_token='IQoJb3JpZ2luX2VjENn//////////wEaCWV1LXdlc3QtMSJGMEQCIEbAU7C2GVFkiapXC9o2gRga4cqH4a4hyadvqqN8tlovAiA4bwNwYWMc2XhajSawXMGwxWEB2JASodQqDLzCwr0abSqbAwhiEAQaDDUzNzU1Nzc5NTM5MyIMZK3/yAIw1dABnkS9KvgCShZ7plVe6UuyvgX5QdHf7vJivbFKl5lG09svRVrnsfjEEwjx4oBHbKZQphdFwv7/toSU7VKQgq84nQSSxOIUqM3Rsjbu9Lw6MJusQS7v4bHabl3sFZyJtCe/qxLAro0NlT1wseBf39dAniGmTHeJl5VrXqimiGnqMYC/WlPXTfNTV+I7yGXmrNOO98vkVtggeW1AtnQU24pTgpE7lU/7KcYiidqr9j0DGwwgKNQP/9sFmAI2a7cNdB0XViuO3U5g72s353GMeslRhOiwT1mJe1RwX28vD8cWSpWqXlVzSVW53NAyxbGoe9DznLKboNPUjf7KZDY6awZPZvDJOa7dTcJNwUJDq+2BR+YxnHO1rqEue1LlAil/CrFcfyQHj8saGY1Bkj/xqoJW13Hsirj9pbxGui+1gUnDw33z7cKtqfnAHrfM+JBfUjm+hY9qqki6K+q7rZlXkyZ/WGFc10hyD9lZrjJYX7A8l1gcVXNHqAWR29mNpknPnjCxi4qfBjqnAdJ/8ubHuFJSt0+wy1dRq3idsRCKz4me24mY1d3f+wci/6HXoexq6h0cU6uLhiD74/gY29UvEtMYywoYS0I8zPP2WvWoKZi5qjYyY+NpGkr25ya2SDGU0kC3OI2e3NHvMauRT5TICDjvPsKziq3HDCGpb6H7BKALgeyuPoIUsN/Q/f9O6RH0buXg+Ku3XI5Ng8Lb2nly3HITUDv0XWL70hpQd1hmZXlq')
__connected_table__ = dynamo_client.Table("freshers-example")

print(__connected_table__.table_status)
print("\n")
