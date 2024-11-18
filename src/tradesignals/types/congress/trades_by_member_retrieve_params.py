# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TradesByMemberRetrieveParams"]


class TradesByMemberRetrieveParams(TypedDict, total=False):
    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """A trading date in the format of YYYY-MM-DD.

    This is optional and by default the last trading date.
    """

    limit: int
    """How many items to return"""

    name: str
    """The full name of a congress member.

    Cannot contain digits/numbers. Spaces need to be replaced with either '+' or
    '%20'. Defaults to Nancy Pelosi.
    """
