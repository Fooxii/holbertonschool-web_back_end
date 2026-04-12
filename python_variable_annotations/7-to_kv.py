#!/usr/bin/env python3
"""Module 7-to_kv.py documentation"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function documentation"""
    return (k, float(v ** 2))
