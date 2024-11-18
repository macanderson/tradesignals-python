# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .option_alert import OptionAlert

__all__ = ["OptionAlertResponse"]


class OptionAlertResponse(BaseModel):
    data: Optional[List[OptionAlert]] = None
