# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .activity import Activity

__all__ = ["TradingActivityListResponse"]

TradingActivityListResponse: TypeAlias = List[Activity]
