# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["IndustryExpiryGreekFlow"]


class IndustryExpiryGreekFlow(BaseModel):
    dir_delta_flow: Optional[str] = None
    """The directional delta flow."""

    dir_vega_flow: Optional[str] = None
    """The directional vega flow."""

    flow_group: Optional[str] = None
    """A flow group where the flow data for all tickers in that group are aggregated."""

    net_call_premium: Optional[str] = None
    """Defined as (call premium ask side) - (call premium bid side)."""

    net_call_volume: Optional[int] = None
    """Defined as (call volume ask side) - (call volume bid side)."""

    net_put_premium: Optional[str] = None
    """Defined as (put premium ask side) - (put premium bid side)."""

    net_put_volume: Optional[int] = None
    """Defined as (put volume ask side) - (put volume bid side)."""

    otm_dir_delta_flow: Optional[str] = None
    """The directional delta flow of out-of-the-money options."""

    otm_dir_vega_flow: Optional[str] = None
    """The directional vega flow of out-of-the-money options."""

    otm_total_delta_flow: Optional[str] = None
    """The total delta flow of out-of-the-money options."""

    otm_total_vega_flow: Optional[str] = None
    """The total vega flow of out-of-the-money options."""

    timestamp: Optional[datetime] = None
    """The (start of minute) timestamp of the data."""

    total_delta_flow: Optional[str] = None
    """The total delta flow."""

    total_vega_flow: Optional[str] = None
    """The total vega flow."""

    transactions: Optional[int] = None
    """The amount of transactions."""

    volume: Optional[int] = None
    """The total options volume."""
