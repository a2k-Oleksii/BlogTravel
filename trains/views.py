from django.core.paginator import Paginator
from django.shortcuts import render
from trains.models import Train


def home(request):
    trains = Train.objects.all()
    paginator = Paginator(trains, 10)
    page = request.GET.get("page")
    trains = paginator.get_page(page)
    context = {"trains_list": trains, }
    return render(request, "trains/home.html", context)
