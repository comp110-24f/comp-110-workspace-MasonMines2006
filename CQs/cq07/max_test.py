__author__ = "730765505"

from find_max import find_and_remove_max


def test_return_test() -> None:
    list_1: list[int] = [1, 4, 5]
    value = find_and_remove_max(list_1)
    assert value == 5
    print(value)


def mutate_test() -> None:
    list_1: list[int] = [1, 4, 5]
    find_and_remove_max(list_1)
    assert list_1 == [1, 4]
    print(list_1)


def empty_test() -> None:
    list_1: list[int] = []
    value = find_and_remove_max(list_1)
    assert value == -1
    print(value)


if __name__ == "__main__":
    empty_test()
