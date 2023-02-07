import boto3 as boto3
from boto3.dynamodb.conditions import Key

dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                               aws_access_key_id='ASIAX2KHRAJA3BAZVYNX',
                               aws_secret_access_key='5ykp7s6lAPq4cDxFN0gWWCwIKrM3AlmrQnAzTB/q',
                               aws_session_token='IQoJb3JpZ2luX2VjEM7//////////wEaCWV1LXdlc3QtMSJHMEUCIDbcZ0ok+D30mtIO21nL7K9jVKdlsxVKvZF37fGoUo7qAiEAsCV5zNoXpiniF2c39H3KXpJZ+jX+yhgq3HG6g7h4TOsqmwMIVxAEGgw1Mzc1NTc3OTUzOTMiDDCVNwA0GKsBoMcIzyr4ApqCbWgLaQvg+80CYSVYvdwboUupWzksDU0PUl1srKer0gV5Sz3a2ph3ZcQy2yu+cRlbty1/y3pv2AgLXe8Vgh4/lQZxUd/+aHRu04v8LAU9cJjslYJq7ZP2mFAewhbQXZ0DkUxO5AKhtGXnz/HkXwpl5VJJwUC5nQ6PZvLOZ4q9A2FYgyloOqXQefcNtsyzqY1IJUYXjbA8Wzcl+K1BzGMkPgYGbC7hcyO592D/IlT6Rn179Sk4gdiSWP6f5JrYlFJ9u7BICJkKBmYsSot6GdNDCHYPi6ChXstJdHhD2DWJJ+knY18pyZX7AphdbblLzRpXRv+r9+Aicl8X6TLYYosPXNKdyPz7t4uHTRoNm79xCIWHuy6q9jiGN8sxpjE45gxv7zei7CHt1IPBaavryUDQxcTT2g8zIzuimKXrSkbYIW39Nseys5UPzTo+wrkMVxI5/iclKT9EVa0GWFwv6h/TrjANr1XJ2rHakwv5a252JOcvFhO+otkw78KHnwY6pgGousccHaBwRa4udxOFn2NL5Bp2aC/Pe2Sg7cOZpH/DGX9x4qN+Y0IbeFa3y+x0vzKX65t+e57eQnDY4cjJ/Ch9WX6c9I2EfeXmMxpaeJqr4CH/+WLxUCGbA+D+oX9qobTsG6r8VbQmFJ7flYmL1WvgEErFqhBK1ayJV73zUy8K2xrTMCtdmPMWFAHfOQcRDLvQJfGkwyEkun/xFTiATuj9DZsLF/YN')
__connected_table__ = dynamo_client.Table("freshers-example")

print(__connected_table__.table_status)
print("\n")
