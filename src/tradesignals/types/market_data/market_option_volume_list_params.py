# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MarketOptionVolumeListParams"]


class MarketOptionVolumeListParams(TypedDict, total=False):
    limit: int
    """How many items to return. Default is 1. Max is 500. Min is 1."""
