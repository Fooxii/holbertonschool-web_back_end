#!/usr/bin/env python3
"""Module 0-simple_helper_function documentation"""


def index_range(page: int, page_size: int) -> tuple:
    """Function documentation"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
