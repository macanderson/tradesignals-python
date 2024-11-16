# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .etf_holding import EtfHolding

__all__ = ["HoldingListResponse"]

HoldingListResponse: TypeAlias = List[EtfHolding]
