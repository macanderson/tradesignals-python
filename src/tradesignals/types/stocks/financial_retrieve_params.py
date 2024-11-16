# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FinancialRetrieveParams"]


class FinancialRetrieveParams(TypedDict, total=False):
    statement_type: Required[Annotated[Literal["income", "balance", "cashflow"], PropertyInfo(alias="statementType")]]
    """Type of financial statement ('income', 'balance', 'cashflow')."""

    period: Literal["annual", "quarterly"]
    """Period type ('annual', 'quarterly')."""
