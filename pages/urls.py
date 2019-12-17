from django.urls import path

from . import views

urlpatterns = [

    # /
    path("", views.index, name="index"),

    # /about
    path("about", views.about, name="about")
]

