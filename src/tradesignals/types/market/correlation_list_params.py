# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CorrelationListParams"]


class CorrelationListParams(TypedDict, total=False):
    tickers: Required[str]
    """A comma-separated list of tickers.

    To exclude certain tickers, prefix the first ticker with a `-`.
    """

    interval: str
    """The timeframe of the data to return. Allowed formats:

    - YTD
    - 1D, 2D, etc.
    - 1W, 2W, etc.
    - 1M, 2M, etc.
    - 1Y, 2Y, etc.
    """
