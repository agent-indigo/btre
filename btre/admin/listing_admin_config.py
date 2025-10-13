"""
Listing admin configuration
"""
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from ..models import Listing
class ListingAdminConfig(admin.ModelAdmin):
    """
    Listings app admin config
    """
    list_display = [
        'title',
        'address',
        'city',
        'state',
        'zipcode',
        'bedrooms',
        'bathrooms',
        'garage',
        'sqft',
        'lot_size',
        'price',
        'is_published',
        'realtor__first_name',
        'realtor__last_name',
        'created_at',
        'updated_at'
    ]
    list_display_links = [
        'title'
    ]
    list_filter = [
        'city',
        'state',
        'zipcode',
        'bedrooms',
        'bathrooms',
        'garage',
        'sqft',
        'lot_size',
        'price',
        'realtor__first_name',
        'realtor__last_name',
        'is_published',
        'created_at'
    ]
    list_editable = [
        'is_published'
    ]
    search_fields = [
        'title',
        'address',
        'city',
        'state',
        'zipcode',
        'description',
        'price',
        'bedrooms',
        'bathrooms',
        'garage',
        'sqft',
        'lot_size',
        'realtor__first_name',
        'realtor__last_name',
        'created_at'
    ]
    list_per_page = 20
    def realtor__first_name(
        self,
        listing: Listing
    ):
        """
        Realtor's first name as a link to their admin page
        """
        return format_html(
            '<a href="{url}">{name}</a>',
            url = reverse(
                'admin:btre_realtor_change',
                args = [
                    listing.realtor.id
                ]
            ),
            name = listing.realtor.first_name
        )
    realtor__first_name.short_description = 'Realtor First Name'
    def realtor__last_name(
        self,
        listing: Listing
    ):
        """
        Realtor's last name as a link to their admin page
        """
        return format_html(
            '<a href="{url}">{name}</a>',
            url = reverse(
                'admin:btre_realtor_change',
                args = [
                    listing.realtor.id
                ]
            ),
            name = listing.realtor.last_name
        )
    realtor__last_name.short_description = 'Realtor Last Name'
