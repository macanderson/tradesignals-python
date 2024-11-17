# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .market_tide_entry import MarketTideEntry

__all__ = ["MarketTideListResponse"]

MarketTideListResponse: TypeAlias = List[MarketTideEntry]
