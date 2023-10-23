#!/usr/bin/env python3

"""
    index_range that takes two integer arguments page and page_size.
    The function should return a tuple of size two containing:
    start index and an end index corresponding to the range of indexes
     to return in a list for those particular pagination parameters.
"""
import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        return a tuple of size 2 containing a start idx and an end idx
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            Use assert to verify that both args are int > 0
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        start, end = index_range(page, page_size)

        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int, page_size: int) -> Dict[str, int]:
        """
             returns a dict containing the following key-value pairs:
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size" : len(self.get_page()),
            "page" : page,
            "data" : self.get_page(page, page_size),
            "next_page" : page + 1 if page + 1 < total_pages else None,
            "prev_page" : page - 1 if page > 1 else None,
            "total_pages" : total_pages
        }
