import unittest
from unittest.mock import MagicMock

from controller.question_controller import getAnswer_by_questionId_controller


def test_getAnswer_by_questionId_controller(app):
    mock_put_item = MagicMock()
    mocker.patch