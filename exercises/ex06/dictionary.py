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


def favorite_colors(init_dict: dict[str, str]) -> str:
    final_dict: dict[str, int] = {}
    for elem in init_dict:
        if elem not in final_dict:
            final_dict[elem] = 1
        else:
            final_dict[elem] += 1
    max_val = 0
    max_elem = ""
    for elem in final_dict:
        if final_dict[elem] > max_val:
            max_elem = init_dict[elem]
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
        first_letter = elem[0].lower()
        if first_letter not in final_dict:
            final_dict[first_letter] = []
            final_dict[first_letter].append(elem)
        else:
            final_dict[first_letter].append(elem)
    return final_dict


def update_attendace(attendance: dict[str, list[str]], day: str, name: str) -> None:
    if day not in attendance:
        attendance[day] = []
    attendance[day].append(name)


test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
test_list: list[str] = ["Marc", "yellow", "Ezri", "blue", "Kris", "blue"]
test_day: str = "Monday"
test_name: str = "Brian"
test_attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}

update_attendace(test_attendance_log, test_day, test_name)
print(test_attendance_log)

# python exercises/ex06/dictionary.py
