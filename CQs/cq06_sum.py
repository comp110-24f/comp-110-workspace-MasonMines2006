"""Summing the elements of a list using different loops"""

__author__ = "730765505"


def w_sums(vals: list[float]) -> float:
    i: int = 0
    sum: float = 0.0
    while i < len(vals):
        sum = sum + vals[i]
        i += 0
    return sum


def f_sums(vals: list[float]) -> float:
    sum: float = 0.0
    for elem in vals:
        sum = sum + elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for i in range(len(vals)):
        sum = sum + vals[i]
    return sum
