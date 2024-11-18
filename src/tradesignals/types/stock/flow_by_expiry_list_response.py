# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .expiration_order_flow import ExpirationOrderFlow

__all__ = ["FlowByExpiryListResponse"]

FlowByExpiryListResponse: TypeAlias = List[ExpirationOrderFlow]
