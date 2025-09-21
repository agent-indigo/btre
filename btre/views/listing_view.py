"""
Listing view
"""
from django.shortcuts import (
    get_object_or_404,
    render
)
from django.urls import reverse
from ..models import Listing
def listing(
    request,
    listing_id
):
    """
    Listing page view
    """
    LISTING = get_object_or_404(
        Listing,
        pk = listing_id
    )
    return render(
        request,
        'listings/listing.html', {
            'breadcrumb': [{
                'label': 'Listings',
                'url': reverse('listings')
            }, {
                'label': LISTING.title,
                'url': None
            }],
            'listing': LISTING
        }
    )
