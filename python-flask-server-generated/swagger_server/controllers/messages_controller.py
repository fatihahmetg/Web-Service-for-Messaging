import connexion
import six

from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server import util


def add_message(body):  # noqa: E501
    """takes a message (a string) as a POST and returns the SHA256 hash digest of that message (in hexadecimal format)

     # noqa: E501

    :param body: message that will be stored
    :type body: dict | bytes

    :rtype: Hash
    """
    if connexion.request.is_json:
        body = Message.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_msg_by_hash(hash):  # noqa: E501
    """Find the message by hash

    Returns the message # noqa: E501

    :param hash: Hash of the message to return
    :type hash: str

    :rtype: Message
    """
    return 'do some magic!'
