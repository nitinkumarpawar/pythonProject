import boto3 as boto3
from boto3.dynamodb.conditions import Key

dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                               aws_access_key_id='ASIAX2KHRAJAQQM3OCCE',
                               aws_secret_access_key='N2MImavGEno1aBypggmZMqqKR9o+EFf5vRLSdPWh',
                               aws_session_token='IQoJb3JpZ2luX2VjEPL//////////wEaCWV1LXdlc3QtMSJIMEYCIQDMeUEwuzE1yypEs5CWMvXudz8NnQJ2geTByohoenyZ4wIhANp9dS6sORF2wi6gzDrdBygW8Npu/otz0ahF2IfFgcttKpsDCHsQBBoMNTM3NTU3Nzk1MzkzIgysqPPNq9a/CIjXwqQq+AKaxkVNkfACKdKTR736HpokpD6lQxGdhVN8aSCvdYlU9epMPoBOzGodOk7AcQeH07qEluJK6rvxSkHupUmxyLg6VPgr7fRxr2gxXHbiv9aeZIXT8SrGKguMov7ncFR7LdbUZEgheHTxc/LarWOqHt0dorhXmK7KChqopa6cwURqBWMXMGnuDj1UznjNEccs51PEr/eQdhTvz7HxwAg8BBmizcBbBN5U3NaQ0/hRdGDYfq/8C8Fmf4GyaT5J7L+8OJcEy+JbTp/Gy+objBLSOBe7WIG0dQ3m7JjeJfQOPcMZVhf9hB8iWazFC1r7LhK651UnsfVMGDfZr5JUHXF+rBeER5AZZ8f1kdr8/FzhCxPCs2tG/n2/GnclOzPm0Jo8/iD+gjV7QyQpjrq2ZEL0i4HmKkndqmGfb0Hdb45IwLWsXUm7dFMlkmRXgVdyKDTzTTdka/7ztWi/H/tuyrhaDC/qhfbm3FHt3Qzp90F5E8+k0QiHR4WJcPBQMOvAj58GOqUBp0pyz0a1TFHQBKmMd6hrAEWJrvuKEm7HGCGVY3hlUDP5xnyekClDzH5jGaNNlYTIkaIg8My4xnL6IekeRTrE8GW9ECjWZb3f7HH97AuUnyatGYAQsv8ZLjpl2DvtwQauIlNW8WCjKHF79b0Ix1yA60bxqdQINO/YQde4DCVZtEnpeddzuj+H2nABqmW1v45m2OIt/RVc7uYeCAd6WT3KtG0RQHRI')
__connected_table__ = dynamo_client.Table("freshers-example")

print(__connected_table__.table_status)
print("\n")
