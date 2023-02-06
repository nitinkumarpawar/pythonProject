import boto3 as boto3
from boto3.dynamodb.conditions import Key

dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                               aws_access_key_id='ASIAX2KHRAJAUQCRQGU6',
                               aws_secret_access_key='P4QDLXu3OiPY0JOQ6hskTqe1RhkKmJwK22pU33De',
                               aws_session_token='IQoJb3JpZ2luX2VjELb//////////wEaCWV1LXdlc3QtMSJHMEUCICW/qFR32DOV+JX2i//VEuxxTgzDZmo9dUf0LkNvZKFZAiEA8B7Q4SsFD/ogTYtO9GMvRsv5lEl67C8/hWTBySeu/y4qmwMIPxAEGgw1Mzc1NTc3OTUzOTMiDMdyuCPEDl3sdZM3iir4AiiP6f5Fwwp0ExAL6xulqQW81p6o102eefKiFrg4xbSpVNZVzwVGpKRBgeIOc27eSpilZlsTCqmZDuDGNkDT13H7fL+DBZBJH35cvVFUPtkuiw7Ovjn/QVHu7zyTtBs0oXlEr5pV7zXtCpvq1CeuA66BmXfSu1GfcQWS4f/XCEZhLeu/S9kYsCSxB2P5rIWrk8KotRvV0WPGNwNH3QcyaQuapcEV8ut4lXsdc43KynC2ajMBpWr83w0nMj38TYFN+Hq5rs3WwHH9KPT+Ts1J7CDT/NGZNZRVX0vWnSxO8lSCVzHtMhSocWI7ajhhIERu4YUzjk0/w3QsV99gHsYpcRK/ojtBwcVC+6lZ+TvuDjea5zMmUqRVulOCyiquf0W7F0NLYCl/BQw6Yld3Ts24bC0mwlCud8Uh0JEUsuwzhDlCeGTBNgRqyHgpfO4zC2hVrn0YhBGfr3lyNUzlUo8iQ4ZdahxUYdQ10s2rUiJcYlJvUXqSoaiSaUMw8J6CnwY6pgGbYTVQrlcNf5aa1RZZWK9TVKAYnDQH1J7odBEC0vUAgc1wpGefEhuJrkeydPdVII7D8894wuo0dL5UWs+GoG5UFeeesCp8itI0kLcpppcHGAmyKyES0l8AFfjxSd3OMSWMZxYYE+o5qgYnU4Eu0LA5/FJvWz4jF5/HYcuk7XQrYkZJbO8K0p+S75IKxZtKfO6JRXb/qjIrTLaQ+ktXLnezhxZBRO2s')
__connected_table__ = dynamo_client.Table("freshers-example")

print(__connected_table__.table_status)
print("\n")
