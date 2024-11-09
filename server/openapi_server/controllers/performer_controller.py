import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.performer import Performer  # noqa: E501
from openapi_server.models.planner import Planner  # noqa: E501
from openapi_server.models.update_performer_request import UpdatePerformerRequest  # noqa: E501
from openapi_server import util


def add_performer(planner_id, performer):  # noqa: E501
    """Add Performer to a Planner

    Adds new Performer to Existing Planner by Planner ID # noqa: E501

    :param planner_id: ID of Planner to Update
    :type planner_id: int
    :param performer: Create Performer
    :type performer: dict | bytes

    :rtype: Union[Planner, Tuple[Planner, int], Tuple[Planner, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        performer = Performer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_performer(planner_id, performer_id):  # noqa: E501
    """Delete Performer from Planner

    Deletes Existing Performer from a Planner # noqa: E501

    :param planner_id: ID of Planner to Update
    :type planner_id: int
    :param performer_id: ID of Performer to Delete
    :type performer_id: int

    :rtype: Union[Planner, Tuple[Planner, int], Tuple[Planner, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_performer(planner_id, performer_id, update_performer_request):  # noqa: E501
    """Update Performer within a Planner

    Updates Existing Performer within a Planner # noqa: E501

    :param planner_id: ID of Planner to Update
    :type planner_id: int
    :param performer_id: ID of Performer to Update
    :type performer_id: int
    :param update_performer_request: Update Performer Data
    :type update_performer_request: dict | bytes

    :rtype: Union[Planner, Tuple[Planner, int], Tuple[Planner, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        update_performer_request = UpdatePerformerRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
