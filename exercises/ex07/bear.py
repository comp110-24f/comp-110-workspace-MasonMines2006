"""File to define Bear class."""

__author__ = "730765505"


class Bear:
    """Bear."""

    age: int
    hunger_score: int

    def __init__(self) -> None:
        """Initializataion method."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Simulates one day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Eating."""
        self.hunger_score += num_fish
