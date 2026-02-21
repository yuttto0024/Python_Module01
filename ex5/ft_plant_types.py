class Plant:
    """
    Superclass managing common plant attributes (name, height, age).
    """
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age


class Flower(Plant):
    """
    Subclass inheriting from Plant,
    with a color attribute and blooming behavior.
    """
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """
        Outputs the blooming state of the flower.
        """
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    Subclass inheriting from Plant,
    with a trunk diameter and shade-producing behavior.
    """
    def __init__(self, name: int, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        Calculates and outputs the shade area based on the trunk diameter.
        """
        shade_radius_m = self.trunk_diameter / 10
        shade_area = int(3.14 * (shade_radius_m ** 2))
        print(f"{self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    """
    Subclass inheriting from Plant,
    with harvest season and nutritional value attributes.
    """
    def __init__(
        self, name: str, height: int, age: int,
        harvest_season: str, nutritional_value: str
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutritional_values(self):
        """
        Outputs information about the nutrients abundant in the vegetable.
        """
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== garden Plant Types ===")
    flower_data_list = [
        ("Rose", 25, 30, "red"),
        ("Sunflower", 150, 60, "yellow")
    ]
    for data in flower_data_list:
        flower = Flower(*data)
        print(f"{flower.name} (Flower): "
              f"{flower.height}cm, {flower.age} days, {flower.color} color")
        flower.bloom()
    print("--------------------------")
    tree_data_list = [
        ("Oak", 500, 1825, 50),
        ("Pine", 800, 3650, 40)
    ]
    for data in tree_data_list:
        tree = Tree(*data)
        print(f"{tree.name} (Tree): "
              f"{tree.height}cm, {tree.age} days, {tree.trunk_diameter}")
        tree.produce_shade()
    print("--------------------------")
    vegetable_data_list = [
        ("Tomato", 80, 90, "summer", "vitamin C"),
        ("corn", 80, 90, "summer", "vitamin E")
    ]
    for data in vegetable_data_list:
        vege = Vegetable(*data)
        print(f"{vege.name} (Vegetable): {vege.height}cm, "
              f"{vege.age} days, {vege.harvest_season} harvest")
        vege.get_nutritional_values()
