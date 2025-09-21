"""
Search view
"""
# pylint: disable = no-member
from django.shortcuts import render
from django.urls import reverse
from ..options import (
    BEDS,
    PRICES,
    STATES
)
from ..models import Listing
def search(request):
    """
    Search view
    """
    listings = Listing.objects.order_by('-created_at')
    # keywords
    if 'keywords' in request.GET:
        KEYWORDS = request.GET['keywords']
        if KEYWORDS:
            listings = listings.filter(
                description__icontains = KEYWORDS
            )
    # city
    if 'city' in request.GET:
        CITY = request.GET['city']
        if CITY:
            listings = listings.filter(
                city__iexact = CITY
            )
    # state
    if 'state' in request.GET:
        STATE = request.GET['state']
        if STATE:
            listings = listings.filter(
                state__iexact = STATE
            )
    # bedrooms
    if 'bedrooms' in request.GET:
        BEDROOMS = request.GET['bedrooms']
        if BEDROOMS:
            listings = listings.filter(
                bedrooms__iexact = BEDROOMS
            )
    # price
    if 'price' in request.GET:
        PRICE = request.GET['price']
        if PRICE:
            listings = listings.filter(
                price__lte = PRICE
            )
    return render(
        request,
        'listings/search.html', {
            'breadcrumb': [{
                'label': 'Listings',
                'url': reverse('listings')
            }, {
                'label': 'Search',
                'url': None
            }],
            'beds': BEDS,
            'listings': listings,
            'prices': PRICES,
            'states': STATES,
            'values': request.GET
        }
    )
