# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .ohlc_entry import OhlcEntry

__all__ = ["OhlcResponse"]

OhlcResponse: TypeAlias = List[OhlcEntry]
