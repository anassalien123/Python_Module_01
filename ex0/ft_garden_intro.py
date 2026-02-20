#!/usr/bin/env python3
"""
Exercise 00 - Garden Introduction

This program displays basic information about a plant.
"""


def main() -> None:
    """
    Store plant information and display it.
    """
    plant_name = "Rose"
    plant_height = 25
    plant_age = 30

    print("=== Welcome to My Garden ===")
    print(f"Name: {plant_name}")
    print(f"Height: {plant_height} cm")
    print(f"Age: {plant_age} years\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
