# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CorrelationRetrieveResponse"]


class CorrelationRetrieveResponse(BaseModel):
    correlation_matrix: Optional[List[List[float]]] = FieldInfo(alias="correlationMatrix", default=None)

    symbols: Optional[List[str]] = None
