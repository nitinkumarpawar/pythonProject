import json

from unittest.mock import MagicMock, patch

from service.question_model import question_model

obj1 = question_model()


@patch('service.dynamodb_connector_model.__connected_table__')
def test_post_questions_service(input_mock):
    data = {
        "question": "How are you?",
        "userId": "abcd@arrkgroup.com"
    }
    input_mock.put_item.return_value = {
        'ResponseMetadata': {'RequestId': 'HR1JTJGCFRJB688RDHH076DF77VV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200,
                             'HTTPHeaders': {'server': 'Server', 'date': 'Thu, 09 Feb 2023 10:30:11 GMT',
                                             'content-type': 'application/x-amz-json-1.0', 'content-length': '2',
                                             'connection': 'keep-alive',
                                             'x-amzn-requestid': 'HR1JTJGCFRJB688RDHH076DF77VV4KQNSO5AEMVJF66Q9ASUAAJG',
                                             'x-amz-crc32': '2745614147'}, 'RetryAttempts': 0}}
    response = obj1.post_questions_model(data)
    assert response == {"message": "Data Entered Successfully"}


@patch('service.dynamodb_connector_model.__connected_table__')
# for testing 'if' clause:
def test_getAll_answer_by_questionId_service_1(input_mock):
    data = {"questionId": "22"}
    query_result = {'Items': [], 'Count': 0, 'ScannedCount': 0,
                    'ResponseMetadata': {'RequestId': 'MBJSDAJOUJCM6C2UAP0BN71987VV4KQNSO5AEMVJF66Q9ASUAAJG',
                                         'HTTPStatusCode': 200,
                                         'HTTPHeaders': {'server': 'Server', 'date': 'Thu, 09 Feb 2023 09:54:06 GMT',
                                                         'content-type': 'application/x-amz-json-1.0',
                                                         'content-length': '39', 'connection': 'keep-alive',
                                                         'x-amzn-requestid': 'MBJSDAJOUJCM6C2UAP0BN71987VV4KQNSO5AEMVJF66Q9ASUAAJG',
                                                         'x-amz-crc32': '3413411624'}, 'RetryAttempts': 0}}
    input_mock.query.return_value = query_result
    response = obj1.getAnswer_by_questionId_model(data)
    assert response == {"message": "Data not found"}


@patch('service.dynamodb_connector_model.__connected_table__')
# for testing 'else' clause:
def test_getAll_answer_by_questionId_service_2(input_mock):
    data = {"questionId": "1"}
    query_result = {'Items': [
        {'sortKey': 'answer#1#priyanka@mailinator.com', 'userId': 'priyanka@mailinator.com', 'status': '1',
         'createdAt': '2022-01-11', 'answer': 'updated answer', 'type': 'answer'}], 'Count': 1, 'ScannedCount': 1,
        'ResponseMetadata': {'RequestId': 'SG0J2QHK0I2G883E885R0C342FVV4KQNSO5AEMVJF66Q9ASUAAJG',
                             'HTTPStatusCode': 200,
                             'HTTPHeaders': {'server': 'Server', 'date': 'Thu, 09 Feb 2023 10:04:18 GMT',
                                             'content-type': 'application/x-amz-json-1.0',
                                             'content-length': '236', 'connection': 'keep-alive',
                                             'x-amzn-requestid': 'SG0J2QHK0I2G883E885R0C342FVV4KQNSO5AEMVJF66Q9ASUAAJG',
                                             'x-amz-crc32': '3576652810'}, 'RetryAttempts': 0}}
    input_mock.query.return_value = query_result
    response = obj1.getAnswer_by_questionId_model(data)
    assert response == json.dumps({'Items': [
        {'sortKey': 'answer#1#priyanka@mailinator.com', 'userId': 'priyanka@mailinator.com', 'status': '1',
         'createdAt': '2022-01-11', 'answer': 'updated answer', 'type': 'answer'}], 'Count': 1, 'ScannedCount': 1,
        'ResponseMetadata': {
            'RequestId': 'SG0J2QHK0I2G883E885R0C342FVV4KQNSO5AEMVJF66Q9ASUAAJG',
            'HTTPStatusCode': 200,
            'HTTPHeaders': {'server': 'Server', 'date': 'Thu, 09 Feb 2023 10:04:18 GMT',
                            'content-type': 'application/x-amz-json-1.0',
                            'content-length': '236', 'connection': 'keep-alive',
                            'x-amzn-requestid': 'SG0J2QHK0I2G883E885R0C342FVV4KQNSO5AEMVJF66Q9ASUAAJG',
                            'x-amz-crc32': '3576652810'}, 'RetryAttempts': 0}})


