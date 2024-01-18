import cloudshell.shell.standards.attribute_names as attribute_names
from cloudshell.shell.standards.autoload_generic_models import GenericResourceModel
from cloudshell.shell.standards.core.autoload.resource_model import (
    AbstractResource,
    ResourceAttribute,
)

__all__ = ["GenericResourceModel", "PDUPowerSocket", "PDUResourceModel"]

from cloudshell.shell.standards.core.namespace_type import NameSpaceType


class PDUPowerSocket(AbstractResource):
    _RESOURCE_MODEL = "PDUPowerSocket"
    _RELATIVE_ADDRESS_PREFIX = "PS"
    _NAME_TEMPLATE = "Power Socket {}"
    _FAMILY_NAME = "CS_PowerSocket"

    # Attributes
    model_name = ResourceAttribute(
        attribute_names.MODEL_NAME, NameSpaceType.FAMILY_NAME
    )


class PDUResourceModel(GenericResourceModel):
    SUPPORTED_FAMILY_NAMES = ["CS_PDU"]
    model_name = ResourceAttribute(
        attribute_names.MODEL_NAME, NameSpaceType.FAMILY_NAME
    )

    @property
    def entities(self):
        class _PDUEntities:
            PowerSocket = PDUPowerSocket

        return _PDUEntities
