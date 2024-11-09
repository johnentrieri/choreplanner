import unittest

from flask import json

from openapi_server.models.planner import Planner  # noqa: E501
from openapi_server.test import BaseTestCase


class TestChorePlannerController(BaseTestCase):
    """ChorePlannerController integration test stubs"""

    def test_create_planner(self):
        """Test case for create_planner

        Create new Planner
        """
        planner = {"plannerID":10,"performers":[{"color":"Red","name":"John","performerID":10,"email":"email"},{"color":"Red","name":"John","performerID":10,"email":"email"}],"taskRules":[{"summary":"Take Out the Garbage (Monday)","possibleAssignees":["John","John"],"firstAssignee":"John","weekday":"Any","taskRuleID":10,"firstWeek":5,"frequency":2},{"summary":"Take Out the Garbage (Monday)","possibleAssignees":["John","John"],"firstAssignee":"John","weekday":"Any","taskRuleID":10,"firstWeek":5,"frequency":2}],"numWeeks":52,"startDate":"2000-01-23","tasks":[{"summary":"Take Out the Garbage (Monday)","startWeek":4,"finishDate":"2000-01-23","assignee":"John","taskID":10,"status":"Open"},{"summary":"Take Out the Garbage (Monday)","startWeek":4,"finishDate":"2000-01-23","assignee":"John","taskID":10,"status":"Open"}]}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/planner',
            method='POST',
            headers=headers,
            data=json.dumps(planner),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_planner(self):
        """Test case for delete_planner

        Delete Planner by ID
        """
        headers = { 
        }
        response = self.client.open(
            '/planner/{planner_id}'.format(planner_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_planner(self):
        """Test case for read_planner

        Get Planner by ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/planner/{planner_id}'.format(planner_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_planners(self):
        """Test case for read_planners

        View all planners
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/planners',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_planner(self):
        """Test case for update_planner

        Update Planner Settings by ID
        """
        planner = {"plannerID":10,"performers":[{"color":"Red","name":"John","performerID":10,"email":"email"},{"color":"Red","name":"John","performerID":10,"email":"email"}],"taskRules":[{"summary":"Take Out the Garbage (Monday)","possibleAssignees":["John","John"],"firstAssignee":"John","weekday":"Any","taskRuleID":10,"firstWeek":5,"frequency":2},{"summary":"Take Out the Garbage (Monday)","possibleAssignees":["John","John"],"firstAssignee":"John","weekday":"Any","taskRuleID":10,"firstWeek":5,"frequency":2}],"numWeeks":52,"startDate":"2000-01-23","tasks":[{"summary":"Take Out the Garbage (Monday)","startWeek":4,"finishDate":"2000-01-23","assignee":"John","taskID":10,"status":"Open"},{"summary":"Take Out the Garbage (Monday)","startWeek":4,"finishDate":"2000-01-23","assignee":"John","taskID":10,"status":"Open"}]}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/planner/{planner_id}'.format(planner_id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(planner),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
