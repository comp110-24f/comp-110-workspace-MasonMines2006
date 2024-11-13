from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produces a string representation of a linked list"""
        rest: str = "TODO"
        if self.next is None:
            rest = "None"
        else:
            rest = self.next.__str__()
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))


def last(head: Node) -> int:
    """return the last value of a non-empty list"""
    return_val = -1
    if head.next is None:
        return_val = head.value
    else:
        return_val = last(head.next)

    return return_val


print(last(one))
print(last(courses))
