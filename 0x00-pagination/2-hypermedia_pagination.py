#!/usr/bin/env python3

"""
Simple pagination
"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    The function should return a tuple of size
    two containing a start index and an end index
    corresponding to the range of indexes to return
    in a list for those particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


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
        Function get page that returns a list
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        s, e = index_range(page, page_size)
        data_to_list = self.dataset()

        if s >= len(data_to_list):
            return []
        else:
            return data_to_list[s:e]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        a get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        data_items = self.get_page(page, page_size)
        s, e = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)

        page = {
            'page_size': len(data_items),
            'page': page,
            'data': data_items,
            'next_page': page + 1 if e < len(self.__dataset) else None,
            'prev_page': page - 1 if s > 0 else None,
            'total_pages': total_pages,
        }

        return page
