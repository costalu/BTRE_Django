from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "pages/index.html")


def about(request):
    return render(request, "pages/about.html")

def listings(request):
    return HttpResponse("<h1>Listings Page</h1>")
