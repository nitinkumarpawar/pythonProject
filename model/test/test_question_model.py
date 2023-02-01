from unittest.mock import MagicMock

from model import dynamodb_connector_model
from model.question_model import question_model

obj = dynamodb_connector_model


def test_post_questions_model(mocker):
    mock_put_item = MagicMock(return_value=None)
    mocker.patch.object(dynamodb_connector_model.__connected_table__, 'put_item', mock_put_item)
    data = {
        'question': 'test',
        'userId': 'nk@gmail.com'
    }
    question_model().post_questions_model(data)
    mock_put_item.assert_called_with(
        TableName='freshers_example',
        Item={
            'type': 'question',
            'sortKet': 'question#nk@gmail.com#id_db.hex',
            'question': 'test',
            'status': '1',
            'userId': 'nk@gmail.com'
        }
    )
