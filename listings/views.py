from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import *


def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)

    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(description__icontains=keywords)

    #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            listings = listings.filter(city__iexact=city)

    #State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            listings = listings.filter(state__iexact=state)

    #Bedrooms
    if 'bedrooms' in request.GET:
        bedroom = request.GET['bedrooms']
        if bedroom:
            listings = listings.filter(bedrooms__lte=bedroom)

    #Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listings = listings.filter(price__lte=price)

    context = {
        'state_choices': states,
        'bedroom_choices': bedrooms,
        'price_choices': prices,
        'listings': listings,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
