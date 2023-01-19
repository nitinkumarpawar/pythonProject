import boto3 as boto3
from boto3.dynamodb.conditions import Key
import json
from pprint import pprint

dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                               aws_access_key_id='ASIAX2KHRAJAU5KPS4XH',
                               aws_secret_access_key='V+OXAZAGto/STf/01jNZFmkqub+f+p/3pXcBhljY',
                               aws_session_token='IQoJb3JpZ2luX2VjEAYaCWV1LXdlc3QtMSJHMEUCIQDYMX1uBq9pKjmRid8PRkuIlEflCv8tOdr/THaaQtvvUQIgavoQTgVjswle45Px7+fALSgFeqpv/bXLFGYqJ3D9JmoqmwMIbxADGgw1Mzc1NTc3OTUzOTMiDJJrIJj0qiaDSesKqir4AqCqdNV1BQD0DcmUHuPKVhhU5Xpmh+xRb5bwO9s82bxzm1z3Zi8CPkG4CUnVfUVitJOLJawlPCQLBWudPPMMhFscS7z6wSot9iPbD8LpaNYOZekGTintOeMf+gxL/j/k0pNaEqOF/CdjiG4zA7FSO9HdxXg8xyKvNJjoam8P/GOCaZht2ozdCb88uT6Tn8YLPjSqkOsJn9ytWkidNsqqddXY3ZwtuYuJ72+UBTS5xTzpBbOh1hyHpCxM6yuvRAInlGPaJPoEOtRPkhG1MFniu4e2d0Rt6qKKQU86MsC5SrMnl2bJJQCpDnwEPW89HyRbiVVOAGr6j308jUFoVoEn2BJ53pvnX2rLInqVdzVe/HM03BcPkYr9OIcH8yNZdocnLjT80Nz9z9/Tvjr7EYWOpYiKnrxHQAaYIOX5IoItuYqFWjxU5WoCDQ9rC9ru8Uz15xxExn8HbZxXwvS4IAzpdGaKfaMKEyhGRt/xILH9b4RrdC5At874lU4wrqqjngY6pgHThuLGLtPPoImVBbXZlXAomnE9nVEcyAPxbchR1SlZOQNmyneg69VnUtTw8jE/yCe8cEjlUzoWE/6KXKSiu0yaoVAH9RfBLkMnGdUhtbWBFGwAlXrg9V/7Q/lZwjDlUssa+z+PrZq5C9ec+2V0My7IiF/rK+vJY28aWknt+Korfo2xoVHEGvD7IV/6/knVucjZzl9rY4cUCez63cRHmyFlylIC93zs')
__connected_table__ = dynamo_client.Table("freshers-example")

print(__connected_table__.table_status)
print("\n")

def post_questions():
    type = "question"
    question = input("Enter the question: ")
    questionId = input("Enter the questionId: ")
    userId = input("Enter the userId as your emailId: ")
    sortKey = str(type+"#"+userId+"#"+questionId)
    item_details = {
        'type': type,
        'sortKey': sortKey,
        'question': question,
        'questionId': questionId,
        'userId': userId
    }
    data = __connected_table__.put_item(
        TableName='freshers-example',
        Item=item_details
    )
    print("Data Entered Successfully")
post_questions()

def getAnswer_by_questionId():
    type = "answer"
    print("Please enter following details to get the answer by questionId: ")
    questionId = input("questionId: ")
    userId = input("userId: ")
    sortKey = str(type + "#" + questionId + "#" + userId)
    data = __connected_table__.get_item(
        Key={'type': type, 'sortKey': sortKey},
        TableName='freshers-example'
    )
    print(data)
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
    type = "answer"
    print("Please enter following details to edit and update a particular answer: ")
    questionId = input("questionId: ")
    userId = input("userId: ")
    sortKey= str(type+"#"+questionId+"#"+userId)
    data = __connected_table__.update_item(
            Key={'type':type,'sortKey':sortKey},
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
    print("Please enter following details to delete a question: ")
    type = "question"
    userId = input("userId: ")
    questionId = input("questionId: ")
    sortKey = str(type+"#"+userId+"#"+questionId)
    data = __connected_table__.delete_item(
        Key={'type': 'question', 'sortKey': sortKey},
    )
    print("Deleted the item")
delete_question()