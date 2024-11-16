# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InsiderTradeListParams"]


class InsiderTradeListParams(TypedDict, total=False):
    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """Date to filter insider trades."""

    insider: str
    """Name of the insider."""

    symbol: str
    """Stock symbol to filter insider trades."""

    transaction_type: Annotated[Literal["Buy", "Sell"], PropertyInfo(alias="transactionType")]
    """Type of transaction (Buy or Sell)."""
