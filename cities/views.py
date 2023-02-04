from django.shortcuts import render
from django.views.generic.detail import DetailView
from .forms import CityForm
from cities.models import City


def home(request, pk=None):
    if request.method == "POST":
        form = CityForm(request.POST or None)
        if form.is_valid():
            form.save()
    form = CityForm()
    cities = City.objects.all()
    context = {"cities_list": cities, "form": form}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = "city"
    template_name = "cities/detail.html"
