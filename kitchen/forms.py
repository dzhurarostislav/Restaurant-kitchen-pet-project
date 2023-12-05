from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms

from kitchen.models import Cook


class CookCreationForm(UserCreationForm):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)

        self.fields['password2'].help_text = None
        self.fields['years_of_experience'].help_text = \
            "Number of years worked in the kitchen"

    class Meta:
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ("first_name", "last_name", "email", "years_of_experience")
