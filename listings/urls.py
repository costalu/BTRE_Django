from django.urls import path

from . import views

urlpatterns = [

    #/listings
    path("", views.index, name="listings"),
    
    #/listings/id
    path("<int:listing_id>", views.listing, name="listing"),

    #/listing/search
    path("search", views.search, name="search"),
]

