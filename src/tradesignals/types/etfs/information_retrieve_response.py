# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .etf_info import EtfInfo

__all__ = ["InformationRetrieveResponse"]

InformationRetrieveResponse: TypeAlias = List[EtfInfo]
