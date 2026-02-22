class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        self.single_growth = 0

    def grow(self, growth_amount: int):
        self.height += growth_amount
        self.single_growth += growth_amount

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
        return f"{base_info}, Prize points: {self.prize_points}"


class GardenManager:
    total_gardens = 0
    gardens_list = []

    def __init__(self, owner_name: str):
        self.owner_name = owner_name
        GardenManager.total_gardens += 1
        self.plants_list = []
        GardenManager.gardens_list.append(self)

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    def add_plant(self, plant: Plant):
        self.plants_list.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def all_grow(self, growth_amount: int):
        for plant in self.plants_list:
            plant.grow(growth_amount)
            print(f"{plant.name} grew {growth_amount}cm")

    def get_data(self):
        for plant in self.plants_list:
            print(plant.get_info())
        plant_total_growth = (
            GardenManager.GardenStats.calculate_total_growth(
                self.plants_list
            )
        )
        plant_count = len(self.plants_list)
        print("")
        print(f"Plants added: {plant_count}, "
              f"Total growth: {plant_total_growth}cm")
        regular, flowering, prize = (
            GardenManager.GardenStats.count_plant_types(self.plants_list)
        )
        print(f"Plant types: {regular} regular, "
              f"{flowering} flowering, {prize} prize flowers")

    @classmethod
    def create_garden_network(cls):
        print("Garden scores - ", end="")
        gardens_score_list = []
        for garden in cls.gardens_list:
            score = 0
            for plant in garden.plants_list:
                score += plant.height
                if type(plant) is PrizeFlower:
                    score += plant.prize_points * 4
            gardens_score_list.append(f"{garden.owner_name}: {score}")
        print(", ".join(gardens_score_list))

    class GardenStats:
        @staticmethod
        def calculate_total_growth(plants_list) -> int:
            plant_total_growth = 0
            for plant in plants_list:
                plant_total_growth += plant.single_growth

            return plant_total_growth

        @staticmethod
        def count_plant_types(plants_list):
            count_dict = {
                    Plant: 0,
                    FloweringPlant: 0,
                    PrizeFlower: 0
            }
            for plant in plants_list:
                plant_type = type(plant)
                if plant_type in count_dict:
                    count_dict[plant_type] += 1
            return (
                count_dict[Plant],
                count_dict[FloweringPlant],
                count_dict[PrizeFlower]
            )


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()
    alice_garden = GardenManager("Alice")
    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    bob_garden = GardenManager("Bob")
    bob_garden.plants_list.append(Plant("Bob tree", 92))
    print()
    print("Alice is helping all plants grow...")
    alice_garden.all_grow(1)
    print()
    print("=== Alice's Garden Report ===")
    print("Plants in garden:")
    alice_garden.get_data()
    print()
    is_valid = GardenManager.validate_height(100)
    print(f"Height validation test: {is_valid}")
    GardenManager.create_garden_network()
    print(f"Total gardens managed: {GardenManager.total_gardens}")
