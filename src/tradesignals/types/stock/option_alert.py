# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OptionAlert"]


class OptionAlert(BaseModel):
    alert_rule: Optional[str] = None

    all_opening_trades: Optional[bool] = None

    created_at: Optional[datetime] = None

    expiry: Optional[date] = None

    expiry_count: Optional[int] = None

    has_floor: Optional[bool] = None

    has_multileg: Optional[bool] = None

    has_singleleg: Optional[bool] = None

    has_sweep: Optional[bool] = None

    open_interest: Optional[str] = None

    option_chain: Optional[str] = None

    price: Optional[str] = None

    strike: Optional[str] = None

    ticker: Optional[str] = None

    total_ask_side_prem: Optional[str] = None

    total_bid_side_prem: Optional[str] = None

    total_premium: Optional[str] = None

    total_size: Optional[int] = None

    trade_count: Optional[int] = None

    type: Optional[Literal["call", "put"]] = None

    underlying_price: Optional[str] = None

    volume: Optional[int] = None

    volume_oi_ratio: Optional[str] = None
