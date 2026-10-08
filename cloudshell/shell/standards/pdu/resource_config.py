from __future__ import annotations

from attrs import define
from attrs.validators import ge

from cloudshell.shell.standards import attribute_names as attr_name
from cloudshell.shell.standards.core.resource_conf import BaseConfig, attr
from cloudshell.shell.standards.resource_config_generic_models import (
    GenericCLIConfig,
    GenericConsoleServerConfig,
    GenericSnmpConfig,
)

from cloudshell.shell.standards.pdu import attribute_names as api_attr_name


@define(slots=False, str=False)
class PDUResourceConfig(
    GenericSnmpConfig, GenericCLIConfig, GenericConsoleServerConfig
):
    ...


@define(slots=False, str=False)
class RESTAPIPDUResourceConfig(BaseConfig):
    api_user: str = attr(attr_name.USER)
    api_password: str = attr(attr_name.PASSWORD, is_password=True)
    api_port: int = attr(api_attr_name.API_PORT, validator=ge(0))
    api_scheme: str = attr(api_attr_name.API_SCHEME)
