import boto3 as boto3
from boto3.dynamodb.conditions import Key

dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                               aws_access_key_id='ASIAX2KHRAJASL3QKHKM',
                               aws_secret_access_key='+ZfMIbKkIvY7g/uE3EuHcrk821zrdKoBE8X0+fb7',
                               aws_session_token='IQoJb3JpZ2luX2VjEOb//////////wEaCWV1LXdlc3QtMSJIMEYCIQDSkR8rLSFY3Fi5iZdUVkLn0yXIiqvb6ToJnGSlHWBRegIhAOXgbee4p0QZgPGX3UI48NX8PHPbriP671Q7QgPNBKx/KpsDCG8QBBoMNTM3NTU3Nzk1MzkzIgx/DhWGGpj7OyKyBwUq+AJNJ4jys4+u7pDTUjmTXNlOHwr2DU/YKTHNawV1l7NlIs5bCY47EeuJpmZs/Sd/YX3+rpxjQVO2Pgr+BrgHthKtcR3cN4OkV5sXZ+kayYpaj7/xlu9YC8jcJRuDGHJgjmUdNavN+gPYW9N4U8Jep6XLM3KcnumWUqv21Ujr/pvEzAUwC/1SDv89Z4Wd1aVqAK9zJj5M3a/dnRE6yjoN9LTRCF2PpRwhgn5+Gx0Gho8ZqrxzSf2FOnZpFcyYheb5gGDjUbAip2P1eVixLNp+jbJ286N9AQX2QgYD5dSxXoNGB7sUKOGcByBjcI1Wc+JJov5Rn1zyB4YIKk9TjzjqonB9FmBzKnD+85yLllrOwe5+Sd2f6PeCXrAF/fW3UU403aQsgbBCOyiusx5JQPLuCu+/1TSkr43JvrjnYubSCfsADIl7Smgw/l5QDSRvg8joOF5KzTeC0ruzOh/FBXbRlUhbgZXaGC03m6lwQ5cGihlWb3AGZlEXJ3f9MMHljJ8GOqUBsPGWpT/LwaCPFJAzKpklDuy8vuMekiwi3iJDG1dRvamZxcDIk7S0gOoYPuh1R5WGYMHnlgMJJ4pXt1FRT7Xx0xJ1VgDis855UHZKMBiaKurX94tVNJ2+iEWHn1OgtKiNT4J/7pGXsabQhQgUsKwqiYXJ+QR1NMf4QrvuRcCyAn8GcfNjZzarNhoFh6mWrqWDOjIQnBzggjiuKg5bd7k/jPSyB8wf')
__connected_table__ = dynamo_client.Table("freshers-example")

print(__connected_table__.table_status)
print("\n")
