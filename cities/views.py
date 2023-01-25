from django.shortcuts import render
from cities.models import City


def home(request):
    cities = City.objects.all()
    context = {"cities_list": cities, }
    return render(request, 'cities/home.html', context)
