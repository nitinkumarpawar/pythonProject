import boto3 as boto3
from boto3.dynamodb.conditions import Key

dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                               aws_access_key_id='ASIAX2KHRAJARQIYVX3S',
                               aws_secret_access_key='Mzna6SX+8x50cR/eGzba605Tf9g0ln7LiMfNmNIN',
                               aws_session_token='IQoJb3JpZ2luX2VjEGUaCWV1LXdlc3QtMSJIMEYCIQDmnzbO7uHATCCFa1rECvkZGu1nIxa4Irg3evlbsYVx2AIhAIkLPW3uO4pPRHCIsVlYHG6N0DDvBh3v+CWqKkeulnZDKqQDCM7//////////wEQAxoMNTM3NTU3Nzk1MzkzIgxxTculh/ahU1LUWPsq+AI9twerkX8/N/Jh5tItHBwdstrv99F9zpMXrH6muUc+Z3f6AZ+MGqO53TOL/rVxZOYLb5A2m7MjVKeEaB198EVRMkYu0Q7ADqhAn5lLIkujHBNBye+epOlWRUy6Ggc68RS0OeIs4ZZSr2AAV3+n7XzY7n5J4lCn6kvk6JWULXiz+z9L891Vtw0aVB5UWZ1kPoSJDIe9PeQdUgMMRqqGsolxzeSdMiWMMClTGrRJyxeRvzJfRPwkgx9O4xUVF+WRFelti4Tt5Uz2KPlweQtnuWP1pANJmbJ+dDtIMhfR6a69z9CnI5fHQZUyJ6gU7SY3rYLpbGEDHp3dl8WvVsxJpRwhxUVA3Llcl0eFajiJyKGJNOqXtpqsx0jPffb2VRYLkBTZROO8n+fLlHLdc7FsPND3ywW5rx6xHSZypDPPqxDnKZZOhHqOpoQ8mnExzKetq9d4m+aHCD24ioXFm7dfPgc1QGU6DgpZwgM3dzdDWPbc6xLeIo5Db3diMJWquJ4GOqUBrvJOG54hwcjaboH6VWsNjhcMaI9KiKqMZkJkuU1TMBShS6MTQmfpiiKLi3OFouAMJXOHXSxPMtSobf8wLrlQCvoQr7hJ5P/YyRdEi0Q1frDCy199zAQ4/npt4WGRh67e3rIu/oDB/gLtA9xlhP3LGQYMPhP3JANiSI3aMaCSQh/Qm40ygCLg4IzglptSmV1IG7AU9sIxpPJmyex7eJn1hwgB1ROv')
__connected_table__ = dynamo_client.Table("freshers-example")

print(__connected_table__.table_status)
print("\n")


