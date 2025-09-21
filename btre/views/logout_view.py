"""
Logout view
"""
from django.shortcuts import redirect
from django.contrib import (
    messages,
    auth
)
def logout(request):
    """
    Log out view
    """
    if request.method == 'POST':
        auth.logout(request)
        messages.success(
            request,
            'You are now logged out.'
        )
        return redirect('index')
