# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .analyst_rating_entry import AnalystRatingEntry

__all__ = ["RatingListResponse"]

RatingListResponse: TypeAlias = List[AnalystRatingEntry]
