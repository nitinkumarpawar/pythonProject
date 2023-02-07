from service.question_model import question_model

obj = question_model()
from controller.question_controller import post_question_controller, getAnswer_by_questionId_controller, \
    getAll_question_by_userId_controller, edit_answers_controller, delete_question_controller
from unittest.mock import patch


@patch('service.question_model.question_model.post_questions_model')
@patch('builtins.input', side_effect=['quiz', 'test@gmail.com'])
# for testing 'if' clause:
def test_post_question_controller_1(input_mock, service_mock):
    service_mock.return_value = {"message": "Data Entered Successfully"}
    response = post_question_controller()
    assert response == {"message": "Data Entered Successfully"}


@patch('service.question_model.question_model.post_questions_model')
@patch('builtins.input', side_effect=['quiz', 'test@gmail'])
# for testing 'else' clause:
def test_post_question_controller_2(input_mock, service_mock):
    service_mock.return_value = {"message": "Invalid email id"}
    response = post_question_controller()
    assert response == {"message": "Invalid email id"}


@patch('service.question_model.question_model.getAnswer_by_questionId_model')
@patch('builtins.input', side_effect=['1'])
def test_getAnswer_by_questionId_controller(input_mock, service_mock):
    service_mock.return_value = {"data['ResponseMetadata']['HTTPStatusCode'] == 200"}
    response = getAnswer_by_questionId_controller()
    assert response == {"data['ResponseMetadata']['HTTPStatusCode'] == 200"}


@patch('service.question_model.question_model.getAll_question_by_userId_model')
@patch('builtins.input', side_effect=['nk@gmail.com'])
def test_getAll_question_by_userId_controller(input_mock, service_mock):
    service_mock.return_value = {"data['ResponseMetadata']['HTTPStatusCode'] == 200"}
    response = getAll_question_by_userId_controller()
    assert response == {"data['ResponseMetadata']['HTTPStatusCode'] == 200"}


@patch('service.question_model.question_model.edit_answers_model')
@patch('builtins.input', side_effect=['1', 'nk@gmail.com', 'new answer'])
def test_edit_answers_controller(input_mock, service_mock):
    service_mock.return_value = {"message": "answer updated"}
    response = edit_answers_controller()
    assert response == {"message": "answer updated"}


@patch('service.question_model.question_model.delete_question_model')
@patch('builtins.input', side_effect=['1', 'nk@gmail.com'])
def test_delete_question_controller(input_mock, service_mock):
    service_mock.return_value = {"message": "Question Deleted Successfully"}
    response = delete_question_controller()
    assert response == {"message": "Question Deleted Successfully"}
