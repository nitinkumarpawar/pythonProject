import unittest

from model.dynamodb_connector_model import connection_test


def test_dynamodb_connector_model():
    assert connection_test() == "ACTIVE"
