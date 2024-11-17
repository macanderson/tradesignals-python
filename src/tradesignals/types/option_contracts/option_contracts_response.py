# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .option_contracts_entry import OptionContractsEntry

__all__ = ["OptionContractsResponse"]


class OptionContractsResponse(BaseModel):
    data: Optional[List[OptionContractsEntry]] = None
