"""
Import admin configs and corresponding SQL table models and register them here.
"""
# Import admin site registration utility here.
from django.contrib.admin import site
# Import admin configs here.
from .inquiry_admin_config import InquiryAdminConfig
from .listing_admin_config import ListingAdminConfig
from .realtor_admin_config import RealtorAdminConfig
# Import SQL table models here.
from ..models import (
    Inquiry,
    Listing,
    Realtor
)
# Register admin configs and corresponding SQL table models here.
site.register(
    Inquiry,
    InquiryAdminConfig
)
site.register(
    Listing,
    ListingAdminConfig
)
site.register(
    Realtor,
    RealtorAdminConfig
)
