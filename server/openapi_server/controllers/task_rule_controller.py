import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.planner import Planner  # noqa: E501
from openapi_server.models.task_rule import TaskRule  # noqa: E501
from openapi_server.models.update_task_rule_request import UpdateTaskRuleRequest  # noqa: E501
from openapi_server import util


def add_task_rule(planner_id, task_rule):  # noqa: E501
    """Add Task Rule to a Planner

    Adds new Task Rule to Existing Planner by Planner ID # noqa: E501

    :param planner_id: ID of Planner to Update
    :type planner_id: int
    :param task_rule: Create Task Rule
    :type task_rule: dict | bytes

    :rtype: Union[Planner, Tuple[Planner, int], Tuple[Planner, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        task_rule = TaskRule.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_task_rule(planner_id, task_rule_id):  # noqa: E501
    """Delete Task Rule from Planner

    Deletes Existing Task Rule from a Planner # noqa: E501

    :param planner_id: ID of Planner to Update
    :type planner_id: int
    :param task_rule_id: ID of Task Rule to Delete
    :type task_rule_id: int

    :rtype: Union[Planner, Tuple[Planner, int], Tuple[Planner, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_task_rule(planner_id, task_rule_id, update_task_rule_request):  # noqa: E501
    """Update Task Rule within a Planner

    Updates Existing Taske Rule within a Planner # noqa: E501

    :param planner_id: ID of Planner to Update
    :type planner_id: int
    :param task_rule_id: ID of Task Rule to Update
    :type task_rule_id: int
    :param update_task_rule_request: Update Task Rule Data
    :type update_task_rule_request: dict | bytes

    :rtype: Union[Planner, Tuple[Planner, int], Tuple[Planner, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        update_task_rule_request = UpdateTaskRuleRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
