from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class TaskRule(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, task_rule_id=None, summary=None, frequency=None, first_week=None, first_assignee=None, possible_assignees=None, weekday=None):  # noqa: E501
        """TaskRule - a model defined in OpenAPI

        :param task_rule_id: The task_rule_id of this TaskRule.  # noqa: E501
        :type task_rule_id: int
        :param summary: The summary of this TaskRule.  # noqa: E501
        :type summary: str
        :param frequency: The frequency of this TaskRule.  # noqa: E501
        :type frequency: int
        :param first_week: The first_week of this TaskRule.  # noqa: E501
        :type first_week: int
        :param first_assignee: The first_assignee of this TaskRule.  # noqa: E501
        :type first_assignee: str
        :param possible_assignees: The possible_assignees of this TaskRule.  # noqa: E501
        :type possible_assignees: List[str]
        :param weekday: The weekday of this TaskRule.  # noqa: E501
        :type weekday: str
        """
        self.openapi_types = {
            'task_rule_id': int,
            'summary': str,
            'frequency': int,
            'first_week': int,
            'first_assignee': str,
            'possible_assignees': List[str],
            'weekday': str
        }

        self.attribute_map = {
            'task_rule_id': 'taskRuleID',
            'summary': 'summary',
            'frequency': 'frequency',
            'first_week': 'firstWeek',
            'first_assignee': 'firstAssignee',
            'possible_assignees': 'possibleAssignees',
            'weekday': 'weekday'
        }

        self._task_rule_id = task_rule_id
        self._summary = summary
        self._frequency = frequency
        self._first_week = first_week
        self._first_assignee = first_assignee
        self._possible_assignees = possible_assignees
        self._weekday = weekday

    @classmethod
    def from_dict(cls, dikt) -> 'TaskRule':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TaskRule of this TaskRule.  # noqa: E501
        :rtype: TaskRule
        """
        return util.deserialize_model(dikt, cls)

    @property
    def task_rule_id(self) -> int:
        """Gets the task_rule_id of this TaskRule.

        Task Rule ID  # noqa: E501

        :return: The task_rule_id of this TaskRule.
        :rtype: int
        """
        return self._task_rule_id

    @task_rule_id.setter
    def task_rule_id(self, task_rule_id: int):
        """Sets the task_rule_id of this TaskRule.

        Task Rule ID  # noqa: E501

        :param task_rule_id: The task_rule_id of this TaskRule.
        :type task_rule_id: int
        """

        self._task_rule_id = task_rule_id

    @property
    def summary(self) -> str:
        """Gets the summary of this TaskRule.


        :return: The summary of this TaskRule.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary: str):
        """Sets the summary of this TaskRule.


        :param summary: The summary of this TaskRule.
        :type summary: str
        """
        if summary is not None and len(summary) > 64:
            raise ValueError("Invalid value for `summary`, length must be less than or equal to `64`")  # noqa: E501
        if summary is not None and len(summary) < 3:
            raise ValueError("Invalid value for `summary`, length must be greater than or equal to `3`")  # noqa: E501

        self._summary = summary

    @property
    def frequency(self) -> int:
        """Gets the frequency of this TaskRule.

        How Often Task Should Be Performed, in weeks. Zero (0) indicates a one time task with no repetition.  # noqa: E501

        :return: The frequency of this TaskRule.
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency: int):
        """Sets the frequency of this TaskRule.

        How Often Task Should Be Performed, in weeks. Zero (0) indicates a one time task with no repetition.  # noqa: E501

        :param frequency: The frequency of this TaskRule.
        :type frequency: int
        """
        if frequency is not None and frequency > 52:  # noqa: E501
            raise ValueError("Invalid value for `frequency`, must be a value less than or equal to `52`")  # noqa: E501
        if frequency is not None and frequency < 0:  # noqa: E501
            raise ValueError("Invalid value for `frequency`, must be a value greater than or equal to `0`")  # noqa: E501

        self._frequency = frequency

    @property
    def first_week(self) -> int:
        """Gets the first_week of this TaskRule.

        First Week That Task Should Be Performed  # noqa: E501

        :return: The first_week of this TaskRule.
        :rtype: int
        """
        return self._first_week

    @first_week.setter
    def first_week(self, first_week: int):
        """Sets the first_week of this TaskRule.

        First Week That Task Should Be Performed  # noqa: E501

        :param first_week: The first_week of this TaskRule.
        :type first_week: int
        """
        if first_week is not None and first_week > 52:  # noqa: E501
            raise ValueError("Invalid value for `first_week`, must be a value less than or equal to `52`")  # noqa: E501
        if first_week is not None and first_week < 1:  # noqa: E501
            raise ValueError("Invalid value for `first_week`, must be a value greater than or equal to `1`")  # noqa: E501

        self._first_week = first_week

    @property
    def first_assignee(self) -> str:
        """Gets the first_assignee of this TaskRule.


        :return: The first_assignee of this TaskRule.
        :rtype: str
        """
        return self._first_assignee

    @first_assignee.setter
    def first_assignee(self, first_assignee: str):
        """Sets the first_assignee of this TaskRule.


        :param first_assignee: The first_assignee of this TaskRule.
        :type first_assignee: str
        """
        if first_assignee is not None and len(first_assignee) > 64:
            raise ValueError("Invalid value for `first_assignee`, length must be less than or equal to `64`")  # noqa: E501
        if first_assignee is not None and len(first_assignee) < 3:
            raise ValueError("Invalid value for `first_assignee`, length must be greater than or equal to `3`")  # noqa: E501

        self._first_assignee = first_assignee

    @property
    def possible_assignees(self) -> List[str]:
        """Gets the possible_assignees of this TaskRule.

        List of all Potential Assignees. Will Loop Through Assignee List Each Week.  # noqa: E501

        :return: The possible_assignees of this TaskRule.
        :rtype: List[str]
        """
        return self._possible_assignees

    @possible_assignees.setter
    def possible_assignees(self, possible_assignees: List[str]):
        """Sets the possible_assignees of this TaskRule.

        List of all Potential Assignees. Will Loop Through Assignee List Each Week.  # noqa: E501

        :param possible_assignees: The possible_assignees of this TaskRule.
        :type possible_assignees: List[str]
        """
        if possible_assignees is not None and len(possible_assignees) < 1:
            raise ValueError("Invalid value for `possible_assignees`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._possible_assignees = possible_assignees

    @property
    def weekday(self) -> str:
        """Gets the weekday of this TaskRule.

        Specific Day of the Week Task Must be Complete.  # noqa: E501

        :return: The weekday of this TaskRule.
        :rtype: str
        """
        return self._weekday

    @weekday.setter
    def weekday(self, weekday: str):
        """Sets the weekday of this TaskRule.

        Specific Day of the Week Task Must be Complete.  # noqa: E501

        :param weekday: The weekday of this TaskRule.
        :type weekday: str
        """
        allowed_values = ["Any", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]  # noqa: E501
        if weekday not in allowed_values:
            raise ValueError(
                "Invalid value for `weekday` ({0}), must be one of {1}"
                .format(weekday, allowed_values)
            )

        self._weekday = weekday