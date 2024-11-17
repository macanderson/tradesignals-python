# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .sector_exposure import SectorExposure

__all__ = ["SectorListResponse"]

SectorListResponse: TypeAlias = List[SectorExposure]
