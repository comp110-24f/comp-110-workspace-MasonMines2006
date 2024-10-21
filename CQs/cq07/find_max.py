__author__ = "730765505"


def find_and_remove_max(list_1: list[int]) -> int:
    max: int = -9999999
    if list_1 == []:
        max = -1
    else:
        for elim in list_1:
            if elim > max:
                max = elim
    i = 0
    while i < len(list_1):
        if list_1[i] == max:
            list_1.pop(i)
        else:
            i += 1
    return max
