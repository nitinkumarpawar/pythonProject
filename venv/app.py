import boto3 as boto3
from boto3.dynamodb.conditions import Key
import json
from pprint import pprint

dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                               aws_access_key_id='ASIAX2KHRAJA4VO2RUPM',
                               aws_secret_access_key='HGH7hr2HxkaKue30Tm6WFybQ+Q2iRCm4RXwKkjAd',
                               aws_session_token='IQoJb3JpZ2luX2VjEO3//////////wEaCWV1LXdlc3QtMSJIMEYCIQCCPTVdBzFfDZe37hymnxFOA5sobXkrK6sjOw25XCIK0gIhAK8RmvfTmb9rCqa32iKKJV1TdNK9zVF6Cnm3BnzWG8oWKpsDCFYQAxoMNTM3NTU3Nzk1MzkzIgxi3vL21dcONBO+s9Eq+AJ2uEmeXpkw0lIXiZ81bOnY2IwsH0mMNsN/oLuNqm9F3dOApCGbVYA/WCf976KIavT0LZPTF+NGWaupnmDxny8WH8e1UzcMNIj/Ral06boCt8tybhTBbQki67xmvMFoXHA0KzYhLi8BpYbs1BWpl2BXDbZkLrt5eYF9QEurdymqY9BAfz962hpDZPRdgEYvPosZVya6tr/3xbUKuEMe3fFawHmNU8vcpIwibg4hkP5sEKi3w/aXGSzB94uW5l6Xy+vic9I3esOzOBEbOkBePSYE+Sks+sOLEOJ3x67OKM9pt+XgLz60QZY+zLBaCwQ0/hAFm+1DRz7KRFDSoJdFf5xudxoMa7Vqkvjf7+A4+Fy7v6oQRXxrfBYOs0OEKxit24W1ro6gRf4xoHoU1bt60EPYz5EzrcIjq83wbch/XVOyq5eEj+RYTjdfACjRUogxxb1W6eMFgmjLjSaL/d68aSs+YLrnSuD6ZvHdmEFGnTEOheGxkn7DwQN9MJv1nZ4GOqUBEawkdZFLUp+OIb28vI1Q+6M7F0PhEPkqQCd3Zj7WP6RRuji2F8Ee+RkSHS49FXG6QOoT2z56BT58RfVXVhA3DyhLNv+8Xq5fvyZB4Vc33lDP7VIEHRxXd1PJ5ItA2gys6yP/kH3E9JmOdR12o42JsL7IlKWLhcIkYEhFm4nHorZhlE2/wqydjf94plkdOeLkTpeBUV1E3jbzss/w+xhq7MkWNvf5')
__connected_table__ = dynamo_client.Table("freshers-example")

print(__connected_table__.table_status)
print("\n")

def post_questions():
    type = input("Please the 'type' (i.e. Partition Key): ")
    sortKey = input("Please enter the sortKey to be stored: ")
    question = input("Enter the question: ")
    item_details = {
        'type': type,
        'sortKey': sortKey,
        'question': question
    }
    data = __connected_table__.put_item(
        TableName='freshers-example',
        Item=item_details
    )
    print("Data Entered Successfully")
    # print(data['Items'])
post_questions()

def getAnswer_by_questionId():
    sortKey = input("Please enter the sortKey to get all answers by questionId: ")
    data = __connected_table__.scan(
        FilterExpression=Key('sortKey').eq(sortKey)
    )
    #print(data['Items'])
    print("Entered 'sortKey': "+sortKey)
    print("[")
    for i in data['Items']:
        print("   { ")
        print("    " + i['answer'])
        print("   }")
    print("]")
getAnswer_by_questionId()

def getAll_question_by_userId():
    print("\n")
    sortKey = input("Please enter the sortKey to get all the questions by userId: ")
    data = __connected_table__.scan(
             FilterExpression=Key('sortKey').eq(sortKey)
    )
    print("Entered 'sortKey': "+sortKey)
    for i in data['Items']:
        print("   { ")
        print("    " + i['question'])
        print("   }")
    print("]")
getAll_question_by_userId()

def edit_answers(val1):
    print("\n")
    sortKey=input("Please enter the sortKey to update the answer for the particular question: ")
    # val1: input("Enter the answer thats has to be updated: ")
    data = __connected_table__.update_item(
            Key={'type':'answer','sortKey':sortKey},
            #val1= input("Enter the answer thats has to be updated: "),
            UpdateExpression="SET answer=:val",
            ExpressionAttributeValues = {':val': val1},
            ReturnValues="UPDATED_NEW"
    )
    print("Answer updated: ")
    return data
    print(data['Attributes'])
val1 = input("Enter the answer thats has to be updated: ")
data = edit_answers(val1)
print(data)

def delete_question():
    print("\n")
    sortKey = input("Please enter the sortKey for the particular question that you want to delete: ")
    data = __connected_table__.delete_item(
        Key={'type': 'question', 'sortKey': sortKey},
    )
    print("Deleted the item")
delete_question()