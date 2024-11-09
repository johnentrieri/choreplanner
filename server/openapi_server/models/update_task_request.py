from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.task_instance import TaskInstance
from openapi_server import util

from openapi_server.models.task_instance import TaskInstance  # noqa: E501

class UpdateTaskRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, new_data=None):  # noqa: E501
        """UpdateTaskRequest - a model defined in OpenAPI

        :param new_data: The new_data of this UpdateTaskRequest.  # noqa: E501
        :type new_data: TaskInstance
        """
        self.openapi_types = {
            'new_data': TaskInstance
        }

        self.attribute_map = {
            'new_data': 'newData'
        }

        self._new_data = new_data

    @classmethod
    def from_dict(cls, dikt) -> 'UpdateTaskRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The updateTask_request of this UpdateTaskRequest.  # noqa: E501
        :rtype: UpdateTaskRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def new_data(self) -> TaskInstance:
        """Gets the new_data of this UpdateTaskRequest.


        :return: The new_data of this UpdateTaskRequest.
        :rtype: TaskInstance
        """
        return self._new_data

    @new_data.setter
    def new_data(self, new_data: TaskInstance):
        """Sets the new_data of this UpdateTaskRequest.


        :param new_data: The new_data of this UpdateTaskRequest.
        :type new_data: TaskInstance
        """

        self._new_data = new_data
