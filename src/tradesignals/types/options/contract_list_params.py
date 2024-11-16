# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ContractListParams"]


class ContractListParams(TypedDict, total=False):
    symbol: Required[str]
    """Stock symbol to filter option contracts."""

    expiration: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Option expiration date to filter contracts."""

    option_type: Annotated[Literal["CALL", "PUT"], PropertyInfo(alias="optionType")]
    """Option type (CALL or PUT) to filter contracts."""

    strike: float
    """Option strike price to filter contracts."""
