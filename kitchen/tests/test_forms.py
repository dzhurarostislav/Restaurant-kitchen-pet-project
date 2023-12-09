from django.test import TestCase
from kitchen.forms import CookCreationForm, DishOrderingForm


class FormTests(TestCase):
    def test_cook_creation_form_valid(self):
        form_data = {
            "username": "test_user",
            "password1": "test_password",
            "password2": "test_password",
            "first_name": "John",
            "last_name": "Doe",
            "years_of_experience": 3,
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cook_creation_form_password_mismatch(self):
        form_data = {
            "username": "test_user",
            "password1": "test_password",
            "password2": "mismatched_password",
            "first_name": "John",
            "last_name": "Doe",
            "years_of_experience": 3,
        }
        form = CookCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)

    def test_dish_ordering_form_valid(self):
        form_data = {
            "ordering": "price_asc",
        }
        form = DishOrderingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_ordering_form_invalid_choice(self):
        form_data = {
            "ordering": "invalid_choice",
        }
        form = DishOrderingForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("ordering", form.errors)
