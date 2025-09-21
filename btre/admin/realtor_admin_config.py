"""
Realtor admin configuration
"""
from django.contrib import admin
from django.utils.html import format_html
from ..models import Realtor
class RealtorAdminConfig(admin.ModelAdmin):
    """
    Realtors app admin config
    """
    list_display = [
        'first_name',
        'last_name',
        'email',
        'phone',
        'is_mvp',
        'created_at',
        'updated_at'
    ]
    list_display_links = [
        'first_name',
        'last_name'
    ]
    search_fields = [
        'first_name',
        'last_name',
        'email_address',
        'phone_number',
        'created_at',
        'updated_at'
    ]
    list_per_page = 25
    def email(
        self,
        realtor: Realtor
    ):
        """
        Realtor's email address as a mailto link
        """
        return format_html(
            '<a href="mailto:{email}">{email}</a>',
            email = realtor.email_address
        )
    email.short_description = 'Email Address'
    def phone(
        self,
        realtor: Realtor
    ):
        """
        Realtor's phone number as a tel link
        """
        return format_html(
            '<a href="tel:{phone}">{phone}</a>',
            phone = realtor.phone_number
        )
    phone.short_description = 'Phone Number'
