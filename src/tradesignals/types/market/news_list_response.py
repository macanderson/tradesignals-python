# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["NewsListResponse", "News"]


class News(BaseModel):
    description: Optional[str] = None

    published_at: Optional[datetime] = None

    source: Optional[str] = None

    title: Optional[str] = None

    url: Optional[str] = None


class NewsListResponse(BaseModel):
    news: Optional[List[News]] = None
