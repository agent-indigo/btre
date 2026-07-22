"""
Realtor SQL table model
"""
from uuid import uuid4
from django.db import models
from cloudinary.models import CloudinaryField
from ..settings import CLOUDINARY_FOLDER
class Realtor(models.Model):
    """
    Realtor SQL table model
    """
    class Meta:
        """
        Realtor SQL table model meta class
        """
        verbose_name = 'Realtor'
        verbose_name_plural = f'{verbose_name}s'
        db_table = verbose_name_plural.lower()
    id = models.UUIDField(
        primary_key = True,
        default = uuid4,
        editable = False
    )
    first_name = models.CharField()
    last_name = models.CharField()
    photo = CloudinaryField(
        'Photo',
        folder = CLOUDINARY_FOLDER
    )
    description = models.TextField()
    email_address = models.EmailField()
    phone_number = models.CharField()
    is_mvp = models.BooleanField(
        default = False
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now = True
    )
