# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .etf_exposure_data import EtfExposureData

__all__ = ["ExposureRetrieveResponse"]

ExposureRetrieveResponse: TypeAlias = List[EtfExposureData]
