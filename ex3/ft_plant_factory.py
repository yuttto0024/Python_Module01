class Plant:
    """
    A class to simulate a plant and manage its initial characteristics.
    """
    def __init__(self, name: str, init_h: int, init_age: int):
        """
        Initializes a new Plant instance with its starting values.

        Args:
            name (str): The name of the plant (e.g., "Rose").
            init_h (int): The initial height of the plant in centimeters.
            init_age (int): The initial age of the plant in days.
        """
        self.name = name
        self.init_h = init_h
        self.init_age = init_age

    def get_info(self):
        """
        Prints the plant's creation status and initial characteristics.
        """
        print(f"Created: {self.name} ({self.init_h}cm, {self.init_age} days)")


if __name__ == "__main__":
    plant1 = ("Rose", 25, 30)
    plant2 = ("Oak", 200, 365)
    plant3 = ("Rose", 5, 90)
    plant4 = ("Rose", 80, 45)
    plant5 = ("Rose", 15, 120)
    all_plant = [plant1, plant2, plant3, plant4, plant5]
    i = 0
    print("=== Plant Factory Output ===")
    for data in all_plant:
        my_plant = Plant(*data)
        my_plant.get_info()
        i += 1
    print(f"Total plants created: {i}")