@patch('service.dynamodb_connector_model.__connected_table__')
# for testing 'if' clause:
def test_getAll_question_by_userId_service_1(input_mock):
    data = {"userId": "jan_01@arrkgroup.com"}
    query_result = {'Items': [], 'Count': 0, 'ScannedCount': 0,
                    'ResponseMetadata': {'RequestId': 'MBJSDAJOUJCM6C2UAP0BN71987VV4KQNSO5AEMVJF66Q9ASUAAJG',
                                         'HTTPStatusCode': 200,
                                         'HTTPHeaders': {'server': 'Server', 'date': 'Thu, 09 Feb 2023 09:54:06 GMT',
                                                         'content-type': 'application/x-amz-json-1.0',
                                                         'content-length': '39', 'connection': 'keep-alive',
                                                         'x-amzn-requestid': 'MBJSDAJOUJCM6C2UAP0BN71987VV4KQNSO5AEMVJF66Q9ASUAAJG',
                                                         'x-amz-crc32': '3413411624'}, 'RetryAttempts': 0}}
    input_mock.query.return_value = query_result
    response = obj1.getAll_question_by_userId_model(data)
    assert response == {"message": "Data not found"}


@patch('service.dynamodb_connector_model.__connected_table__')
# for testing 'else' clause:
def test_getAll_question_by_userId_service_1(input_mock):
    data = {"userId": "priyanka.juwar@arrkgroup.com"}
    query_result = {'Items': [
        {'question': 'This is my new question', 'sortKey': 'question#priyanka.juwar@arrkgroup.com#1', 'questionId': '1',
         'userId': 'priyanka.juwar@arrkgroup.com', 'status': '1', 'createdAt': '2022-12-12', 'type': 'question'},
        {'question': 'Explain Dynamodb?', 'sortKey': 'question#priyanka.juwar@arrkgroup.com#2', 'questionId': '2',
         'userId': 'priyanka.juwar@arrkgroup.com', 'status': '1', 'createdAt': '2022-12-12', 'type': 'question'}],
        'Count': 2, 'ScannedCount': 2,
        'ResponseMetadata': {'RequestId': '8NN6UQBEH07DKHIPDGJAOFC1ORVV4KQNSO5AEMVJF66Q9ASUAAJG',
                             'HTTPStatusCode': 200,
                             'HTTPHeaders': {'server': 'Server', 'date': 'Thu, 09 Feb 2023 10:16:16 GMT',
                                             'content-type': 'application/x-amz-json-1.0',
                                             'content-length': '524', 'connection': 'keep-alive',
                                             'x-amzn-requestid': '8NN6UQBEH07DKHIPDGJAOFC1ORVV4KQNSO5AEMVJF66Q9ASUAAJG',
                                             'x-amz-crc32': '1758263636'}, 'RetryAttempts': 0}}
    input_mock.query.return_value = query_result
    response = obj1.getAll_question_by_userId_model(data)
    assert response == json.dumps({'Items': [
        {'question': 'This is my new question', 'sortKey': 'question#priyanka.juwar@arrkgroup.com#1', 'questionId': '1',
         'userId': 'priyanka.juwar@arrkgroup.com', 'status': '1', 'createdAt': '2022-12-12', 'type': 'question'},
        {'question': 'Explain Dynamodb?', 'sortKey': 'question#priyanka.juwar@arrkgroup.com#2', 'questionId': '2',
         'userId': 'priyanka.juwar@arrkgroup.com', 'status': '1', 'createdAt': '2022-12-12', 'type': 'question'}],
        'Count': 2, 'ScannedCount': 2, 'ResponseMetadata': {
            'RequestId': '8NN6UQBEH07DKHIPDGJAOFC1ORVV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200,
            'HTTPHeaders': {'server': 'Server', 'date': 'Thu, 09 Feb 2023 10:16:16 GMT',
                            'content-type': 'application/x-amz-json-1.0', 'content-length': '524',
                            'connection': 'keep-alive',
                            'x-amzn-requestid': '8NN6UQBEH07DKHIPDGJAOFC1ORVV4KQNSO5AEMVJF66Q9ASUAAJG',
                            'x-amz-crc32': '1758263636'}, 'RetryAttempts': 0}})


