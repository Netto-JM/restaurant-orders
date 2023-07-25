import csv
from typing import Set
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes: Set[Dish] = set()
        self.ingredients: Set[Ingredient] = set()

        self._load_data_from_csv(source_path)

    def _load_data_from_csv(self, source_path: str) -> None:

        with open(source_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                dish_name = row["dish"]
                ingredient_name = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                dish = self._get_or_create_dish(dish_name, row["price"])

                ingredient = self._get_or_create_ingredient(ingredient_name)

                dish.recipe[ingredient] = recipe_amount

    def _get_or_create_dish(self, dish_name: str, dish_price: str) -> Dish:
        for dish in self.dishes:
            if dish.name == dish_name:
                return dish

        dish = Dish(dish_name, float(dish_price))
        self.dishes.add(dish)
        return dish

    def _get_or_create_ingredient(self, ingredient_name: str) -> Ingredient:
        for ingredient in self.ingredients:
            if ingredient.name == ingredient_name:
                return ingredient

        ingredient = Ingredient(ingredient_name)
        self.ingredients.add(ingredient)
        return ingredient
