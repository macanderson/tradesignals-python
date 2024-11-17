# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .spike_entry import SpikeEntry

__all__ = ["SpikeListResponse"]

SpikeListResponse: TypeAlias = List[SpikeEntry]
