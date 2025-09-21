"""
Registration view
"""
from django.shortcuts import (
    render,
    redirect
)
from django.contrib import (
    messages,
    auth
)
from django.contrib.auth.models import User
def register(request):
    """
    Registration view
    """
    if request.method == 'POST':
        # get form values
        USERNAME = request.POST['username']
        PASSWORD = request.POST['password']
        CONFIRM_PASSWORD = request.POST['confirm_password']
        # check if passwords match
        if PASSWORD == CONFIRM_PASSWORD:
            # check username
            if User.objects.filter(
                username = USERNAME
            ).exists():
                messages.error(
                    request,
                    'That username is taken.'
                )
                return redirect('register')
            else:
                # check email
                EMAIL = request.POST['email']
                if User.objects.filter(
                    email = EMAIL
                ).exists():
                    messages.error(
                        request,
                        'An account with that email address already exists.'
                    )
                    return redirect('register')
                else:
                    # create user and immediately log in
                    auth.login(
                        request,
                        User.objects.create_user(
                            username = USERNAME,
                            password = PASSWORD,
                            email = EMAIL,
                            first_name = request.POST['first_name'],
                            last_name = request.POST['last_name']
                        )
                    )
                    messages.success(
                        request,
                        'You are now logged in.'
                    )
                    return redirect('dashboard')
        else:
            messages.error(
                request,
                'Passwords do not match'
            )
            return redirect('register')
    else:
        return render(
            request,
            'accounts/register.html'
        )
