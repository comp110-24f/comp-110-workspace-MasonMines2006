"""File to define Fish class."""

__author__ = "730765505"


class Fish:
    """Fish."""

    age: int

    def __init__(self) -> None:
        """Inititialization."""
        self.age = 0

    def one_day(self) -> None:
        """One day simulation."""
        self.age += 1
        return None
