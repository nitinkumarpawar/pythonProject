import json
from unittest import mock

from boto3.dynamodb.conditions import Key, Attr

from unittest.mock import MagicMock
import boto3 as boto3

from service import dynamodb_connector_model
from service.question_model import question_model

obj1 = question_model()


def test_post_questions_model(mocker):
    mock_put_item = MagicMock()
    mocker.patch.object(dynamodb_connector_model.__connected_table__, 'put_item', mock_put_item)
    data = {
        'question': 'test',
        'userId': 'nk@gmail.com'
    }
    obj1.post_questions_model(data)
    mock_put_item.assert_called_with(
        TableName='freshers-example',
        Item={
            'type': 'question',
            'sortKey': 'question#nk@gmail.com#5000',
            'question': 'test',
            'questionId': '5000',
            'status': '1',
            'userId': 'nk@gmail.com'
        }
    )


def test_getAnswer_by_questionId_model(mocker):
    mock_query_item = MagicMock()
    mocker.patch.object(dynamodb_connector_model.__connected_table__, 'query', mock_query_item)
    data = {
        'questionId': '5000'
    }
    obj1.getAnswer_by_questionId_model(data)
    mock_query_item.assert_called_with(
        KeyConditionExpression=Key('type').eq('answer') & Key('sortKey').begins_with('answer#5000'),
        FilterExpression=Attr('status').contains('1')
    )


def test_getAll_question_by_userId_model(mocker):
    mock_query_item = MagicMock()
    mocker.patch.object(dynamodb_connector_model.__connected_table__, 'query', mock_query_item)
    data = {
        'userId': 'nk@gmail.com'
    }
    obj1.getAll_question_by_userId_model(data)
    mock_query_item.assert_called_with(
        KeyConditionExpression=Key('type').eq('question') & Key('sortKey').begins_with('question#nk@gmail.com'),
        FilterExpression=Attr('status').contains('1')
    )


def test_edit_answers_model(mocker):
    mock_query_item = MagicMock()
    mocker.patch.object(dynamodb_connector_model.__connected_table__, 'query', mock_query_item)
    data = {
        'questionId': '1',
        'userId': 'nk@gmail.com',
        'val1': 'updated answer'
    }
    obj1.edit_answers_model(data)
    mock_query_item.assert_called_with(
        KeyConditionExpression=Key('type').eq('answer') & Key('sortKey').begins_with('answer#1#nk@gmail.com'),
        FilterExpression=Attr('status').contains('1')
    )
    for i in mock_query_item['Items']:
        mock_update_item = MagicMock()
        mocker.patch.object(dynamodb_connector_model.__connected_table__, 'update_item', mock_update_item)
        obj1.edit_answers_model(data)
        mock_update_item.assert_called_with(
            Key={'type': 'answer', 'sortKey': 'answer#nk@gmail.com#1'},
            UpdateExpression="SET answer=:val",
            ExpressionAttributeValues={':val': 'updated answer'},
            ReturnValues="UPDATED_NEW"
        )


def test_delete_question_model(mocker):
    mock_update_item = MagicMock()
    mocker.patch.object(dynamodb_connector_model.__connected_table__, 'update_item', mock_update_item)
    data = {
        'questionId': '1',
        'userId': 'nk@gmail.com'
    }
    obj1.delete_question_model(data)
    mock_update_item.assert_called_with(
        Key={'type': 'question', 'sortKey': 'question#nk@gmail.com#1'},
        UpdateExpression='SET #ts = :val1',
        ExpressionAttributeValues={
            ":val1": '0'
        },
        ExpressionAttributeNames={
            "#ts": "status"
        },
        ReturnValues="UPDATED_NEW"
    )
    mocker_query_item = MagicMock()
    mocker.patch.object(dynamodb_connector_model.__connected_table__, 'query', mocker_query_item)
    mocker_query_item.assert_called_with(
        KeyConditionExpression=Key('type').eq('answer') & Key('sortKey').begins_with('answer#1')
    )
    for res in mocker_query_item['Items']:
        mock_update_item = MagicMock()
        mocker.patch.object(dynamodb_connector_model.__connected_table__, 'update_item', mock_update_item)
        sortKey1 = str('answer' + "#" + '1' + "#" + res['userId'])
        # obj1.delete_question_model(data)
        mock_update_item.assert_called_with(
            Key={'type': 'answer', 'sortKey': sortKey1},
            UpdateExpression='SET #ts = :val1',
            ExpressionAttributeValues={
                ":val1": '0'
            },
            ExpressionAttributeNames={
                "#ts": "status"
            },
            ReturnValues="UPDATED_NEW"
        )

#
