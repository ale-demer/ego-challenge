from django.urls import path

from .views import (
    CarCreateView,
    CarUpdateView,
    CarListView,
    CarDeleteView,
    CarSheetView,
    TechSheetCreateView,
    TechSlideCreateView,
)

urlpatterns = [
    path("", CarListView.as_view(), name="car_list"),
    path("add/", CarCreateView.as_view(), name="car_add"),
    path("<int:pk>/", CarUpdateView.as_view(), name="car_change"),
    path("delete/<int:pk>/", CarDeleteView.as_view(), name="car_delete"),
    path("sheet/<int:pk>/", CarSheetView.as_view(), name="car_sheet"),
    path("sheet/create/<int:car_id>/", TechSheetCreateView.as_view(), name="sheet_create"),
    path("slide/create/<int:car_id>/", TechSlideCreateView.as_view(), name="slide_create"),
]
