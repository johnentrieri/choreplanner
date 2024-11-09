import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.planner import Planner  # noqa: E501
from openapi_server.models.task_instance import TaskInstance  # noqa: E501
from openapi_server.models.update_task_request import UpdateTaskRequest  # noqa: E501
from openapi_server import util


def add_task(planner_id, task_instance):  # noqa: E501
    """Add Task Rule to a Planner

    Adds new Task to Existing Planner by Planner ID # noqa: E501

    :param planner_id: ID of Planner to Update
    :type planner_id: int
    :param task_instance: Create TaskRule
    :type task_instance: dict | bytes

    :rtype: Union[Planner, Tuple[Planner, int], Tuple[Planner, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        task_instance = TaskInstance.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_task(planner_id, task_id):  # noqa: E501
    """Delete Task from Planner

    Deletes Existing Task from a Planner # noqa: E501

    :param planner_id: ID of Planner to Update
    :type planner_id: int
    :param task_id: ID of Task to Delete
    :type task_id: int

    :rtype: Union[Planner, Tuple[Planner, int], Tuple[Planner, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_task(planner_id, task_id, update_task_request):  # noqa: E501
    """Update Task within a Planner

    Updates Existing Task within a Planner # noqa: E501

    :param planner_id: ID of Planner to Update
    :type planner_id: int
    :param task_id: ID of Task to Update
    :type task_id: int
    :param update_task_request: Update Task Data
    :type update_task_request: dict | bytes

    :rtype: Union[Planner, Tuple[Planner, int], Tuple[Planner, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        update_task_request = UpdateTaskRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'