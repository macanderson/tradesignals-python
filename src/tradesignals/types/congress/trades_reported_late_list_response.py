# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .congress_late_report import CongressLateReport

__all__ = ["TradesReportedLateListResponse"]

TradesReportedLateListResponse: TypeAlias = List[CongressLateReport]
