import unittest

from flask import json

from openapi_server.models.planner import Planner  # noqa: E501
from openapi_server.models.task_instance import TaskInstance  # noqa: E501
from openapi_server.models.update_task_request import UpdateTaskRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTaskController(BaseTestCase):
    """TaskController integration test stubs"""

    def test_add_task(self):
        """Test case for add_task

        Add Task Rule to a Planner
        """
        task_instance = {"summary":"Take Out the Garbage (Monday)","startWeek":4,"finishDate":"2000-01-23","assignee":"John","taskID":10,"status":"Open"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/planner/{planner_id}/task'.format(planner_id=56),
            method='POST',
            headers=headers,
            data=json.dumps(task_instance),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_task(self):
        """Test case for delete_task

        Delete Task from Planner
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/planner/{planner_id}/task/{task_id}'.format(planner_id=56, task_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_task(self):
        """Test case for update_task

        Update Task within a Planner
        """
        update_task_request = openapi_server.UpdateTaskRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/planner/{planner_id}/task/{task_id}'.format(planner_id=56, task_id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(update_task_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
