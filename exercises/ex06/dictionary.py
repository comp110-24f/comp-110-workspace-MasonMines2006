"""Notation for EX06 Dictionary"""

__author__ = "730765505"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    dict_2: dict[str, str] = {}
    key: str = ""
    value: str = ""
    for elem in dict_1:
        key = elem
        value = dict_1[elem]
        if value in dict_2:
            raise KeyError("Dictionary must be a bijection")
        else:
            dict_2[value] = key
    return dict_2


def favorite_color(init_dict: dict[str, str]) -> str:
    final_dict: dict[str, int] = {}
    for color in init_dict.values():
        if color not in final_dict:
            final_dict[color] = 1
        else:
            final_dict[color] += 1

    max_val: int = 0
    max_elem: str = ""
    for color, count in final_dict.items():
        if count > max_val:
            max_val = count
            max_elem = color
    return max_elem


def count(list_1: list[str]) -> dict[str, int]:
    final_dict: dict[str, int] = {}
    for elem in list_1:
        if elem not in final_dict:
            final_dict[elem] = 1
        else:
            final_dict[elem] += 1
    return final_dict


def alphabetizer(list_1: list[str]) -> dict[str, list[str]]:
    final_dict: dict[str, list[str]] = {}
    for elem in list_1:
        first_letter: str = elem[0].lower()
        if first_letter not in final_dict:
            final_dict[first_letter] = []
            final_dict[first_letter].append(elem)
        else:
            final_dict[first_letter].append(elem)
    return final_dict


def update_attendance(attendance: dict[str, list[str]], day: str, name: str) -> None:
    if day not in attendance:
        attendance[day] = []
    if name not in attendance[day]:
        attendance[day].append(name)
