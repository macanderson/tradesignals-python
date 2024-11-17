# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .expiry_breakdown_entry import ExpiryBreakdownEntry

__all__ = ["ExpiryBreakdownListResponse"]

ExpiryBreakdownListResponse: TypeAlias = List[ExpiryBreakdownEntry]
