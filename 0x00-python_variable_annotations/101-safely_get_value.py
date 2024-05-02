#!/usr/bin/env python3
"""
Task 11. More involved type annotations

More involved type annotations
"""

from typing import Any, Union, Mapping, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """safely_get_value

    safely get value
    """
    if key in dct:
        return dct[key]
    else:
        return default
