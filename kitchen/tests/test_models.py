from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from kitchen.models import DishType, IngredientType, Ingredient, Cook, Dish


class ModelTests(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Main Course")
        self.ingredient_type = IngredientType.objects.create(name="Vegetable")
        self.cook = Cook.objects.create(
            username="test_cook",
            first_name="John",
            last_name="Doe",
            years_of_experience=5,
        )
        self.ingredient = Ingredient.objects.create(
            name="Carrot", quantity=2, type=self.ingredient_type
        )
        self.dish = Dish.objects.create(
            name="Carrot Dish",
            description="A delicious dish with carrots",
            price=10.99,
            dish_type=self.dish_type,
        )
        self.dish.ingredients.add(self.ingredient)
        self.dish.cooks.add(self.cook)

    def test_dish_type_creation(self):
        dish_type = DishType.objects.create(name="Dessert")
        self.assertEqual(str(dish_type), "Dessert")

    def test_ingredient_type_creation(self):
        ingredient_type = IngredientType.objects.create(name="Fruit")
        self.assertEqual(str(ingredient_type), "Fruit")

    def test_ingredient_creation(self):
        ingredient = Ingredient.objects.create(name="Tomato", type=self.ingredient_type)
        self.assertEqual(str(ingredient), "Tomato")

    def test_cook_creation(self):
        cook = Cook.objects.create(
            username="test_cook_2",
            first_name="Jane",
            last_name="Doe",
            years_of_experience=3,
        )
        self.assertEqual(str(cook), "test_cook_2 (Jane Doe)")

    def test_dish_creation(self):
        dish = Dish.objects.create(
            name="Tomato Dish",
            description="A tasty dish with tomatoes",
            price=15.99,
            dish_type=self.dish_type,
        )
        dish.ingredients.add(self.ingredient)
        dish.cooks.add(self.cook)
        self.assertEqual(str(dish), "Tomato Dish")

    def test_unique_name_constraint(self):
        with self.assertRaises(IntegrityError):
            DishType.objects.create(
                name="Main Course"
            )

    def test_unique_ingredient_name_constraint(self):
        with self.assertRaises(IntegrityError):
            Ingredient.objects.create(
                name="Carrot", type=self.ingredient_type
            )

    def test_blank_quantity(self):
        ingredient = Ingredient.objects.create(
            name="Potato", type=self.ingredient_type, quantity=None
        )
        self.assertIsNone(ingredient.quantity)
