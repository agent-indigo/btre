"""
About view
"""
# pylint: disable = no-member
from django.shortcuts import render
from ..models import Realtor
def about(request):
    """
    About page view
    """
    return render(
        request,
        'pages/about.html', {
            'breadcrumb': [{
                'label': 'About',
                'url': None
            }],
            'mvps': Realtor.objects.all().filter(
                is_mvp = True
            ),
            'realtors': Realtor.objects.order_by('-created_at')
        }
    )
