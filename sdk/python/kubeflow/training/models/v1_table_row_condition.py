# coding: utf-8

"""
    Kubeflow Training SDK

    Python SDK for Kubeflow Training  # noqa: E501

    The version of the OpenAPI document: v1.7.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubeflow.training.configuration import Configuration


class V1TableRowCondition(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'message': 'str',
        'reason': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'message': 'message',
        'reason': 'reason',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, message=None, reason=None, status='', type='', local_vars_configuration=None):  # noqa: E501
        """V1TableRowCondition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._message = None
        self._reason = None
        self._status = None
        self._type = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if reason is not None:
            self.reason = reason
        self.status = status
        self.type = type

    @property
    def message(self):
        """Gets the message of this V1TableRowCondition.  # noqa: E501

        Human readable message indicating details about last transition.  # noqa: E501

        :return: The message of this V1TableRowCondition.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1TableRowCondition.

        Human readable message indicating details about last transition.  # noqa: E501

        :param message: The message of this V1TableRowCondition.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def reason(self):
        """Gets the reason of this V1TableRowCondition.  # noqa: E501

        (brief) machine readable reason for the condition's last transition.  # noqa: E501

        :return: The reason of this V1TableRowCondition.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this V1TableRowCondition.

        (brief) machine readable reason for the condition's last transition.  # noqa: E501

        :param reason: The reason of this V1TableRowCondition.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def status(self):
        """Gets the status of this V1TableRowCondition.  # noqa: E501

        Status of the condition, one of True, False, Unknown.  # noqa: E501

        :return: The status of this V1TableRowCondition.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1TableRowCondition.

        Status of the condition, one of True, False, Unknown.  # noqa: E501

        :param status: The status of this V1TableRowCondition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def type(self):
        """Gets the type of this V1TableRowCondition.  # noqa: E501

        Type of row condition. The only defined value is 'Completed' indicating that the object this row represents has reached a completed state and may be given less visual priority than other rows. Clients are not required to honor any conditions but should be consistent where possible about handling the conditions.  # noqa: E501

        :return: The type of this V1TableRowCondition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1TableRowCondition.

        Type of row condition. The only defined value is 'Completed' indicating that the object this row represents has reached a completed state and may be given less visual priority than other rows. Clients are not required to honor any conditions but should be consistent where possible about handling the conditions.  # noqa: E501

        :param type: The type of this V1TableRowCondition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1TableRowCondition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1TableRowCondition):
            return True

        return self.to_dict() != other.to_dict()
