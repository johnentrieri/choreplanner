import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.planner import Planner  # noqa: E501
from openapi_server import util


def create_planner(planner):  # noqa: E501
    """Create new Planner

    Create new Planner # noqa: E501

    :param planner: Update Planner Settings
    :type planner: dict | bytes

    :rtype: Union[Planner, Tuple[Planner, int], Tuple[Planner, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        planner = Planner.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_planner(planner_id):  # noqa: E501
    """Delete Planner by ID

    Delete Existing Planner Settings by ID # noqa: E501

    :param planner_id: ID of Planner to Update
    :type planner_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def read_planner(planner_id):  # noqa: E501
    """Get Planner by ID

    Request specific existing planner by ID # noqa: E501

    :param planner_id: ID of Planner to return
    :type planner_id: int

    :rtype: Union[Planner, Tuple[Planner, int], Tuple[Planner, int, Dict[str, str]]
    """
    return 'do some magic!'


def read_planners():  # noqa: E501
    """View all planners

    Request all Planners in Database # noqa: E501


    :rtype: Union[List[Planner], Tuple[List[Planner], int], Tuple[List[Planner], int, Dict[str, str]]
    """
    return 'do some magic!'


def update_planner(planner_id, planner):  # noqa: E501
    """Update Planner Settings by ID

    Change Existing Planner Settings by ID # noqa: E501

    :param planner_id: ID of Planner to Update
    :type planner_id: int
    :param planner: Update Planner Settings
    :type planner: dict | bytes

    :rtype: Union[Planner, Tuple[Planner, int], Tuple[Planner, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        planner = Planner.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
