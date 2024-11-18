# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .congress_recent_report import CongressRecentReport

__all__ = ["RecentReportListResponse"]

RecentReportListResponse: TypeAlias = List[CongressRecentReport]
