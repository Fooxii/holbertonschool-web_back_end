#!/usr/bin/env python3
"""Module 9-element_length.py documentation"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function documentation"""
    return [(i, len(i)) for i in lst]
