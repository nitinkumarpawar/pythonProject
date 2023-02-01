import boto3 as boto3
from boto3.dynamodb.conditions import Key

dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                               aws_access_key_id='ASIAX2KHRAJAXI3B3SL7',
                               aws_secret_access_key='KjUCJ9oOX9zaZnPCf19ufwSqamWZreR0cssStkz9',
                               aws_session_token='IQoJb3JpZ2luX2VjED8aCWV1LXdlc3QtMSJHMEUCIQDWgF8tlfpdlXWMjDGEHXTz3YVzHwQKOa8+H3pEhwwAvQIgNMyOrl5y9vYArRuSJf6ZsGdYffm2i6sOtSfT3TD1SCoqpAMIuP//////////ARADGgw1Mzc1NTc3OTUzOTMiDMQNLe9vqyNsbYkzxSr4ArCab64/3DEuSU6kVK07MoZ7hbnx/z2zoerBCTcuGlfuslzItCozsWdA3dWBM9uCjqnk+Rb4QyTQsryB6sTzJf3jSl+gGLf0egrIXdcnKMoxDw+74vVXlGqfx8LqqBFEnxAmYBPMNDYBAjDMsXNRYWhawZfEJkpWEWcUIrhVbwywU8Cn5zAxrG7bVDmfJfHDO7WSizxNbiB5QDRDnjxCh06oRR4348F4xr/5vG3TaqPszH3rFiKqQHSQ1P7krHVl8u+vs0ZC/gwrawKi7+7PSkjbAgUfxGeguTgIGUJzGm7ZQtsNDkcM2VWWM4GLubeeA7waYCCzqqCZYcZXk7aNRRW4AfXOtKDSEsUkvpJJWYSBel+ljBQNSrD5EZysHD/R7mhLejGOLO4DcxGcFZaJHwfnw/kpGLSnl5BWtYTCIv8JMx+32JMaAcMzLkK/IDK8Osa9MQwHMO21lXhMCK+UivnPu+j3KIE5WEPWusS2SA9IGPeCMiV1AnMwwZbongY6pgFIsAfU/0o/3dfsvnsi5p7eDp3OWsDzpzyxmfuuTw8mMOdRlu1YFb6SZp6jn9Lg38L7peJ3Dn0UKypoXfWjhm30utn7R2cny4cg4g88dsTXSuGHhad8V+GigLPZmXQNIAy/ZqAvV6QjZLXsP0MAt7WbRTGnmYkl6YR6w+4BLLqPHjS8Flcj69yjLAiiotSKT/KP9AdMRt8k1K8RsJ35DOLxvyA+x6mt')
__connected_table__ = dynamo_client.Table("freshers-example")

print(__connected_table__.table_status)
print("\n")
