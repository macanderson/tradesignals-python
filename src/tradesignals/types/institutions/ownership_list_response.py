# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .institution_ownership import InstitutionOwnership

__all__ = ["OwnershipListResponse"]

OwnershipListResponse: TypeAlias = List[InstitutionOwnership]
