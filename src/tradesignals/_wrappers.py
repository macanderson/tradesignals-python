# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Generic, TypeVar

from ._models import GenericModel

__all__ = ["DataWrapper", "ChainsWrapper"]

_T = TypeVar("_T")


class DataWrapper(GenericModel, Generic[_T]):
    data: _T

    @staticmethod
    def _unwrapper(obj: "DataWrapper[_T]") -> _T:
        return obj.data


class ChainsWrapper(GenericModel, Generic[_T]):
    chains: _T

    @staticmethod
    def _unwrapper(obj: "ChainsWrapper[_T]") -> _T:
        return obj.chains
