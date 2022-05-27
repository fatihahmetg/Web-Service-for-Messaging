# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Hash(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, digest: str=None):  # noqa: E501
        """Hash - a model defined in Swagger

        :param digest: The digest of this Hash.  # noqa: E501
        :type digest: str
        """
        self.swagger_types = {
            'digest': str
        }

        self.attribute_map = {
            'digest': 'digest'
        }
        self._digest = digest

    @classmethod
    def from_dict(cls, dikt) -> 'Hash':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Hash of this Hash.  # noqa: E501
        :rtype: Hash
        """
        return util.deserialize_model(dikt, cls)

    @property
    def digest(self) -> str:
        """Gets the digest of this Hash.


        :return: The digest of this Hash.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest: str):
        """Sets the digest of this Hash.


        :param digest: The digest of this Hash.
        :type digest: str
        """
        if digest is None:
            raise ValueError("Invalid value for `digest`, must not be `None`")  # noqa: E501

        self._digest = digest
