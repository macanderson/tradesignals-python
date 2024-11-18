# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .option_expiration_data import OptionExpirationData

__all__ = ["OptionExpirationDataResponse"]


class OptionExpirationDataResponse(BaseModel):
    data: Optional[List[OptionExpirationData]] = None
