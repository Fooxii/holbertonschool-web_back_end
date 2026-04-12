#!/usr/bin/env python3
"""Module 8-make_multiplier.py documentation"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function documentation"""
    def multiply(value: float) -> float:
        """Function documentation"""
        return value * multiplier
    return multiply
