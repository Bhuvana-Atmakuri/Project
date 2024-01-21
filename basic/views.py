from django.shortcuts import render
import razorpay
from email.message import EmailMessage
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from razorpay.resources import payment

# from .tokens import Generate_Token
from django.shortcuts import render, redirect
from .models import *

from django.http import JsonResponse
import json
from django.contrib import messages


# Create your views here.
def log(request):
    # if request.method == "POST":
    #     username = request.POST.get("username")
    #     password = request.POST.get("password")
    #     email = request.POST.get("email")
    #     myuser = User.objects.create_user(username, email, password)
    #
    #
    #     if not username.isalnum():
    #         messages.error(request, "User name must be alpha numeric")
    #
    #     myuser.save()
    #     messages.success(request,
    #                      "Your account has been successfully created we have sent you a confirmation email!please confirm your email to activate your account")
    #
    #     subject = "Welcome to Aaharam"
    #     message = "Hello!" + myuser.username + "! \n\n" + "Welcome to Aaharam!\n\nThankyou for registering for our website \n\n we have also sent you a confirmation email ,please confirm your email address in order to activate your account\n\n" + "Thanking you\n\n Bhuvana"
    #     from_email = settings.EMAIL_HOST_USER
    #     to_list = [myuser.email]
    #     send_mail(subject, message, from_email, to_list, fail_silently=True)
    #
    #     current_site = get_current_site(request)
    #     email_subject = "Confirm your email for Aaharam website"
    #     message2 = render_to_string('email_confimation.html', {
    #         'name': myuser.username,
    #         'domain': current_site.domain,
    #         'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
    #         'token': Generate_Token.make_token(myuser)
    #
    #     })
    #     email = EmailMessage(email_subject, message2, settings.EMAIL_HOST_USER, [myuser.email], )
    #     email.fail_silently = True
    #     email.send()
    #
    #     return redirect("sign")
    return render(request, "register.html")