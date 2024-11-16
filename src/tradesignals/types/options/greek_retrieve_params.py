# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["GreekRetrieveParams"]


class GreekRetrieveParams(TypedDict, total=False):
    expiration: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Option expiration date to filter the greeks data."""

    option_type: Annotated[Literal["CALL", "PUT"], PropertyInfo(alias="optionType")]
    """Option type (CALL or PUT)."""

    strike: float
    """Option strike price to filter the greeks data."""