def post_questions():
    print("To Post a Question: ")
    type = "question"
    question = input("Enter the question: ")
    questionId = input("Enter the questionId: ")
    userId = input("Enter the userId as your emailId: ")
    status = '1'
    sortKey = str(type + "#" + userId + "#" + questionId)
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
    print("\n")
    print("To Get an Answer by QuestionId: ")
    type = "answer"
    questionId = input("Enter the questionId: ")
    userId = input("Enter the userId as your emailId: ")
    type = "answer"
    questionId = input("Please enter the questionId: ")
    sortKey = str(type + "#" + questionId)
    data: object = __connected_table__.query(
        KeyConditionExpression=Key('type').eq(type) & Key('sortKey').begins_with(sortKey)
    )
    for i in data["Items"]:
        try:
            if i['status'] == '1':
                print("   { ")
                print("     userId: " + i['userId'])
                print("     answer: " + i['answer'])
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
    print("To Get All Questions by UserId: ")
    type = "question"
    userId = input("Enter the userId as your emailId: ")
    sortKey = str(type + "#" + userId)
    data: object = __connected_table__.query(
        print("\n")
    type = "question"
    userId = input("Please enter the userId: ")
    sortKey = str(type + "#" + userId)
    data: object = __connected_table__.query(
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
    print("To Edit an Answer: ")
    print("\n")
    type = "answer"
    print("Please enter following details to edit and update a particular answer: ")
    questionId = input("questionId: ")
    userId = input("userId: ")
    sortKey = str(type + "#" + questionId + "#" + userId)
    data: object = __connected_table__.update_item(
        Key={'type': type, 'sortKey': sortKey},
        # val1= input("Enter the answer thats has to be updated: "),
        UpdateExpression="SET answer=:val",
        ExpressionAttributeValues={':val': val1},
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
    print("To Delete a Question: ")
    type = "question"
    questionId = input("Enter the questionId: ")
    userId = input("Enter the userId as your emailId: ")
    sortKey = str(type + "#" + questionId + "#" + userId)
    print("\n")
    type = "question"
    print("Please enter following details to delete a question: ")
    questionId = input("questionId: ")
    userId = input("userId: ")
    sortKey = str(type + "#" + userId + "#" + questionId)
    data: object = __connected_table__.update_item(
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
    sortKey_begins_with = str(type1 + "#" + questionId)
    print("enter")
    data = __connected_table__.query(
        KeyConditionExpression=Key('type').eq(type1) & Key('sortKey').begins_with(sortKey_begins_with)
    )
    print("1")
    for res in data["Items"]:
        sortKey1 = str(type1 + "#" + questionId + "#" + res['userId'])
        print(sortKey1)
        data1: object = __connected_table__.update_item(
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


def delete_answer():
    print("\n")
    print("To Delete a Answer: ")
    type = "answer"
    print("Please enter following details to delete a answer: ")
    questionId = input("questionId: ")
    userId = input("userId: ")
    sortKey = str(type + "#" + questionId + "#" + userId)
    data: object = __connected_table__.update_item(
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
    print("Answer deleted successfully")


delete_answer()


def post_answers():
    print("\n")
    print("To Post an Answer: ")
    type = "answer"
    print("Please enter following details to post an answer: ")
    questionId = input("questionId: ")
    userId = input("userId: ")
    type = "answer"
    questionId = input("Enter the questionId: ")
    userId = input("Enter the userId as your emailId: ")
    answer = input("Enter the answer: ")
    status = '1'
    sortKey = str(type + "#" + questionId + "#" + userId)
    item_details = {
        'type': type,
        'sortKey': sortKey,
        'questionId': questionId,
        'answer': answer,
        'status': status,
        'userId': userId
    }
    data = __connected_table__.put_item(
        TableName='freshers-example',
        Item=item_details
    )
    print("Data Entered Successfully")


post_answers()


def getAll_answer_by_userId():
    print("\n")
    print("To Get All Answer by User Id: ")
    type = "answer"
    userId = input("Please enter the userId: ")
    sortKey = str(type + "#" + userId)
    data: object = __connected_table__.query(
        KeyConditionExpression=Key('type').eq(type) & Key('sortKey').begins_with(sortKey)
    )
    for i in data["Items"]:
        try:
            if i['status'] == '1':
                print("   { ")
                print("     userId: " + i['userId'])
                print("     questionId: " + i['questionId'])
                print("     answer: " + i['answer'])
                print("   }")
            else:
                print("   { ")
                print("     userId: " + i['userId'])
                print("     questionId: " + i['questionId'])
                print("     No data: Answer has been deleted")
                print("   }")
        except KeyError:
            print()


getAll_answer_by_userId()


def getAll_question():
    print("\n")
    print("To Get All Question: ")
    type = "question"
    data: object = __connected_table__.scan(
        FilterExpression=Key('type').eq(type)
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


getAll_question()


def getAll_answer():
    print("\n")
    print("To Get All Answer: ")
    type = "answer"
    data: object = __connected_table__.scan(
        FilterExpression=Key('type').eq(type)
    )
    for i in data["Items"]:
        try:
            if i['status'] == '1':
                print("   { ")
                print("     userId: " + i['userId'])
                print("     questionId: " + i['questionId'])
                print("     answer: " + i['answer'])
                print("   }")
            else:
                print("   { ")
                print("     userId: " + i['userId'])
                print("     questionId: " + i['questionId'])
                print("     No data: Answer has been deleted")
                print("   }")
        except KeyError:
            print()


getAll_answer()
