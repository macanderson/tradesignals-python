# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .flow_per_strike_intraday_entry import FlowPerStrikeIntradayEntry

__all__ = ["FlowPerStrikeIntradayResponse"]

FlowPerStrikeIntradayResponse: TypeAlias = List[FlowPerStrikeIntradayEntry]
