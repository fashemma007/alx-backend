#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Tuple


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
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:10]
            # print(truncated_dataset)
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_page docs"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        try:
            start, end = index_range(page, page_size)
            # print(start, end)
            dataset = self.dataset()  # get the dataset list loaded
            return dataset[start:end]  # return a slice of the dataset
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_hyper docs"""
        dataset = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = math.ceil(total_data / page_size)
        prev_page = page - 1
        next_page = page + 1

        result_dict = {
            'page_size': page_size,
            'page': page,
            'data': dataset,  # return a slice of the dataset
            # USING tenary operator instead
            'next_page': None if page == total_pages else next_page,
            'prev_page': None if page == 1 else prev_page,
            'total_pages': total_pages

        }
        return result_dict

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """return a dictionary"""

        # load already pre-indexed dataset
        indexed_dataset = self.indexed_dataset()
        indexed_page = {}

        i = index
        # print(f"i is {i} after assignment")
        # loop until required no. of pages are stored in `indexed_page`
        while len(indexed_page) < page_size:
            # verify that index is in a valid range
            assert 0 <= index < len(self.dataset())
            if i in indexed_dataset:  # chk if given index exists
                # print(f"i is {i} in cheka")
                indexed_page[i] = indexed_dataset[i]
            # else:
                # print(f"i is {i} and not found ")
            i += 1

        page = list(indexed_page.values())  # all pages in a list
        page_indices = indexed_page.keys()  # all index in a list
        # print(max(page_indices))
        result_dict = {
            'index': index,
            'next_index': max(page_indices) + 1,
            'page_size': len(page),
            'data': page
        }
        return result_dict
