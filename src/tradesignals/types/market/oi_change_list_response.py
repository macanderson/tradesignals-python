# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .oi_change_entry import OiChangeEntry

__all__ = ["OiChangeListResponse"]

OiChangeListResponse: TypeAlias = List[OiChangeEntry]
