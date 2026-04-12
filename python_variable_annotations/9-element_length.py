#!/usr/bin/env python3
"""Module 9-element_length.py documentation"""
from typing import Iterable, Sequence, Tuple, List, TypeVar

T = TypeVar('T', bound=Sequence)

def element_length(lst: Iterable[T]) -> List[Tuple[T, int]]:
    """Function documentation"""
    return [(i, len(i)) for i in lst]
