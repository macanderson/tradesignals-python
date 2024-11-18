# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .monthly_average_entry import MonthlyAverageEntry

__all__ = ["MonthlySeasonalityListResponse"]

MonthlySeasonalityListResponse: TypeAlias = List[MonthlyAverageEntry]
