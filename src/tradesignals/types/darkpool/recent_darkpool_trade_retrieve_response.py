# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..shared.darkpool_trade import DarkpoolTrade

__all__ = ["RecentDarkpoolTradeRetrieveResponse"]

RecentDarkpoolTradeRetrieveResponse: TypeAlias = List[DarkpoolTrade]
