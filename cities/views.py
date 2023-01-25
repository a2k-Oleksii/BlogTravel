from django.shortcuts import render
from cities.models import City


def home(request, pk=None):
    if pk:
        city = City.objects.filter(id=pk).first()
        return render(request, 'cities/detail.html', {'city': city})
    cities = City.objects.all()
    context = {"cities_list": cities, }
    return render(request, 'cities/home.html', context)
