class Plant:
    """
    A blueprint representing a plant in the garden.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize the plant with its name, height, and age.
        """
        self.name = name
        self.height = height
        self.age = age

    def output(self) -> None:
        """
        Display the plant's current information.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


plant1 = ("Rose", 25, 30)
plant2 = ("Sunflower", 80, 45)
plant3 = ("Cactus", 15, 120)
garden_data = [plant1, plant2, plant3]
for data in garden_data:
    my_plant = Plant(*data)
    my_plant.output()
