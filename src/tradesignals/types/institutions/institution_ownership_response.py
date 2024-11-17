# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .institution_ownership import InstitutionOwnership

__all__ = ["InstitutionOwnershipResponse"]


class InstitutionOwnershipResponse(BaseModel):
    data: Optional[List[InstitutionOwnership]] = None
