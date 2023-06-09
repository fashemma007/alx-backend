#!/usr/bin/env python3
"""module docs for 0-simple_helper_function.py"""
from typing import Tuple, List
import csv
import math


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
                # print(dataset)
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """method docs"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        try:
            start, end = index_range(page, page_size)
            # print(start, end)
            dataset = self.dataset()  # get the dataset list loaded
            return dataset[start:end]  # return a slice of the dataset
        except IndexError:
            return []
