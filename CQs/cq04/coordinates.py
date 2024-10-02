"""Coordinates File for CQ04"""

__author__ = "730765505"


def get_coords(xs: str, ys: str) -> None:
    for i in range(len(xs)):
        for j in range(len(ys)):
            print(xs[i] + ys[j])
