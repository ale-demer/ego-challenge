from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from .models import Car
from .forms import CarForm, CarUpdateForm


@method_decorator(login_required, name="dispatch")
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
            queryset = queryset.order_by("price")
        elif order_by == "mayor_precio":
            queryset = queryset.order_by("-price")
        elif order_by == "mas_viejo":
            queryset = queryset.order_by("-year")
        elif order_by == "mas_nuevo":
            queryset = queryset.order_by("year")

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
    success_url = reverse_lazy("car_list")


@method_decorator(login_required, name="dispatch")
class CarDeleteView(DeleteView):
    model = Car
    success_url = "/cars"
    template_name = "cars/car_confirm_delete.html"
