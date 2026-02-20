#!/usr/bin/env python3
"""
Exercise 01 - Garden Data

This program defines a Plant class and displays
information about multiple plants.
"""


class Plant:
    """
    Represents a plant with a name, height, and age.
    """

    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        """
        Initialize a plant with its name, height in centimeters,
        and age in days.
        """
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    print(f"{plant1.name}: {plant1.height_cm}cm, "
          f"{plant1.age_days} days old")
    print(f"{plant2.name}: {plant2.height_cm}cm, "
          f"{plant2.age_days} days old")
    print(f"{plant3.name}: {plant3.height_cm}cm, "
          f"{plant3.age_days} days old")
