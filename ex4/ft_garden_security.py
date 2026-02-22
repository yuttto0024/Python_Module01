class SecurePlant:
    """
    A class to keep plant data safe.

    Attributes:
        __name (str): The plant's name (private).
        __height (int): The plant's height in cm (private).
        __age (int): The plant's age in days (private).
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Sets up the plant with safe data.

        Args:
            name (str): Plant's name.
            height (int): Initial height in cm.
            age (int): Initial age in days.
        """
        self.__name = name
        self.__height = height
        self.__age = age

    def set_height(self, new_height: int) -> None:
        """
        Safely changes the plant's height.
        """
        if new_height > 0:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print("Invalid operation attempted: "
                  f"height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, new_age: int) -> None:
        """
        Safely changes the plant's age.
        """
        if new_age >= 0:
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print("Invalid operation attempted: "
                  f"age {new_age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_name(self) -> str:
        """
        Returns the plant's name.
        """
        return self.__name

    def get_height(self) -> int:
        """
        Returns the plant's height.
        """
        return self.__height

    def get_age(self) -> int:
        """
        Returns the plant's age.
        """
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant_dict = {
        "name": "Rose",
        "height": 10,
        "age": 15,
    }
    my_plant = SecurePlant(**plant_dict)
    print(f"Plant created: {my_plant.get_name()}")
    my_plant.set_height(25)
    my_plant.set_age(30)
    print("------------------------------")
    print(f"Plant height: {my_plant.get_height()}")
    print(f"Plant age: {my_plant.get_age()}")
    print("------------------------------")
    my_plant.set_height(-5)
    my_plant.set_age(-10)
    print("------------------------------")
    print(f"Current plant: {my_plant.get_name()} "
          f"({my_plant.get_height()}cm, {my_plant.get_age()} days)")
