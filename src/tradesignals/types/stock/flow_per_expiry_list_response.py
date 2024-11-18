# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .expiry_flow import ExpiryFlow

__all__ = ["FlowPerExpiryListResponse"]

FlowPerExpiryListResponse: TypeAlias = List[ExpiryFlow]
