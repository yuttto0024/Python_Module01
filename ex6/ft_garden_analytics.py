class Plant:
    """
    Base class representing a generic plant.
    """
    def __init__(self, name: str, height: int) -> None:
        """
        Initialize a plant with a name and height.
        """
        self.name = name
        self.height = height
        self.single_growth = 0

    def grow(self, growth_amount: int) -> None:
        """
        Increase the plant's height and record the growth amount.
        """
        self.height += growth_amount
        self.single_growth += growth_amount

    def get_info(self) -> str:
        """
        Return a formatted string containing basic plant details.
        """
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """
    A plant that produces flowers, inheriting from Plant.
    """
    def __init__(self, name: str, height: int, color: str) -> None:
        """
        Initialize a flowering plant with a specific flower color.
        """
        super().__init__(name, height)
        self.color = color

    def get_info(self) -> str:
        """
        Return plant details including flower color and status.
        """
        base_info = super().get_info()
        return f"{base_info}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """
    A highly-rated flowering plant with prize points.
    """
    def __init__(
        self, name: str, height: int,
        color: str, prize_points: int
    ) -> None:
        """
        Initialize a prize flower with competition points.
        """
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self) -> str:
        """
        Return plant details including accumulated prize points.
        """
        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.prize_points}"


class GardenManager:
    """
    Manages individual gardens and tracks the global garden network.
    """
    total_gardens = 0
    gardens_list = []

    def __init__(self, owner_name: str) -> None:
        """
        Initialize a garden for an owner and register it globally."
        """
        self.owner_name = owner_name
        GardenManager.total_gardens += 1
        self.plants_list = []
        GardenManager.gardens_list.append(self)

    @staticmethod
    def validate_height(height: int) -> bool:
        """
        Utility function to check if a given height is valid.
        """
        return height >= 0

    def add_plant(self, plant: Plant) -> None:
        """
        Add a new plant object to the manager's garden.
        """
        self.plants_list.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def all_grow(self, growth_amount: int) -> None:
        """
        Apply a specific growth amount to all plants in the garden.
        """
        for plant in self.plants_list:
            plant.grow(growth_amount)
            print(f"{plant.name} grew {growth_amount}cm")

    def get_data(self) -> None:
        """
        Generate and print a comprehensive report for this garden.
        """
        for plant in self.plants_list:
            print(plant.get_info())
        plant_total_growth = (
            GardenManager.GardenStats.calculate_total_growth(
                self.plants_list
            )
        )
        plant_count = len(self.plants_list)
        print("-------------------------------------")
        print(f"Plants added: {plant_count}, "
              f"Total growth: {plant_total_growth}cm")
        regular, flowering, prize = (
            GardenManager.GardenStats.count_plant_types(self.plants_list)
        )
        print(f"Plant types: {regular} regular, "
              f"{flowering} flowering, {prize} prize flowers")

    @classmethod
    def create_garden_network(cls) -> None:
        """
        Calculate and print the scores for all registered gardens.
        """
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
        """
        Nested helper class providing analytics and calculations.
        """
        @staticmethod
        def calculate_total_growth(plants_list) -> int:
            """
            Calculate the total growth amount across a list of plants.
            """
            plant_total_growth = 0
            for plant in plants_list:
                plant_total_growth += plant.single_growth

            return plant_total_growth

        @staticmethod
        def count_plant_types(plants_list) -> tuple:
            """
            Count the occurrences of each plant type in a given list.
            """
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
    alice_garden = GardenManager("Alice")
    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    bob_garden = GardenManager("Bob")
    bob_garden.plants_list.append(Plant("Bob tree", 92))
    print("Alice is helping all plants grow...")
    print("-------------------------------------")
    alice_garden.all_grow(1)
    print("-------------------------------------")
    print("=== Alice's Garden Report ===")
    print("Plants in garden:")
    alice_garden.get_data()
    print("-------------------------------------")
    is_valid = GardenManager.validate_height(100)
    print(f"Height validation test: {is_valid}")
    GardenManager.create_garden_network()
    print(f"Total gardens managed: {GardenManager.total_gardens}")
