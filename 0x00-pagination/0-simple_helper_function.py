#!/usr/bin/env python3
"""module docs for 0-simple_helper_function.py"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    The index_range function takes a page number and a page size,
    and returns the start index and end index of that range.

    page: int: the page number required
    page_size: int: the number of items to be displayed per page
    return: A tuple with the start and end index of a page
    """
    end_index = page_size * page
    start_index = end_index - page_size
    return (start_index, end_index)
