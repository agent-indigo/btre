"""
Login view
"""
from django.shortcuts import (
    render,
    redirect
)
from django.contrib import (
    messages,
    auth
)
from django.urls import reverse
def login(request):
    """
    Log in view
    """
    if request.method == 'POST':
        USER = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if USER is not None:
            auth.login(
                request,
                USER
            )
            if USER.is_staff:
                return redirect(reverse('admin:index'))
            else:
                messages.success(
                    request,
                    'You are now logged in.'
                )
                return redirect('dashboard')
        else:
            messages.error(
                request,
                'Invalid credentials.'
            )
            return redirect('login')
    else:
        return render(
            request,
            'accounts/login.html'
        )
