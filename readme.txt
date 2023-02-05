1. Pytest:
    pytest-mock is a plugin for pytest that provides a simple interface for mocking objects in Python.
    The MagicMock class from the unittest.mock library is a key component of this plugin.
    https://docs.python.org/3/library/unittest.mock.html

    #Example:
        from unittest import TestCase
        from unittest.mock import patch

        class MyTestCase(TestCase):
            @patch('my_module.dynamodb_connector.get_item', mock_get_item)
            def test_get_item(self):
                # Test code that uses the get_item operation
                ...

            @patch('my_module.dynamodb_connector.update_item', mock_update_item)
            def test_update_item(self):
                # Test code that uses the update_item operation
                ...

            @patch('my_module.dynamodb_connector.delete_item', mock_delete_item)
            def test_delete_item(self):
                # Test code that uses the delete_item operation
                ...

            @patch('my_module.dynamodb_connector.put_item', mock_put_item)
            def test_put_item(self):
                # Test code that uses the put_item operation

    #'mocker.patch.object':
        It is a method from the unittest.mock library (when using pytest_mock) in Python.
        It allows you to replace the behavior of an object dynamically, usually for the purposes of testing.
        In the context of testing, you can use mocker.patch.object to temporarily replace the behavior of a method
        or class with a mock object, which is a simplified version of the original object that you can control and
        manipulate for testing purposes.
        This allows you to isolate your tests and verify that the desired behavior occurs when the real object would
        have been used in a production environment.

    #'dynamodb' mock example:
        import unittest.mock
        import boto3
        import pytest

        def test_dynamodb_query(mocker):
            # mock the boto3 client for DynamoDB
            dynamodb = mocker.patch("boto3.client")

            # mock the query response
            dynamodb.return_value.query.return_value = {
                "Items": [
                    {"id": 1, "name": "Test Item 1"},
                    {"id": 2, "name": "Test Item 2"},
                ]
            }

            # mock the update response
            dynamodb.return_value.update_item.return_value = {}

            # mock the delete response
            dynamodb.return_value.delete_item.return_value = {}

            # mock the get response
            dynamodb.return_value.get_item.return_value = {
                "Item": {"id": 1, "name": "Test Item 1"}
            }

            # call the function that uses the DynamoDB client
            def query_items():
                dynamodb_client = boto3.client("dynamodb")
                response = dynamodb_client.query(
                    TableName="test-table",
                    KeyConditionExpression="id = :id",
                    ExpressionAttributeValues={":id": 1},
                )
                return response["Items"]

            def update_item(item_id, name):
                dynamodb_client = boto3.client("dynamodb")
                dynamodb_client.update_item(
                    TableName="test-table",
                    Key={"id": item_id},
                    UpdateExpression="SET name = :name",
                    ExpressionAttributeValues={":name": name},
                )

            def delete_item(item_id):
                dynamodb_client = boto3.client("dynamodb")
                dynamodb_client.delete_item(
                    TableName="test-table",
                    Key={"id": item_id},
                )

            def get_item(item_id):
                dynamodb_client = boto3.client("dynamodb")
                response = dynamodb_client.get_item(
                    TableName="test-table",
                    Key={"id": item_id},
                )
                return response.get("Item", None)

            # test the query operation
            items = query_items()
            assert len(items) == 2
            assert items[0]["id"] == 1
            assert items[0]["name"] == "Test Item 1"
            assert items[1]["id"] == 2
            assert items[1]["name"] == "Test Item 2"

            # test the update operation
            update_item(1, "Updated Test Item 1")
            updated_item = get_item(1)
            assert updated_item["id"] == 1
            assert updated_item["name"] == "Updated Test Item 1"

            # test the delete operation
            delete_item(1)
            deleted_item = get_item(1)
            assert deleted_item is None

    #'call_args_list':
        It is a property of a MagicMock object in Python that contains a list of all the calls made to the mock object.
        Each call is represented as a tuple of positional arguments, keyword arguments, and any other information
        related to the call. The list is stored in the order that the calls were made.
