# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OhlcListParams"]


class OhlcListParams(TypedDict, total=False):
    ticker: Required[str]

    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]

    end_date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]

    limit: int

    timeframe: str
    """The timeframe of the data to return. Allowed formats:

    - YTD
    - 1D, 2D, etc.
    - 1W, 2W, etc.
    - 1M, 2M, etc.
    - 1Y, 2Y, etc. Default: `1Y`
    """
