import boto3 as boto3
from boto3.dynamodb.conditions import Key
import json
from pprint import pprint

dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                               aws_access_key_id='ASIAX2KHRAJA2BMVS6MT',
                               aws_secret_access_key='Dv9mYASXFm8R1bC4EgeiEBjJqJy4Q+kCGGLORMp5',
                               aws_session_token='IQoJb3JpZ2luX2VjEB4aCWV1LXdlc3QtMSJHMEUCIAo6k+dXcuWFYEIcNBbpQ9unD8HvOE06m+6BS47o6ANdAiEAi39+0GCo/nHx13BGL9SkOpiGeEHz1a6mMFLtkxtrfbwqpAMIh///////////ARADGgw1Mzc1NTc3OTUzOTMiDJGXcgsoIi37HznlEir4AnfSNppwpiXaO1lQhkwyWMIIz/MrXlP0XWh81mJVeDlsEApip4mE3du+chvaU3FKYxvDa5SXo9ZXOAi1FRn4chTuI93xmjIzdiGZJUECB7oLQOB6M88ZTn4ZbL0Hw2Nrku6GIJKqzoogGKducbybb41/Y5uyXiJwnB5Tv+Ti9sOWI65TEKGXaGjRnSawtnSoA4U8ATcU3PP/p6hoYXzUo4f9W4+c6tC0G+Kn24N0xLnENLw0qYoIe78+tvnYByrKBYPn/ow0Q0zYradpDN5J0kwjhjleCMPzcH2rsi4SZSzbO7j6rDQamBEpvNI74i6NpvQKyiy9+U3gmSpoeXz3uX5QQbo9QI3DAFpDzOwmuaxjwHmEooNATL7qL0YVljvWtNGc4zLRRPfvcCJbzOPkG8qe1Ub5/Fs9+XwAY1GEiDNrwoZ0j3WU7k6lH5++3rozIMRyW930zohYM5cD7Nu4jqln8gw2PVec12ZDJRzmcHk24alN/DOAVK8wkdWongY6pgEqRFVejK0NQX56O67ltWxEFb8KI3BFlTF/zX17pdj/QX+ekIdXWA/H0u4otKjga49iW4VZrnNGIDTGFDXaGuevl3a/I/m1EEws82jWs6SxhWI2NXCSzE9+uaZJUXY9b1OQijt4y8yOUBxemEU3lH+auduQvjFOufmCm0c0ChJycryAynL/t1S4em5oel8nr/qSsWXzyDgF6j8z6TgrZWOuufg5L1Ry')
__connected_table__ = dynamo_client.Table("freshers-example")

print(__connected_table__.table_status)
print("\n")

def post_questions():
    type = "question"
    question = input("Enter the question: ")
    questionId = input("Enter the questionId: ")
    userId = input("Enter the userId as your emailId: ")
    status = '1'
    sortKey = str(type+"#"+userId+"#"+questionId)
    item_details = {
        'type': type,
        'sortKey': sortKey,
        'question': question,
        'questionId': questionId,
        'status': status,
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
    questionId = input("Please enter the questionId: ")
    sortKey = str(type + "#" + questionId)
    data = __connected_table__.query(
        KeyConditionExpression=Key('type').eq(type) & Key('sortKey').begins_with(sortKey)
    )
    for i in data["Items"]:
        try:
            if i['status'] == '1':
                print("   { ")
                print("     userId: "+i['userId'])
                print("     answer: " +i['answer'])
                print("   }")
            else:
                print("   { ")
                print("     userId: " + i['userId'])
                print("     No data: No answer from the user")
                print("   }")
        except KeyError:
            print("")
getAnswer_by_questionId()

def getAll_question_by_userId():
    print("\n")
    type = "question"
    userId = input("Please enter the userId: ")
    sortKey = str(type + "#" + userId)
    data = __connected_table__.query(
        KeyConditionExpression=Key('type').eq(type) & Key('sortKey').begins_with(sortKey)
    )
    for i in data["Items"]:
        try:
            if i['status'] == '1':
                print("   { ")
                print("     userId: " + i['userId'])
                print("     questionId: " + i['questionId'])
                print("     question: " + i['question'])
                print("   }")
            else:
                print("   { ")
                print("     userId: " + i['userId'])
                print("     questionId: " + i['questionId'])
                print("     No data: Question has been deleted")
                print("   }")
        except KeyError:
            print()
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
    type = "question"
    print("Please enter following details to delete a question: ")
    questionId = input("questionId: ")
    userId = input("userId: ")
    sortKey= str(type+"#"+userId+"#"+questionId)
    data = __connected_table__.update_item(
        Key={'type': type, 'sortKey': sortKey},
        UpdateExpression='SET #ts = :val1',
        ExpressionAttributeValues={
            ":val1": '0'
        },
        ExpressionAttributeNames={
            "#ts": "status"
        },
        ReturnValues="UPDATED_NEW"
    )
    type1 = "answer"
    sortKey_begins_with =  str(type1 + "#" + questionId)
    print("enter")
    data = __connected_table__.query(
        KeyConditionExpression=Key('type').eq(type1) & Key('sortKey').begins_with(sortKey_begins_with)
    )
    print("1")
    for res in data["Items"]:
        sortKey1 = str(type1 + "#" + questionId+ "#" +res['userId'])
        print(sortKey1)
        data1 = __connected_table__.update_item(
            Key={'type': type1, 'sortKey': sortKey1},
            UpdateExpression='SET #ts = :val1',
            ExpressionAttributeValues={
                ":val1": '0'
            },
            ExpressionAttributeNames={
                "#ts": "status"
            },
            ReturnValues="UPDATED_NEW"
        )
        print(res['sortKey'])
    print("Question deleted successfully")
delete_question()