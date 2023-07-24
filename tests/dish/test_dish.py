from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    lasagna = Dish("lasanha", 33.25)
    pizza = Dish("pizza", 22.50)

    mussarela = Ingredient("queijo mussarela")
    ovo = Ingredient("ovo")

    lasagna.add_ingredient_dependency(mussarela, 2)
    lasagna.add_ingredient_dependency(ovo, 1)

    # Test for equality (__eq__)
    assert lasagna == lasagna
    assert lasagna != pizza

    # Test for hash (__hash__)
    assert hash(lasagna) == hash(lasagna)
    assert hash(lasagna) != hash(pizza)

    # Test for repr (__repr__)
    assert repr(lasagna) == "Dish('lasanha', R$33.25)"

    # Test for name attribute
    assert lasagna.name == "lasanha"

    # Test for price attribute
    assert lasagna.price == 33.25

    # Test for recipe attribute
    assert lasagna.recipe.get(mussarela) == 2

    # Test for TypeError in price attribute
    with pytest.raises(TypeError, match=r"Dish price must be float."):
        Dish("lasanha", "33.25")

    # Test for ValueError in price attribute
    with pytest.raises(
        ValueError,
        match=r"Dish price must be greater then zero."
    ):
        Dish("lasanha", -33.25)

    # Test for get_restrictions method
    assert lasagna.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    # Test for get_ingredients method
    assert lasagna.get_ingredients() == {mussarela, ovo}