@patch('service.dynamodb_connector_model.__connected_table__')
def test_edit_answers_service(input_mock):
    data = {
        "questionId": "2",
        "userId": "jan_01@arrkgroup.com",
        "val1": "updated answer"
    }
    response = {"answer": "updated answer"}
    query_result = {'Items': [
        {'sortKey': 'answer#2#jan_01@arrkgroup.com', 'userId': 'jan_01@arrkgroup.com', 'status': '1',
         'createdAt': '2022-11-01', 'type': 'answer',
         'answer': 'NoSQL database service that supports key–value and document data structures'}], 'Count': 1,
        'ScannedCount': 1,
        'ResponseMetadata': {'RequestId': '018MUBCF3O83H9DEP2U4S2AT7JVV4KQNSO5AEMVJF66Q9ASUAAJG',
                             'HTTPStatusCode': 200,
                             'HTTPHeaders': {'server': 'Server', 'date': 'Thu, 09 Feb 2023 09:22:38 GMT',
                                             'content-type': 'application/x-amz-json-1.0',
                                             'content-length': '293', 'connection': 'keep-alive',
                                             'x-amzn-requestid': '018MUBCF3O83H9DEP2U4S2AT7JVV4KQNSO5AEMVJF66Q9ASUAAJG',
                                             'x-amz-crc32': '3201606822'}, 'RetryAttempts': 0}}
    input_mock.query.return_value = query_result
    input_mock.update_item.return_value = response
    response = obj1.edit_answers_model(data)
    assert response == json.dumps({"message": "updated answer"})


@patch('service.dynamodb_connector_model.__connected_table__')
def test_delete_question_service(input_mock):
    data = {
        "questionId": "1",
        "userId": "nk@gmail.com"
    }

    response = {"message": "Question Deleted Successfully"}
    input_mock.update_item.return_value = response

    result = {
        "Items": [{'sortKey': 'answer#1#priyanka@mailinator.com', 'userId': 'priyanka@mailinator.com', 'status': '1',
                   'createdAt': '2022-01-11',
                   'answer': 'Amazon API Gateway is an AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs at any scale',
                   'type': 'answer'}], 'Count': 1, 'ScannedCount': 1,
        'ResponseMetadata': {'RequestId': '3GNSO3L0DLLFBB4R3F79TRJ8FVVV4KQNSO5AEMVJF66Q9ASUAAJG',
                             'HTTPStatusCode': 200,
                             'HTTPHeaders': {'server': 'Server', 'date': 'Thu, 09 Feb 2023 07:22:42 GMT',
                                             'content-type': 'application/x-amz-json-1.0', 'content-length': '366',
                                             'connection': 'keep-alive',
                                             'x-amzn-requestid': '3GNSO3L0DLLFBB4R3F79TRJ8FVVV4KQNSO5AEMVJF66Q9ASUAAJG',
                                             'x-amz-crc32': '1114440167'}, 'RetryAttempts': 0}}

    input_mock.query.return_value = result

    response = obj1.delete_question_model(data)
    assert response == json.dumps({"message": "Question Deleted Successfully"})
