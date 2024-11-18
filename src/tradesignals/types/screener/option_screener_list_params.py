# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OptionScreenerListParams"]


class OptionScreenerListParams(TypedDict, total=False):
    expiry_dates: Annotated[List[Union[str, date]], PropertyInfo(format="iso8601")]

    is_otm: bool

    issue_types: List[Literal["Common Stock", "ETF", "Index", "ADR"]]

    max_daily_perc_change: float

    min_volume: int

    order: Literal["bid_ask_vol", "bull_bear_vol", "contract_pricing", "daily_perc_change", "volume"]

    order_direction: Literal["asc", "desc"]
