# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .institution_holding import InstitutionHolding

__all__ = ["HoldingListResponse"]

HoldingListResponse: TypeAlias = List[InstitutionHolding]
