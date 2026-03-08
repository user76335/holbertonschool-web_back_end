#!/usr/bin/env python3
"""
Simple helper function for pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of start and end indexes for the given page and page_size.
    Pages are 1-indexed.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
