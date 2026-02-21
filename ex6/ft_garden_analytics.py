class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self, growth_amount: int):
        self.height += growth_amount

    def get_info(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(
        self, name: str, height: int,
        color: str, prize_points: int
    ) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, Prize points: "


class GardenManager:
    total_gardens = 0

    def __init__(self, owner_name: str):
        self.owner_name = owner_name
        GardenManager.total_gardens += 1
        self.plants = []

    def add_plant(self, plant: Plant):
        self.plants.append(plant)
        print(f"added {plant.name} to {self.owner_name}'s garden")

    def all_grow(self, growth_amount: int):
        for plant in self.plants:
            plant.grow(growth_amount)
            print(f"{plant.name} grew {growth_amount}cm")

    def get_data(self):
        for plant in self.plants:
            print(plant.get_info())


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    alice_garden = GardenManager("Alice")
    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    print("-------------------------------------")
    alice_garden.all_grow(3)
    print("-------------------------------------")
    print("=== Alice's Garden Report ===")
    print("Plants in garden:")
    alice_garden.get_data()
    print("-------------------------------------")
    print(f"Total gardens managed: {GardenManager.total_gardens}")
