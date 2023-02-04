from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
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


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')


class CityDeleteView(DeleteView):
    model = City
    template_name = "cities/delete.html"
    success_url = reverse_lazy('cities:home')

    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)
