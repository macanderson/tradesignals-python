# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ExpiryListParams"]


class ExpiryListParams(TypedDict, total=False):
    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """Date to filter the Greek flow data. ISO 8601 format."""

    expiration: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """Option expiration date. ISO 8601 format."""

    symbol: str
    """Stock symbol to filter the Greek flow data."""
