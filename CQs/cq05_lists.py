"""Mutating functions."""

__author__ = "730765505"


def maunal_append(x: list[int], y: int) -> None:
    new_array: list[int] = [0] * (len(x) + 1)
    for i in range(len(x)):
        new_array[i] = x[i]
    new_array[len(x)] = y
    print(new_array)


def double(x: list[int]) -> None:
    i: int = 0
    while i < len(x):
        x[i] = x[i] * 2
        i += 1
    print(x)


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
