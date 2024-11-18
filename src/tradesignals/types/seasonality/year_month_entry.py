# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["YearMonthEntry"]


class YearMonthEntry(BaseModel):
    change: Optional[float] = None

    close: Optional[str] = None

    month: Optional[int] = None

    open: Optional[str] = None

    year: Optional[int] = None
