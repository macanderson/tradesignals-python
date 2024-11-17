# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .hottest_chain_entry import HottestChainEntry

__all__ = ["HottestChainsResponse"]


class HottestChainsResponse(BaseModel):
    data: Optional[List[HottestChainEntry]] = None
