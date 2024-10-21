"""Test code doc for ex05"""

__author__ = "730765505"

from utils import only_evens, sub, add_at_index
import pytest


def only_evens_1_test() -> None:
    list_1 = [1, 4, 5]
    list_2 = only_evens(list_1)
    assert list_2 == [4]
    print(list_2)


def only_evens_2_test() -> None:
    list = [1, 3, 5]
    f_list = only_evens(list)
    assert f_list == []
    print(f_list)


def only_evens_3_test() -> None:
    list = [4, 4, 4]
    f_list = only_evens(list)
    assert f_list == [4, 4, 4]
    print(f_list)


def sub_1_test() -> None:
    list = [10, 20, 30, 40]
    f_list = sub(list, 1, 3)
    print(f_list)
    assert f_list == [20, 30]


def sub_2_test() -> None:
    list = [10, 20, 30, 40]
    f_list = sub(list, -1, 6)
    assert f_list == [10, 20, 30, 40]
    print(f_list)


def sub_3_test() -> None:
    list = []
    f_list = sub(list, 1, 3)
    assert f_list == []
    print(f_list)


def add_at_index_1_test() -> None:
    list_1 = [1, 2, 3, 5]
    add_at_index(list_1, 4, 3)
    assert list_1 == [1, 2, 3, 4, 5]


def add_at_index_2_test() -> None:
    list_1 = [1]
    add_at_index(list_1, 1, 2)
    assert list_1 == [1, 2]


def add_at_index_3_test() -> None:
    """Test that add_at_index raises an IndexError for an invalid index."""
    list_1 = []
    with pytest.raises(IndexError):
        add_at_index(list_1, 4, 1)


add_at_index_3_test()
