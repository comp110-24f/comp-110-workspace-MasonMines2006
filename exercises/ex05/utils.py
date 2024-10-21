"""Main utils code doc for ex05"""

__author__ = "730765505"


def only_evens(list: list[int]) -> list[int]:
    f_list = []
    for elem in list:
        if elem % 2 == 0:
            f_list.append(elem)
    return f_list


def sub(list: list[int], start: int, end: int) -> list[int]:
    f_list = []
    for i in range(len(list)):
        if start <= i & i < end:
            f_list.append(list[i])
    return f_list


def add_at_index(list: list[int], index: int, elem: int) -> None:
    if index > len(list):
        raise IndexError("Index is out of bounds for the input list")
    temp_list = []
    for i in range(index, len(list)):
        temp_list.append(list[i])
        list.pop(len(list) - i)
    list.append(elem)
    for elem in temp_list:
        list.append(elem)
    print(list)
