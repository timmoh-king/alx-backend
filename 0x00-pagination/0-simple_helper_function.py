#!/usr/bin/env python3

"""
    index_range that takes two integer arguments page and page_size.
    The function should return a tuple of size two containing:
    start index and an end index corresponding to the range of indexes
     to return in a list for those particular pagination parameters.
"""


def index_range(page, page_size):
    """
        return a tuple of size 2 containing a start idx and an end idx
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
