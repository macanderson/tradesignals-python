# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TickerOptionContractListParams"]


class TickerOptionContractListParams(TypedDict, total=False):
    exclude_zero_dte: bool
    """Exclude chains expiring the same day."""

    exclude_zero_oi_chains: bool
    """Exclude chains where open interest is zero."""

    exclude_zero_vol_chains: bool
    """Exclude chains where volume is zero."""

    expiry: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Filter by expiry date."""

    limit: int
    """The number of items to return. Minimum is 1."""

    maybe_otm_only: bool
    """Include only out-of-the-money chains."""

    option_type: Literal["call", "put"]
    """Filter by option type (call/put)."""

    vol_greater_oi: bool
    """Include only chains where volume > open interest."""
