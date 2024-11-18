# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .atm_chain_entry import AtmChainEntry

__all__ = ["AtmChainsResponse"]


class AtmChainsResponse(BaseModel):
    data: Optional[List[AtmChainEntry]] = None
