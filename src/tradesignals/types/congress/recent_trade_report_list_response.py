# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .congressional_trade import CongressionalTrade

__all__ = ["RecentTradeReportListResponse"]

RecentTradeReportListResponse: TypeAlias = List[CongressionalTrade]
