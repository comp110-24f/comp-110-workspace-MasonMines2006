"""Docstring for this assignment"""

__author__ = "730765505"


def all(list_1: list[int], num: int) -> bool:
    i: int = 0
    condition = True
    if list_1 == []:
        condition = False
    while i < len(list_1):
        if list_1[i] != num:
            condition = False
        i += 1
    return condition


def max(list_1: list[int]) -> int:
    max_val: int = -999999
    i: int = 0
    while i < len(list_1):
        if list_1[i] > max_val:
            max_val = list_1[i]
        i += 1
    return max_val


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    condition: bool = True
    i: int = 0
    if len(list_1) != len(list_2):
        condition = False
    else:
        while i < len(list_1):
            if list_1[i] != list_2[i]:
                condition = False
            i += 1
    return condition


def extend(list_1: list[int], list_2: list[int]) -> None:
    i: int = 0
    while i < len(list_2):
        list_1.append(list_2[i])
        i += 1
    print(list_1)


if __name__ == "__main__":
    print(all([], 1))
