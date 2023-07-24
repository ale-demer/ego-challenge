from django.forms import ModelForm
from .models import Car


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["name", "category", "title", "description", "year", "price", "image"]


class CarUpdateForm(ModelForm):
    class Meta:
        model = Car
        fields = ["name", "category", "title", "description", "year", "price", "image"]
