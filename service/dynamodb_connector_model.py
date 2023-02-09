import boto3 as boto3
from boto3.dynamodb.conditions import Key

dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                               aws_access_key_id='ASIAX2KHRAJAVHFJ4SIS',
                               aws_secret_access_key='3isfDLmpCXkt2tfim8gAlT8MnijcaiQOgl8EzO9o',
                               aws_session_token='IQoJb3JpZ2luX2VjEP7//////////wEaCWV1LXdlc3QtMSJIMEYCIQCXtmi5hfwp4xvv8aAXxoQag/HjhnJnOElmT/6b3XKYrQIhAJ/ZcoDcFjfc4GqA8cASsqUCfbkcVQvctfde4KPQbqd6KqQDCIf//////////wEQBBoMNTM3NTU3Nzk1MzkzIgz0/I6EGA4aYwmiBL4q+AIXAMY4i4gY5EHodQjP9yFxzvZ9/h8TRxkLHmdNkKSt9fB8K4GPuEgbBbL1yf7MxhPoOL1VrN7Vcscdg2UiOCg0qlqqAzpos1/fHiN3C1yXi7v40z972KYu7IdyBQcqIPprzN+7NHILjCx1hnOOwvgC4UYGSmIAPDBkD9q/cCxV7ERmre3xOPPYIxJDhC/ZbnEmTDcJQzyAn0FbCS6Pz4cmFR3xXpHUKh5RXUoA3fxcKvVj8IyvqZCBQh1ZSdyz10saF1m52IvxAp4MqQZF/AjG3Ra3ln9gC7UiuPoIvM3PY0rxmUgQbYx2OKDqjvD8LcfS10qeYJSsmekhtOzmyhokOcjQeW1RO3VDaVx2BXAgz8f6N9Ju3dMqBWDQ+R/My2XIhIxlAQnU54KaUer6Isziu7JdJuRW4Hps7mmZSseY8uNSfZgUxfVX/PjR5El3Yiwn1xEHYVPb/lPyWg2yQbqWDEHPU5VmeUMqiErS5kmUranb5mQQgT3MMMWRkp8GOqUB1+CrrdeiYK/NB8TwTMqPx0wCjWoyLqVhFu3UnDyyyC+9qww6SQYxTPPkQTurrjLy8sjP9TSpS8jFmUEZRGaJX2FbC3BB/OdAOlfQyi0JKEJWxhxUSMNlhq4ykT1d7eDC9yzezHkxZqxB2zr1fB7ExbaBeHbYsjkKm+9uFkiudCHr/TGV0Ai+a7qnGrhszogdn+REWTO4Va0TG6Hqdq1r81ZWqOqS')
__connected_table__ = dynamo_client.Table("freshers-example")

print(__connected_table__.table_status)
print("\n")
