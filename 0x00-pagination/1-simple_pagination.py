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
            pass
