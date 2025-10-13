"""
Inquire view
"""
# pylint: disable = no-member
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from ..settings import SEND_EMAILS
from ..models import (
    Inquiry,
    Listing
)
def inquire(request):
    """
    Inquire view
    """
    if request.method == 'POST':
        # check for existing inquiry
        if request.user.is_authenticated:
            LISTING_ID = request.POST['listing_id']
            USER_ID = request.user.id
            if Inquiry.objects.all().filter(
                listing = LISTING_ID,
                user = USER_ID
            ):
                messages.error(
                    request,
                    'You have an existing inquiry regarding this listing. \
                    Our realtor will reply soon!'
                )
            Inquiry(
                listing = LISTING_ID,
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email_address = request.POST['email_address'],
                phone_number = request.POST['phone_number'],
                message = request.POST['message'],
                user = USER_ID
            ).save()
            # send email
            if SEND_EMAILS:
                LISTING = Listing.objects.get(
                    pk = LISTING_ID
                )
                send_mail(
                    'Property Listing Inquiry',
                    f'There has been an inquiry regarding {LISTING.title}.',
                    '', [
                        LISTING.realtor.email_address
                    ],
                    fail_silently = False
                )
                messages.success(
                    request,
                    'Your inquiry has been sent to our realtor. They will reply soon!'
                )
    return redirect(f'/listings/{LISTING_ID}')
