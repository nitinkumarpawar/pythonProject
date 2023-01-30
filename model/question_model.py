import json
import uuid
from boto3.dynamodb.conditions import Key, Attr

from model import dynamodb_connector_model

id_db = uuid.uuid4()


class question_model():

    def post_questions_model(self, data):
        type = "question"
        question = data['question']
        questionId = id_db.hex
        userId = data['userId']
        status = '1'
        sortKey = str(type + "#" + str(userId) + "#" + str(questionId))

        item_details = {
            'type': type,
            'sortKey': sortKey,
            'question': question,
            'questionId': questionId,
            'status': status,
            'userId': userId
        }
        data = dynamodb_connector_model.__connected_table__.put_item(
            TableName='freshers-example',
            Item=item_details
        )
        response = {"message": "Data Entered Successfully"}
        print(response)

    def getAnswer_by_questionId_model(Self, data):
        type = "answer"
        questionId = data['questionId']
        sortKey = str(type + "#" + questionId)
        data: object = dynamodb_connector_model.__connected_table__.query(
            KeyConditionExpression=Key('type').eq(type) & Key('sortKey').begins_with(sortKey),
            FilterExpression=Attr('status').contains('1')
        )
        for i in data['Items']:
            response = {
                "userId": i['userId'],
                "answer": i['answer']
            }
            print(json.dumps(response))

    def getAll_question_by_userId_model(self, data):
        print("\n")
        type = "question"
        userId = data['userId']
        sortKey = str(type + "#" + userId)
        data: object = dynamodb_connector_model.__connected_table__.query(
            KeyConditionExpression=Key('type').eq(type) & Key('sortKey').begins_with(sortKey),
            FilterExpression=Attr('status').contains('1')
        )
        for i in data["Items"]:
            response = {
                "userId": i['userId'],
                "question": i['question']
            }
            print(json.dumps(response))

    def edit_answers_model(self, data):
        type = "answer"
        questionId = data['questionId']
        userId = data['userId']
        val1 = data['val1']
        sortKey = str(type + "#" + questionId + "#" + userId)
        data: object = dynamodb_connector_model.__connected_table__.update_item(
            Key={'type': type, 'sortKey': sortKey},
            UpdateExpression="SET answer=:val",
            ExpressionAttributeValues={':val': val1},
            ReturnValues="UPDATED_NEW"
        )
        print(data['Attributes'])

    def delete_question_model(self, data):
        type = "question"
        questionId = data['questionId']
        userId = data['userId']
        sortKey = str(type + "#" + userId + "#" + questionId)
        data: object = dynamodb_connector_model.__connected_table__.update_item(
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
        data = dynamodb_connector_model.__connected_table__.query(
            KeyConditionExpression=Key('type').eq(type1) & Key('sortKey').begins_with(sortKey_begins_with)
        )
        print('10')
        for res in data["Items"]:
            sortKey1 = str(type1 + "#" + questionId + "#" + res['userId'])

            data1: object = dynamodb_connector_model.__connected_table__.update_item(
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
        response = {
            "message": "Question Deleted Successfully"
        }
        print(response)
