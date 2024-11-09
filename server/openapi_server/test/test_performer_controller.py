import unittest

from flask import json

from openapi_server.models.performer import Performer  # noqa: E501
from openapi_server.models.planner import Planner  # noqa: E501
from openapi_server.models.update_performer_request import UpdatePerformerRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestPerformerController(BaseTestCase):
    """PerformerController integration test stubs"""

    def test_add_performer(self):
        """Test case for add_performer

        Add Performer to a Planner
        """
        performer = {"color":"Red","name":"John","performerID":10,"email":"email"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/planner/{planner_id}/performer'.format(planner_id=56),
            method='POST',
            headers=headers,
            data=json.dumps(performer),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_performer(self):
        """Test case for delete_performer

        Delete Performer from Planner
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/planner/{planner_id}/performer/{performer_id}'.format(planner_id=56, performer_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_performer(self):
        """Test case for update_performer

        Update Performer within a Planner
        """
        update_performer_request = openapi_server.UpdatePerformerRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/planner/{planner_id}/performer/{performer_id}'.format(planner_id=56, performer_id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(update_performer_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
