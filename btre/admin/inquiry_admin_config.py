"""
Inquiry admin configuration
"""
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from ..models import Inquiry
class InquiryAdminConfig(admin.ModelAdmin):
    """
    Inquiries app admin config
    """
    list_display = [
        'message',
        'listing__title',
        'first',
        'last',
        'email',
        'phone',
        'created_at'
    ]
    list_display_links = [
        'message'
    ]
    search_fields = [
        'message',
        'listing__title',
        'first_name',
        'last_name',
        'email_address',
        'phone_number',
        'created_at'
    ]
    list_per_page = 20
    def listing__title(
        self,
        inquiry: Inquiry
    ):
        """
        Listing title as a link to its admin page
        """
        return format_html(
            '<a href="{url}">{title}</a>',
            url = reverse(
                'admin:btre_listing_change',
                args = [
                    inquiry.listing.id
                ]
            ),
            title = inquiry.listing.title
        )
    listing__title.short_description = 'Listing Title'
    def first(
        self,
        inquiry: Inquiry
    ):
        """
        User's first name as a link to their admin page
        """
        return format_html(
            '<a href="{url}">{name}</a>',
            url = reverse(
                'admin:auth_user_change',
                args = [
                    inquiry.user.id
                ]
            ),
            name = inquiry.first_name
        ) if inquiry.user is not None else inquiry.first_name
    first.short_description = 'First Name'
    def last(
        self,
        inquiry: Inquiry
    ):
        """
        User's last name as a link to their admin page
        """
        return format_html(
            '<a href="{url}">{name}</a>',
            url = reverse(
                'admin:auth_user_change',
                args = [
                    inquiry.user.id
                ]
            ),
            name = inquiry.last_name
        ) if inquiry.user is not None else inquiry.last_name
    last.short_description = 'Last Name'
    def email(
        self,
        inquiry: Inquiry
    ):
        """
        User's email address as a mailto link
        """
        return format_html(
            '<a href="mailto:{email}">{email}</a>',
            email = inquiry.email_address
        )
    email.short_description = 'Email Address'
    def phone(
        self,
        inquiry: Inquiry
    ):
        """
        User's email address as a tel link
        """
        return format_html(
            '<a href="tel:{phone}">{phone}</a>',
            phone = inquiry.phone_number
        )
    phone.short_description = 'Phone Number'
