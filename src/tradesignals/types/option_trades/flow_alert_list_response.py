# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .flow_alert_entry import FlowAlertEntry

__all__ = ["FlowAlertListResponse"]

FlowAlertListResponse: TypeAlias = List[FlowAlertEntry]
