import boto3 as boto3
from boto3.dynamodb.conditions import Key

dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                               aws_access_key_id='ASIAX2KHRAJAX2CAPJFF',
                               aws_secret_access_key='nxp1BTA+XH24VuzCUZhdocrrc7TMOS2Mhj/98amm',
                               aws_session_token='IQoJb3JpZ2luX2VjEF8aCWV1LXdlc3QtMSJHMEUCIQDA3Dib0mpxXlXVADBDO9uaMMA8lmCCH7xxDkhCCch76QIgDCtohDfB1W2ajOD8hOmf6jwQi1Op1MI9pdgsn76KF0wqpAMI2P//////////ARADGgw1Mzc1NTc3OTUzOTMiDEJoj+PigVPTlrSYACr4AueTwinV/+EPwJklHiFt9QxMOAOV5MiDrKCeneto/Ui/Hk50r1HBbwIpAVYzmebLZp8KpfDmuk2Ujj9cVx82ym4MEj6BmI2RzdLq9ktj3n7p9/q/304XyLzXoYiOPiJH4rMKaGqRZvUl9BYea2fIkoV73dcKaMIINDv1iyTCd/ScNBWJP6oGtwXo0Xd4bl7lFp8iYp9FIhpJdEbcw/QXumuZHavhXNMToAa4e0BSJFUlUYxjDEZk5elcQ9xp/WVm14Fw3UGoPdZ/TLJzT7PfCJK+FHUN5cDtRWHm6I8/74VG3HQE0L7Xzyo7n5YGjCWMoonfe3BiRGUlFG+Ppd105QiZzFPM98hL4xD96Dg0K4EdQWrjcFfSl6xVCvC8ZFprSS1j7tl2bszuTi9m/EJzlE8X/Xg/WoDRi2qzbDIy5lzYKPVe6++Q1RpXkVG5au2KwIYy+8i8Kt3FqIr0/MaPG7FTLBTMioCkUO2yTKliEqwZ2cZ/BsqAuI4w55LvngY6pgGH6eTEqGedw2ZsETGA/XN9SoJN2od1TLUvgW/SYyBrcLGsyoYX65W5SdZ8Zj4IxrdCaPTq7f/Zvn/t7DYx5E2VqXfhUUmp32kE8OAfMWIt7a5Ep5s2TqKs0vlw0mWZcWxWjEoCTDSCfskTDEWwWB2mD6CmrH5vsD78kkrpz3JXwXt3TjTp08E8Myqzyty3o+BXwsdbAYnaix5xzTHmfE945hNbsqcu')
__connected_table__ = dynamo_client.Table("freshers-example")

print(__connected_table__.table_status)
print("\n")
