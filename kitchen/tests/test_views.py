from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from kitchen.models import Dish, Cook, Ingredient, IngredientType, DishType

User = get_user_model()


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="test_user", password="test_password"
        )
        self.cook = Cook.objects.create(
            username="test_cook", password="test_password", years_of_experience=3
        )
        self.ingredient_type = IngredientType.objects.create(name="Vegetable")
        self.ingredient = Ingredient.objects.create(
            name="Carrot", quantity=2, type=self.ingredient_type
        )
        self.dish_type = DishType.objects.create(name="cake")
        self.dish = Dish.objects.create(
            name="Carrot Dish",
            description="A delicious dish with carrots",
            price=10.99,
            dish_type=self.dish_type,
        )
        self.dish.ingredients.add(self.ingredient)
        self.dish.cooks.add(self.cook)

    def test_index_view_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("kitchen:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dishes")

    def test_index_view_unauthenticated(self):
        response = self.client.get(reverse("kitchen:home"))
        self.assertEqual(
            response.status_code, 302
        )

    def test_cook_list_view_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("kitchen:cooks-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Years of experience")

    def test_cook_detail_view_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("kitchen:cook-detail", args=[self.cook.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First name")

    def test_cook_create_view_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("kitchen:create-cook"))
        self.assertEqual(response.status_code, 302)

        form_data = {
            "username": "new_cook",
            "password1": "test_password",
            "password2": "test_password",
            "first_name": "New",
            "last_name": "Cook",
            "years_of_experience": 2,
        }

        response = self.client.post(reverse("kitchen:create-cook"), data=form_data)
        self.assertEqual(response.status_code, 302)

    def test_cook_update_view_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("kitchen:cook-update", args=[self.cook.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Update my info")

        form_data = {
            "first_name": "Updated",
            "last_name": "Cook",
            "email": "updated_cook@example.com",
            "years_of_experience": 4,
        }

        response = self.client.post(
            reverse("kitchen:cook-update", args=[self.cook.pk]), data=form_data
        )
        self.assertEqual(response.status_code, 302)

        self.cook.refresh_from_db()
        self.assertEqual(self.cook.first_name, "Updated")

    def test_dish_list_view_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("kitchen:dish-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "All available dishes")

    def test_dish_detail_view_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("kitchen:dish-detail", args=[self.dish.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Update dish")

    def test_dish_create_view_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("kitchen:dish-create"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add dish")

        form_data = {
            "name": "New Dish",
            "description": "A new dish",
            "price": 15.99,
            "dish_type": self.dish.dish_type.pk,
            "cooks": [self.cook.pk],
            "ingredients": [self.ingredient.pk],
        }

        response = self.client.post(
            reverse("kitchen:dish-create"), data=form_data
        )
        self.assertEqual(response.status_code, 302)

        new_dish = Dish.objects.get(name="New Dish")
        self.assertIsNotNone(new_dish)

    def test_dish_update_view_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("kitchen:dish-update", args=[self.dish.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Update dish")

        form_data = {
            "name": "Updated Dish",
            "description": "An updated dish",
            "price": 20.99,
            "dish_type": self.dish.dish_type.pk,
            "cooks": [self.cook.pk],
            "ingredients": [self.ingredient.pk],
        }

        response = self.client.post(
            reverse("kitchen:dish-update", args=[self.dish.pk]), data=form_data
        )
        self.assertEqual(response.status_code, 302)

        self.dish.refresh_from_db()
        self.assertEqual(self.dish.name, "Updated Dish")
