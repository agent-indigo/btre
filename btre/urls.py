"""
URL configuration for btre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.admin import site
from django.urls import path
from django.conf.urls.static import static
from .settings import (
    DEBUG,
    STATIC_URL,
    STATIC_ROOT
)
from .views import (
    index,
    about,
    dashboard,
    login,
    logout,
    register,
    inquire,
    listings,
    listing,
    search
)
urlpatterns = [
    path(
        '',
        index,
        name = 'index'
    ),
    path(
        'about',
        about,
        name = 'about'
    ),
    path(
        'accounts/dashboard',
        dashboard,
        name = 'dashboard'
    ),
    path(
        'accounts/login',
        login,
        name = 'login'
    ),
    path(
        'accounts/logout',
        logout,
        name = 'logout'
    ),
    path(
        'accounts/register',
        register,
        name = 'register'
    ),
    path(
        'admin/',
        site.urls
    ),
    path(
        'inquiries/inquire',
        inquire,
        name = 'inquire'
    ),
    path(
        'listings',
        listings,
        name = 'listings'
    ),
    path(
        'listings/<uuid:listing_id>',
        listing,
        name = 'listing'
    ),
    path(
        'search',
        search,
        name = 'search'
    ),
]
# Serve static files only during development
if DEBUG is True:
    urlpatterns += static(
        STATIC_URL,
        document_root = STATIC_ROOT
    )
