# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .holdings import Holdings

__all__ = ["HoldingListResponse"]

HoldingListResponse: TypeAlias = List[Holdings]
