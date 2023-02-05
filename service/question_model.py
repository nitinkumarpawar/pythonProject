import json
import uuid
from boto3.dynamodb.conditions import Key, Attr

from service import dynamodb_connector_model

id_db = uuid.uuid4()


class question_model():

    def post_questions_model(self, data):
        type = "question"
        question = data['question']
        questionId = "5000"
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
        if data['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(data)
            return {"message": "Data Entered Successfully"}
        else:
            print(data)
            return {"message": "Data Not Entered Successfully"}

    def getAnswer_by_questionId_model(Self, data):
        type = "answer"
        questionId = data['questionId']
        sortKey = str(type + "#" + questionId)
        data: object = dynamodb_connector_model.__connected_table__.query(
            KeyConditionExpression=Key('type').eq(type) & Key('sortKey').begins_with(sortKey),
            FilterExpression=Attr('status').contains('1')
        )
        if data['Items'] == []:
            return ({"message": "Data not found"})
        else:
            for i in data['Items']:
                if data['ResponseMetadata']['HTTPStatusCode'] == 200:
                    return json.dumps(data)

    def getAll_question_by_userId_model(self, data):
        print("\n")
        type = "question"
        userId = data['userId']
        sortKey = str(type + "#" + userId)
        data: object = dynamodb_connector_model.__connected_table__.query(
            KeyConditionExpression=Key('type').eq(type) & Key('sortKey').begins_with(sortKey),
            FilterExpression=Attr('status').contains('1')
        )
        if data['Items'] == []:
            print({"message": "Data not found"})
        else:
            for i in data["Items"]:
                if data['ResponseMetadata']['HTTPStatusCode'] == 200:
                    return json.dumps(data)

    # def edit_answers_model(self, data):
    #     type = "answer"
    #     questionId = data['questionId']
    #     userId = data['userId']
    #     val1 = data['val1']
    #     sortKey = str(type + "#" + questionId + "#" + userId)
    #     data: object = dynamodb_connector_model.__connected_table__.query(
    #         KeyConditionExpression=Key('type').eq(type) & Key('sortKey').begins_with(sortKey)
    #     )
    #     for i in data["Items"]:
    #         try:
    #             if i['status'] == '1':
    #                 data: object = dynamodb_connector_model.__connected_table__.update_item(
    #                     Key={'type': type, 'sortKey': sortKey},
    #                     UpdateExpression="SET answer=:val",
    #                     ExpressionAttributeValues={':val': val1},
    #                     ReturnValues="UPDATED_NEW"
    #                 )
    #                 return json.dumps(data['Attributes'])
    #             else:
    #                 return json.dumps({"message": "No question found for the particular questionId"})
    #         except Exception as e:
    #             return json.dumps("status key not found")

    def edit_answers_model(self, data):
        type = "answer"
        questionId = data['questionId']
        userId = data['userId']
        val1 = data['val1']
        sortKey = str(type + "#" + questionId + "#" + userId)
        data: object = dynamodb_connector_model.__connected_table__.query(
            KeyConditionExpression=Key('type').eq(type) & Key('sortKey').begins_with(sortKey),
            FilterExpression=Attr('status').contains('1')
        )
        for i in data["Items"]:
            try:
                # if i['status'] == '1':
                #     data: object = dynamodb_connector_model.__connected_table__.update_item(
                #         Key={'type': type, 'sortKey': sortKey},
                #         UpdateExpression="SET answer=:val",
                #         ExpressionAttributeValues={':val': val1},
                #         ReturnValues="UPDATED_NEW"
                #     )
                #     return json.dumps(data['Attributes'])
                # else:
                #     return json.dumps({"message": "No question found for the particular questionId"})
                data = dynamodb_connector_model.__connected_table__.update_item(
                    Key={'type': type, 'sortKey': sortKey},
                    UpdateExpression="SET answer=:val",
                    ExpressionAttributeValues={':val': val1},
                    ReturnValues="UPDATED_NEW"
                )
                return json.dumps(data['Attributes'])
            except Exception as e:
                return json.dumps("status key not found")

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
        data = dynamodb_connector_model.__connected_table__.query(
            KeyConditionExpression=Key('type').eq(type1) & Key('sortKey').begins_with(sortKey_begins_with)
        )
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
        if data['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(data)
            response = {
                "message": "Question Deleted Successfully"
            }
            return json.dumps(response)
