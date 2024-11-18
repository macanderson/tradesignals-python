# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .atm_chain_entry import AtmChainEntry

__all__ = ["AtmChainListResponse"]

AtmChainListResponse: TypeAlias = List[AtmChainEntry]
