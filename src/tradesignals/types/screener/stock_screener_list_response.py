# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .stock_entry import StockEntry

__all__ = ["StockScreenerListResponse"]

StockScreenerListResponse: TypeAlias = List[StockEntry]
