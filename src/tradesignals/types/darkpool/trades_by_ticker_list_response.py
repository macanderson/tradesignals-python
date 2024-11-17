# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..trade import Trade

__all__ = ["TradesByTickerListResponse"]

TradesByTickerListResponse: TypeAlias = List[Trade]
