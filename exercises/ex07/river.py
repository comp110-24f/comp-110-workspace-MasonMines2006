"""File to define River class."""

from fish import Fish
from bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        new_fish: list[Fish] = []
        for elem in self.fish:
            if elem.age <= 3:
                new_fish.append(elem)
        self.fish = new_fish
        new_bears: list[Bear] = []
        for elem in self.bears:
            if elem.age <= 5:
                new_bears.append(elem)
        self.bears = new_bears
        return None

    def remove_fish(self, amount: int):
        for i in range(amount):
            if self.fish is not []:
                self.fish.pop(0)

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
        self.bears = new_bears

    def repopulate_fish(self):
        num_fish: int = len(self.fish) // 2
        for i in range(num_fish * 4):
            baby_fish: Fish = Fish()
            self.fish.append(baby_fish)

    def repopulate_bears(self):
        num_bears: int = len(self.bears) // 2
        for i in range(num_bears):
            baby_bear: Bear = Bear()
            self.bears.append(baby_bear)

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish Population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
