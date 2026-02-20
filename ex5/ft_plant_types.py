#!/usr/bin/env python3
"""
Exercise 05 - Plant Types with Inheritance

This program demonstrates inheritance by creating
different specialized plant types.
"""


class Plant:
    """
    Base class representing a general plant.
    """

    def __init__(self, name: str,
                 height_cm: int,
                 age_days: int) -> None:
        """
        Initialize common plant attributes.
        """
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days


class Flower(Plant):
    """
    Represents a flower plant.
    """

    def __init__(self, name: str,
                 height_cm: int,
                 age_days: int,
                 color: str) -> None:
        """
        Initialize flower with color attribute.
        """
        super().__init__(name, height_cm, age_days)
        self.color = color

    def bloom(self) -> None:
        """
        Flower blooms.
        """
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    Represents a tree plant.
    """

    def __init__(self, name: str,
                 height_cm: int,
                 age_days: int,
                 trunk_diameter: int) -> None:
        """
        Initialize tree with trunk diameter.
        """
        super().__init__(name, height_cm, age_days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """
        Tree produces shade.
        """
        shade_area = self.trunk_diameter * 1.56
        print(f"{self.name} provides "
              f"{int(shade_area)} square meters of shade")


class Vegetable(Plant):
    """
    Represents a vegetable plant.
    """

    def __init__(self, name: str,
                 height_cm: int,
                 age_days: int,
                 harvest_season: str,
                 nutritional_value: str) -> None:
        """
        Initialize vegetable with harvest season
        and nutritional value.
        """
        super().__init__(name, height_cm, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 600, 2000, 40)

    tomato = Vegetable("Tomato", 80, 90,
                       "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 70,
                       "spring", "vitamin A")

    print(f"{rose.name} (Flower): "
          f"{rose.height_cm}cm, "
          f"{rose.age_days} days, "
          f"{rose.color} color")
    rose.bloom()

    print(f"{oak.name} (Tree): "
          f"{oak.height_cm}cm, "
          f"{oak.age_days} days, "
          f"{oak.trunk_diameter}cm diameter")
    oak.produce_shade()

    print(f"{tomato.name} (Vegetable): "
          f"{tomato.height_cm}cm, "
          f"{tomato.age_days} days, "
          f"{tomato.harvest_season} harvest")
    print(f"{tomato.name} is rich in "
          f"{tomato.nutritional_value}")

    print("Total plant types created: 6")
