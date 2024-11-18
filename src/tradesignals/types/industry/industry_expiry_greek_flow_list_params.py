# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["IndustryExpiryGreekFlowListParams"]


class IndustryExpiryGreekFlowListParams(TypedDict, total=False):
    flow_group: Required[
        Literal[
            "airline",
            "bank",
            "basic materials",
            "china",
            "communication services",
            "consumer cyclical",
            "consumer defensive",
            "crypto",
            "cyber",
            "energy",
            "financial services",
            "gas",
            "gold",
            "healthcare",
            "industrials",
            "mag7",
            "oil",
            "real estate",
            "refiners",
            "reit",
            "semi",
            "silver",
            "technology",
            "uranium",
            "utilities",
        ]
    ]

    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """A trading date in the format of YYYY-MM-DD.

    This is optional and by default the last trading date.
    """
