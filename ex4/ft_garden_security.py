class SecurePlant:
    """
    ~~
    """
    def __init__(self, name: str, height: int, age: int):
        """
        ~~
        """
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, new_height) -> None:
        """
        ~~
        """
        if new_height > 0:
            self.__height = new_height

            print(f"Height updated: {self.__height} [OK]")
        else:
            print("Invalid operation attempted: "
                  f"height {self.__height} [REJECTED]")
            print("Security: Impossible ages rejected")


    def set_age(self, new_age) -> None:
        """
        ~~
        """
        if new_age >= 0:
            self.__age = new_age
            print(f"Age updated: {self.__age} [OK]")
        else:
            print("Invalid operation attempted: "
                  f"age {self.__age} [REJECTED]")
            print("Security: Impossible ages rejected")

    def get_height(self) -> int:
        """
        ~~
        """
        return self.__height

    def get_age(self) -> int:
        """
        ~~
        """
        return self.__age

    def get_info


plant1 = ["Rose", 25, 30]
my_plant = SecurePlant(*plant1)
