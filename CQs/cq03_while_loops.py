"""
Assignment for CQ 3 on While Loops for CS110
"""

__author__ = 730765505


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    i: int = 0
    while i < len(phrase):
        if phrase[i] == search_char:
            count += 1
        i += 1
    return count


print(num_instances(input("input a phrase: "), input("input a search character: ")))
