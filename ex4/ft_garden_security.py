#!/usr/bin/env python3
"""
ft_garden_security.py

This module implements a secure plant system that protects
plant data using encapsulation and validation.
"""


class SecurePlant:
    """
    A class representing a secure plant with protected attributes.

    Attributes:
        name (str): The name of the plant.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a SecurePlant instance.

        Args:
            name (str): The plant name.
            height (int): Initial plant height in cm.
            age (int): Initial plant age in days.
        """
        self.name: str = name
        self.__height: int = 0
        self.__age: int = 0

        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """
        Set the plant height after validation.

        Args:
            height (int): The new height in cm.
        """
        if height < 0:
            print(
                f"Invalid operation attempted: "
                f"height {height}cm [REJECTED]"
            )
            print("Security: Negative height rejected")
            return
        self.__height = height
        print(f"Height updated: {height}cm [OK]")

    def get_height(self) -> int:
        """
        Get the current plant height.

        Returns:
            int: The height in cm.
        """
        return self.__height

    def set_age(self, age: int) -> None:
        """
        Set the plant age after validation.

        Args:
            age (int): The new age in days.
        """
        if age < 0:
            print(
                f"Invalid operation attempted: "
                f"age {age} days [REJECTED]"
            )
            print("Security: Negative age rejected")
            return
        self.__age = age
        print(f"Age updated: {age} days [OK]")

    def get_age(self) -> int:
        """
        Get the current plant age.

        Returns:
            int: The age in days.
        """
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 25, 30)
    print(f"Plant created: {plant.name}")

    plant.set_height(-5)

    print(
        f"Current plant: {plant.name} "
        f"({plant.get_height()}cm, {plant.get_age()} days)"
    )
