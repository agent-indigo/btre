"""
Listings view
"""
# pylint: disable = no-member
from django.shortcuts import render
from django.core.paginator import Paginator
from ..models import Listing
def listings(request):
    """
    Listings page view
    """
    return render(
        request,
        'listings/listings.html', {
            'breadcrumb': [{
                'label': 'Listings',
                'url': None
            }],
            'listings': Paginator(
                Listing.objects.order_by('-created_at').filter(
                    is_published = True
                ),
                6
            ).get_page(request.GET.get('page'))
        }
    )
