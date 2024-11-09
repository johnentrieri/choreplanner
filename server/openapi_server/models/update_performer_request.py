from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.performer import Performer
from openapi_server import util

from openapi_server.models.performer import Performer  # noqa: E501

class UpdatePerformerRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, new_data=None):  # noqa: E501
        """UpdatePerformerRequest - a model defined in OpenAPI

        :param new_data: The new_data of this UpdatePerformerRequest.  # noqa: E501
        :type new_data: Performer
        """
        self.openapi_types = {
            'new_data': Performer
        }

        self.attribute_map = {
            'new_data': 'newData'
        }

        self._new_data = new_data

    @classmethod
    def from_dict(cls, dikt) -> 'UpdatePerformerRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The updatePerformer_request of this UpdatePerformerRequest.  # noqa: E501
        :rtype: UpdatePerformerRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def new_data(self) -> Performer:
        """Gets the new_data of this UpdatePerformerRequest.


        :return: The new_data of this UpdatePerformerRequest.
        :rtype: Performer
        """
        return self._new_data

    @new_data.setter
    def new_data(self, new_data: Performer):
        """Sets the new_data of this UpdatePerformerRequest.


        :param new_data: The new_data of this UpdatePerformerRequest.
        :type new_data: Performer
        """

        self._new_data = new_data