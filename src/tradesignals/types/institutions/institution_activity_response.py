# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .institution_activity import InstitutionActivity

__all__ = ["InstitutionActivityResponse"]


class InstitutionActivityResponse(BaseModel):
    data: Optional[List[InstitutionActivity]] = None
