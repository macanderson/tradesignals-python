# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .congressional_trader_report import CongressionalTraderReport

__all__ = ["LateTradeReportListResponse"]

LateTradeReportListResponse: TypeAlias = List[CongressionalTraderReport]
