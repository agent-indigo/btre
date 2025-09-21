"""
Inquire view
"""
# pylint: disable = no-member
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from ..settings import SEND_EMAILS
from ..models import Inquiry
def inquire(request):
    """
    Inquire view
    """
    if request.method == 'POST':
        # check for existing inquiry
        if request.user.is_authenticated:
            LISTING_ID = request.POST['listing_id']
            USER_ID = request.user_id
            has_contacted = Inquiry.objects.all().filter(
                listing_id = LISTING_ID,
                user_id = USER_ID
            )
            if has_contacted:
                messages.error(
                    request,
                    'You have an existing inquiry regarding this listing.\
                     Our realtor will reply soon!'
                )
                return redirect(f'/listings/{LISTING_ID}')
            else:
                LISTING_TITLE = request.POST['listing_title']
                Inquiry(
                    listing_title = LISTING_TITLE,
                    listing_id = LISTING_ID,
                    first_name = request.POST['first_name'],
                    last_name = request.POST['last_name'],
                    email_address = request.POST['email_address'],
                    phone_number = request.POST['phone_number'],
                    message = request.POST['message'],
                    user_id = USER_ID
                ).save()
                # send email
                if SEND_EMAILS:
                    send_mail(
                        'Property Listing Inquiry',
                        f'There has been an inquiry regarding {LISTING_TITLE}.',
                        '', [
                            request.POST['realtor_email']
                        ],
                        fail_silently = False
                    )
                    messages.success(
                        request,
                        'Your inquiry has been sent to our realtor. They will reply soon!'
                    )
    return redirect(f'/listings/{LISTING_ID}')
