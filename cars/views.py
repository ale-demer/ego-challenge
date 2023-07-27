from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Car, TechSheet, TechSlide
from .forms import CarForm, CarUpdateForm


class CarListView(ListView):
    model = Car
    context_object_name = "cars"
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get("category")
        order_by = self.request.GET.get("order_by")

        if category:
            queryset = queryset.filter(category=category)

        if order_by == "menor_precio":
            queryset = queryset.order_by("price", "year")
        elif order_by == "mayor_precio":
            queryset = queryset.order_by("-price", "-year")
        elif order_by == "mas_viejo":
            queryset = queryset.order_by("-year", "price")
        elif order_by == "mas_nuevo":
            queryset = queryset.order_by("year", "-price")

        return queryset


@method_decorator(login_required, name="dispatch")
class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy("car_list")


@method_decorator(login_required, name="dispatch")
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarUpdateForm
    template_name = "cars/car_update_form.html"

    def get_success_url(self):
        return reverse("car_sheet", kwargs={"pk": self.object.pk})


@method_decorator(login_required, name="dispatch")
class CarDeleteView(DeleteView):
    model = Car
    success_url = "/cars"
    template_name = "cars/car_confirm_delete.html"


class CarSheetView(DetailView):
    model = Car
    template_name = "cars/car_sheet.html"
    context_object_name = "car"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["alternate_position"] = True
        return context


@method_decorator(login_required, name="dispatch")
class TechSheetCreateView(CreateView):
    model = TechSheet
    fields = ["car", "heading", "paragraph", "image"]
    template_name = "cars/car_sheet_form.html"

    def get_initial(self):
        initial = super().get_initial()
        car_id = self.kwargs.get("car_id")
        try:
            initial["car"] = Car.objects.get(id=car_id)
        except Car.DoesNotExist:
            pass
        return initial

    def get_success_url(self):
        return reverse("car_sheet", kwargs={"pk": self.kwargs.get("car_id")})


@method_decorator(login_required, name="dispatch")
class TechSlideCreateView(CreateView):
    model = TechSlide
    fields = ["car", "heading", "paragraph", "image"]
    template_name = "cars/car_slide_form.html"

    def get_initial(self):
        initial = super().get_initial()
        car_id = self.kwargs.get("car_id")
        try:
            initial["car"] = Car.objects.get(id=car_id)
        except Car.DoesNotExist:
            pass
        return initial

    def get_success_url(self):
        return reverse("car_sheet", kwargs={"pk": self.kwargs.get("car_id")})
