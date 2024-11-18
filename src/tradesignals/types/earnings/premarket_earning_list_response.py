# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .premarket_earnings_data import PremarketEarningsData

__all__ = ["PremarketEarningListResponse"]

PremarketEarningListResponse: TypeAlias = List[PremarketEarningsData]
