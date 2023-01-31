import boto3 as boto3
from boto3.dynamodb.conditions import Key

dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                               aws_access_key_id='ASIAX2KHRAJA6AC7GBSW',
                               aws_secret_access_key='1X7tO+wgU25D9U5chIwue3vQAEPVDqMoLm82zfWI',
                               aws_session_token='IQoJb3JpZ2luX2VjECcaCWV1LXdlc3QtMSJHMEUCIFetjiXvMDL7RmLhWXNGiA2bj7RdEs8Wg5F2EvY+LqwAAiEA/lfwwhPaLZTOgY8zJVGDuCjzll7WSZIGaSY/sY37MGEqpAMIoP//////////ARADGgw1Mzc1NTc3OTUzOTMiDLCYLdvlGoSPwAGhSir4AlqMyTwVjAY3+PnrmWkJZa2M3Gc+TXHKZX7H2Trn4kpV/DRoebwJznTvw7iYlJSazXvbX7MwAZ7lHFf0Kndk8kmYRaTao7TfwWJ5oE9Tw4WPALO0PQFqjmkOLlBqoryKE1SsL7MSZ14jTKntVg19nxklXUPQirK0HSgdfjjCFxB9BsWuW7odbtGdCc0ZZ6O8jTy5eHaVOiM7CuEPN56llKD3vNeuj7kBgkSRZnb8lHA4DnZarxHNA4HcoduOV7J5jLDOfmwlpi//zdiyV4rFBII5KCUR60V4hMIFzU64hHbnIW7mVnJaeuOW4Q7Wx/pqWevjGuraSf/MLaBFTRT4AOUDZuxXQ4O7BkYMFaAlrGdH7Ir6dtd1SJt4XPtgUwKCsev1DebS5XKxW+TzUSk9IfH82L/ZqbN04uN8KMbteof12rj0+46MnZ3gkqhWluKeqA6JLkHCjRPxYMpFc4mY9fDM/BfBHvRbWMds8OoC+JDY+B3HGUrbAdowkvPingY6pgGW/Oh8aLXfkCmvpzuhDd0f2zh9jErmtzDu/EVaofV5srWZJaxSMjfEIU9+kxBVXNHBoG+mjWXxRCGTIBoj7yGvGnBC2D9ytq0Y7hO+OUmGlP5c5EM2eMPXmiYBfUmKn1NzcSp3y560gxfa9uKZUjPnOEXF2ifmGkirlJf79oRU4BB9yuzt6IEnTet37kDopeAVsYdcSUQbsm5DIcP4yhy6uXK6IHUx')
__connected_table__ = dynamo_client.Table("freshers-example")

print(__connected_table__.table_status)
print("\n")