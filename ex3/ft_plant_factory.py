#!/usr/bin/env python3
"""
Exercise 03 - Plant Factory

This program creates multiple plants efficiently
and displays them in an organized format.
"""


class Plant:
    """
    Represents a plant with a name, height,
    and age.
    """

    def __init__(self, name: str,
                 height_cm: int,
                 age_days: int) -> None:
        """
        Initialize plant with starting values.
        """
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    plants = []

    for name, height, age in plant_data:
        plant = Plant(name, height, age)
        plants.append(plant)
        print(f"Created: {plant.name} "
              f"({plant.height_cm}cm, "
              f"{plant.age_days} days)")

    print(f"Total plants created: {len(plants)}")
