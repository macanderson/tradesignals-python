# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SectorExposureListParams"]


class SectorExposureListParams(TypedDict, total=False):
    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """A date in the format of YYYY-MM-DD."""

    limit: int
    """How many items to return. Default 500. Max 500. Min 1."""
