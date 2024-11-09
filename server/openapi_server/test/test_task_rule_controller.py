import unittest

from flask import json

from openapi_server.models.planner import Planner  # noqa: E501
from openapi_server.models.task_rule import TaskRule  # noqa: E501
from openapi_server.models.update_task_rule_request import UpdateTaskRuleRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTaskRuleController(BaseTestCase):
    """TaskRuleController integration test stubs"""

    def test_add_task_rule(self):
        """Test case for add_task_rule

        Add Task Rule to a Planner
        """
        task_rule = {"summary":"Take Out the Garbage (Monday)","possibleAssignees":["John","John"],"firstAssignee":"John","weekday":"Any","taskRuleID":10,"firstWeek":5,"frequency":2}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/planner/{planner_id}/taskRule'.format(planner_id=56),
            method='POST',
            headers=headers,
            data=json.dumps(task_rule),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_task_rule(self):
        """Test case for delete_task_rule

        Delete Task Rule from Planner
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/planner/{planner_id}/taskRule/{task_rule_id}'.format(planner_id=56, task_rule_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_task_rule(self):
        """Test case for update_task_rule

        Update Task Rule within a Planner
        """
        update_task_rule_request = openapi_server.UpdateTaskRuleRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/planner/{planner_id}/taskRule/{task_rule_id}'.format(planner_id=56, task_rule_id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(update_task_rule_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
