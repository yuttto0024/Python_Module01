class Plant:
    """
    A class to simulate the growth and aging of a plant.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes a new Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): The initial height of the plant in centimeters.
            age (int): The initial age of the plant in days.
        """
        self.name = name
        self.height = height
        self.days_old = age

    def grow(self) -> None:
        """
        Increases the plant's height by 1 centimeter.
        """
        self.height += 1

    def age(self) -> None:
        """
        Increases the plant's age by 1 day.
        """
        self.days_old += 1

    def output(self) -> None:
        """
        Prints the current status of the plant to standard output.
        """
        print(f"{self.name}: {self.height}cm {self.days_old} days old")


plant1 = ["Rose", 25, 30]
my_plant = Plant(*plant1)
print("=== Day 1 ===")
my_plant.output()
for _ in range(6):
    my_plant.age()
    my_plant.grow()
print("=== Day 7 ===")
my_plant.output()
print(f"Growing this week: +6cm")
