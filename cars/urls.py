from django.urls import path

from .views import CarCreateView, CarUpdateView, CarListView

urlpatterns = [
    path("", CarListView.as_view(), name="car_list"),
    path("add/", CarCreateView.as_view(), name="car_add"),
    path("<int:pk>/", CarUpdateView.as_view(), name="car_change"),
]
