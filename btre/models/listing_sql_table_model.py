"""
Listing SQL table model
"""
from uuid import uuid4
from django.db import models
from cloudinary.models import CloudinaryField
from ..settings import CLOUDINARY_FOLDER
class Listing(models.Model):
    """
    Listing SQL table model
    """
    class Meta:
        """
        Listing SQL table model meta class
        """
        verbose_name = 'Listing'
        verbose_name_plural = f'{verbose_name}s'
        db_table = verbose_name_plural.lower()
    id = models.UUIDField(
        primary_key = True,
        default = uuid4,
        editable = False
    )
    title = models.CharField()
    address = models.CharField()
    city = models.CharField()
    state = models.CharField()
    zipcode = models.CharField(
        max_length = 5
    )
    description = models.TextField(
        blank = True
    )
    price = models.DecimalField(
        max_digits = 12,
        decimal_places = 2
    )
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(
        max_digits = 2,
        decimal_places = 1
    )
    garage = models.IntegerField(
        default = 0
    )
    sqft = models.DecimalField(
        max_digits = 6,
        decimal_places = 1
    )
    lot_size = models.DecimalField(
        max_digits = 5,
        decimal_places = 1
    )
    exterior_photo = CloudinaryField(
        'Exterior',
        folder = CLOUDINARY_FOLDER
    )
    interior_photo_1 = CloudinaryField(
        'Interior Photo 1',
        folder = CLOUDINARY_FOLDER,
        blank = True
    )
    interior_photo_2 = CloudinaryField(
        'Interior Photo 2',
        folder = CLOUDINARY_FOLDER,
        blank = True
    )
    interior_photo_3 = CloudinaryField(
        'Interior Photo 3',
        folder = CLOUDINARY_FOLDER,
        blank = True
    )
    interior_photo_4 = CloudinaryField(
        'Interior Photo 4',
        folder = CLOUDINARY_FOLDER,
        blank = True
    )
    interior_photo_5 = CloudinaryField(
        'Interior Photo 5',
        folder = CLOUDINARY_FOLDER,
        blank = True
    )
    interior_photo_6 = CloudinaryField(
        'Interior Photo 6',
        folder = CLOUDINARY_FOLDER,
        blank = True
    )
    is_published = models.BooleanField(
        default = True
    )
    realtor = models.ForeignKey(
        to = 'Realtor',
        on_delete = models.DO_NOTHING,
        verbose_name = 'Realtor'
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now = True
    )
