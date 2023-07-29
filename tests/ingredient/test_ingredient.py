from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


def test_ingredient():
    mussarela = Ingredient("queijo mussarela")
    farinha = Ingredient("farinha")

    # Test for equality (__eq__)
    assert mussarela == mussarela
    assert mussarela != farinha

    # Test for hash (__hash__)
    assert hash(mussarela) == hash(mussarela)
    assert hash(mussarela) != hash(farinha)

    # Test for repr (__repr__)
    assert repr(mussarela) == "Ingredient('queijo mussarela')"

    # Test for name attribute
    assert mussarela.name == "queijo mussarela"

    # Test for restrictions attribute
    assert mussarela.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
