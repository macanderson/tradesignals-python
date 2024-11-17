# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .group_greek_flow import GroupGreekFlow

__all__ = ["GreekFlowsByExpiryListResponse"]

GreekFlowsByExpiryListResponse: TypeAlias = List[GroupGreekFlow]
