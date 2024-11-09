from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class Performer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, performer_id=None, name=None, email=None, color=None):  # noqa: E501
        """Performer - a model defined in OpenAPI

        :param performer_id: The performer_id of this Performer.  # noqa: E501
        :type performer_id: int
        :param name: The name of this Performer.  # noqa: E501
        :type name: str
        :param email: The email of this Performer.  # noqa: E501
        :type email: str
        :param color: The color of this Performer.  # noqa: E501
        :type color: str
        """
        self.openapi_types = {
            'performer_id': int,
            'name': str,
            'email': str,
            'color': str
        }

        self.attribute_map = {
            'performer_id': 'performerID',
            'name': 'name',
            'email': 'email',
            'color': 'color'
        }

        self._performer_id = performer_id
        self._name = name
        self._email = email
        self._color = color

    @classmethod
    def from_dict(cls, dikt) -> 'Performer':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Performer of this Performer.  # noqa: E501
        :rtype: Performer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def performer_id(self) -> int:
        """Gets the performer_id of this Performer.

        Performer ID  # noqa: E501

        :return: The performer_id of this Performer.
        :rtype: int
        """
        return self._performer_id

    @performer_id.setter
    def performer_id(self, performer_id: int):
        """Sets the performer_id of this Performer.

        Performer ID  # noqa: E501

        :param performer_id: The performer_id of this Performer.
        :type performer_id: int
        """

        self._performer_id = performer_id

    @property
    def name(self) -> str:
        """Gets the name of this Performer.


        :return: The name of this Performer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Performer.


        :param name: The name of this Performer.
        :type name: str
        """
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if name is not None and len(name) < 3:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")  # noqa: E501

        self._name = name

    @property
    def email(self) -> str:
        """Gets the email of this Performer.

        Performer Email Address  # noqa: E501

        :return: The email of this Performer.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this Performer.

        Performer Email Address  # noqa: E501

        :param email: The email of this Performer.
        :type email: str
        """

        self._email = email

    @property
    def color(self) -> str:
        """Gets the color of this Performer.

        Performer Color Code  # noqa: E501

        :return: The color of this Performer.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color: str):
        """Sets the color of this Performer.

        Performer Color Code  # noqa: E501

        :param color: The color of this Performer.
        :type color: str
        """
        allowed_values = ["Red", "Green", "Blue", "Orange", "Pink", "Purple", "Yellow"]  # noqa: E501
        if color not in allowed_values:
            raise ValueError(
                "Invalid value for `color` ({0}), must be one of {1}"
                .format(color, allowed_values)
            )

        self._color = color