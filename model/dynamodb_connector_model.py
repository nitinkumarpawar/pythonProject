import boto3 as boto3
from boto3.dynamodb.conditions import Key

dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                               aws_access_key_id='ASIAX2KHRAJA73QGYSUS',
                               aws_secret_access_key='WOFqNzqF8EX6DHaTuqcC9UhlRirMrntpAnzcyFcJ',
                               aws_session_token='IQoJb3JpZ2luX2VjEFYaCWV1LXdlc3QtMSJHMEUCIQCKx+mpL/wDh0rLqf71tpWZUxAFmtjVgcYrPu+FvSlZTAIgHBmLeWVySICtlOur80YJwIiNV722OgFkOcn6YpB+z08qpAMIz///////////ARADGgw1Mzc1NTc3OTUzOTMiDA/9+9snYR8xfHDelir4AgNlsV9qDmnX7roe0kCLNTCmzSXiNOlqnAZNYHnULdeR7/P5Pe5VUUJ21DSGOiKj11pnGa0FG0odhSikfnV3iv2roJ0eL0J4Po2yZX0SJHgqHzqxXYQFK2+d/YfCWIQoqaKHbWOmo4F3IFb39G60pISucp50svn3A4vnXMVl47eHIsdplb64V9UHKZKpELBxPFHl33ZrKHlCBY5vaUesb+zZUX/qei1svj8MlSa9VI1gukeeYoYLZidbyzwP7zvnRCmDkRba3FyHBA6NdORN9Xs+WN/TFLHBDbXIl7rsB8ApQqp4lg2ed7aY16VOOaZOxI3tUowCqy/5jeIZmhYjft6Of41WvBuzFMfVlq3c8NyQPQZ5RIrqjjrJXXG6goosiuTasR5f0gZvcR7X4oq63PGdOy+IROY+dVWc2CgJ4mFI+e9MZ+wnYZHSxqvtz5EnIlkIrPl29XDpvZoibZmYzyzX/hDxZPc4S+EMn0zClvHIa2zWFxh7wDIwzpXtngY6pgGcpNgtYrF3ddrTVhXMjO/AO2uZXctb6tkFmce8GR+bkONcM+tNrlrtffEGt1RW2JJ720tOEwhRtG6dKVIDBId3/41szO6Fn+O6JQpvdtvSFmpjrZ3AyXLBlCVvZBKgfvtMO0gI7ytdT+4Ev3BU9/UD4yBTDV0n8idOAERdWDzNI8fXS2B6qIrYmlvixpc4kywqeAWb+wvNF/einO90DexFDTBi36CU')
__connected_table__ = dynamo_client.Table("freshers-example")

print(__connected_table__.table_status)
print("\n")
