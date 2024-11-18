# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CongressMemberTrade"]


class CongressMemberTrade(BaseModel):
    amounts: Optional[str] = None
    """The reported amount range of the transaction."""

    filed_at_date: Optional[date] = None
    """The filing date as ISO date."""

    issuer: Optional[str] = None
    """The person who executed the transaction."""

    member_type: Optional[Literal["senate", "house", "other"]] = None
    """The type of person who executed the transaction."""

    notes: Optional[str] = None
    """Notes of the filing."""

    reporter: Optional[str] = None
    """The person who reported the transaction."""

    ticker: Optional[str] = None
    """The stock ticker."""

    transaction_date: Optional[date] = None
    """The transaction date as ISO date."""

    txn_type: Optional[
        Literal[
            "Buy",
            "Sell (partial)",
            "Purchase",
            "Sale (Partial)",
            "Receive",
            "Sale (Full)",
            "Sell (PARTIAL)",
            "Sell",
            "Exchange",
        ]
    ] = None
    """The transaction type."""
