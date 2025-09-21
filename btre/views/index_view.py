"""
Index view
"""
from django.shortcuts import render
from ..options import (
    BEDS,
    PRICES,
    STATES
)
from ..models import Listing
# pylint: disable = no-member
def index(request):
    """
    Home page view
    """
    return render(
        request,
        'pages/index.html', {
            'beds': BEDS,
            'listings': Listing.objects.order_by('-created_at').filter(
                is_published = True
            )[:3],
            'prices': PRICES,
            'states': STATES
        }
    )
