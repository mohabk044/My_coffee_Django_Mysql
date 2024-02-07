from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

# Create your views here.
# def index(request):
#     return HttpResponse("<h1> Home Page  </h1>")


# def about(request):
#     return HttpResponse("<h1> About Page </h1>")


def index(request):
    context = {"products": Product.objects.all()}
    return render(request, "Pages/index.html", context)


def about(request):
    return render(request, "Pages/about.html")


def coffee(request):
    return render(request, "Pages/coffee.html")
