from unittest.mock import MagicMock

import pytest
import controller
import service
from controller import question_controller
from controller.question_controller import post_question_controller
from service.question_model import question_model
obj = question_model()
from controller.question_controller import post_question_controller
from unittest.mock import patch

@patch('service.question_model.question_model.post_questions_model')
@patch('builtins.input', side_effect=['quiz','test@gmail.com'])
def test_post_question_controller(input_mock, service_mock):
    service_mock.return_value = 'response'
    response = post_question_controller()
    # mock_service.assert_called_once_with()
    assert response.status_code == 200
