#!/usr/bin/env python3
"""
Exercise 02 - Plant Growth Simulation

This program simulates plant growth over a week.
"""


class Plant:
    """
    Represents a plant that can grow and age over time.
    """

    def __init__(self, name: str, height_cm: int,
                 age_days: int) -> None:
        """
        Initialize a plant with name, height (cm),
        and age (days).
        """
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def grow(self) -> None:
        """
        Increase the plant height by 1 cm.
        """
        self.height_cm += 1

    def age(self) -> None:
        """
        Increase the plant age by 1 day.
        """
        self.age_days += 1

    def get_info(self) -> str:
        """
        Return formatted plant information.
        """
        return (f"{self.name}: {self.height_cm}cm, "
                f"{self.age_days} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)

    print("=== Day 1 ===")
    print(rose.get_info())
    print(sunflower.get_info())

    initial_rose_height = rose.height_cm

    for _ in range(6):
        rose.grow()
        rose.age()
        sunflower.grow()
        sunflower.age()

    print("=== Day 7 ===")
    print(rose.get_info())
    print(sunflower.get_info())

    growth = rose.height_cm - initial_rose_height
    print(f"Growth this week: +{growth}cm")
