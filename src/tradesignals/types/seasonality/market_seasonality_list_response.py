# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .seasonality_entry import SeasonalityEntry

__all__ = ["MarketSeasonalityListResponse"]

MarketSeasonalityListResponse: TypeAlias = List[SeasonalityEntry]
