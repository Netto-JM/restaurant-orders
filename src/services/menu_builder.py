from typing import Dict, List, Optional

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    def make_menu(self) -> List[Dict]:
        menu = []
        for dish in self.menu_data.dishes:
            menu.append(
                {
                    "dish_name": dish.name,
                    "ingredients": dish.get_ingredients(),
                    "price": dish.price,
                    "restrictions": dish.get_restrictions(),
                }
            )

        return menu

    def get_main_menu(self, restriction: Optional[str] = None) -> List[Dict]:
        if not restriction:
            return self.make_menu()
        return list(
            item
            for item in self.make_menu()
            if restriction not in item["restrictions"]
        )
