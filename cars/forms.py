from django.forms import ModelForm
from .models import Car, TechSheet, TechSlide


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["name", "category", "title", "description", "year", "price", "image"]


class CarUpdateForm(ModelForm):
    class Meta:
        model = Car
        fields = ["name", "category", "title", "description", "year", "price", "image"]


class TechSheetForm(ModelForm):
    class Meta:
        model = TechSheet
        fields = ["heading", "paragraph", "image"]


class TechSlideForm(ModelForm):
    class Meta:
        model = TechSlide
        fields = ["heading", "paragraph", "image"]
