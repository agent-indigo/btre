"""
Dashboard view
"""
# pylint: disable = no-member
from django.shortcuts import render
from ..models import Inquiry
def dashboard(request):
    """
    Dashboard view
    """
    return render(
        request,
        'accounts/dashboard.html', {
            'breadcrumb': [{
                'label': 'Dashboard',
                'url': None
            }],
            'inquiries': Inquiry.objects.order_by('-created_at').filter(
                user_id = request.user.id
            )
        }
    )
