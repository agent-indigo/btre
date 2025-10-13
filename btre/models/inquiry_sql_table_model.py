"""
Inquiry SQL table model
"""
from uuid import uuid4
from django.db import models
class Inquiry(models.Model):
    """
    Inquiry SQL table model
    """
    class Meta:
        """
        Inquiry SQL table model meta class
        """
        verbose_name = 'Inquiry'
        verbose_name_plural = 'Inquiries'
        db_table = verbose_name_plural.lower()
    id = models.UUIDField(
        primary_key = True,
        default = uuid4,
        editable = False
    )
    listing = models.ForeignKey(
        to = 'Listing',
        on_delete = models.CASCADE
    )
    first_name = models.CharField()
    last_name = models.CharField()
    email_address = models.EmailField()
    phone_number = models.CharField()
    message = models.TextField(
        blank = True
    )
    user = models.ForeignKey(
        to = 'auth.User',
        on_delete = models.CASCADE,
        blank = True
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now = True
    )
