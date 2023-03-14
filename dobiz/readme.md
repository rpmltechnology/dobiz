created custom model
changes made in model.py, admin.py, views.py

added new files and folder
forms.py
managers.py
templatestags folder

isntalled apps

installed model django-countries
using pip install django-countries


added in setting.py
added in installed_apps 'django_countries'
AUTH_USER_MODEL = 'dobiz.User'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL='contact'
LOGOUT_REDIRECT_URL='contact'




import requests
import json
from datetime import datetime
from django.conf import settings
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
import random

# SMS API credentials
smsbazaar_username = 'your_smsbazaar_username'
smsbazaar_password = 'your_smsbazaar_password'
smsbazaar_sender_id = 'your_smsbazaar_sender_id'

def send_otp_to_phone(phone_number, token):
    url = 'https://www.smsbazaar.in/app/smsapi/index.php'
    payload = {
        'uname': smsbazaar_username,
        'password': smsbazaar_password,
        'send': smsbazaar_sender_id,
        'dest': phone_number,
        'msg': f'Your otp is {token}'
    }
    r = requests.get(url, params=payload)
    response = r.text.strip()
    if response == '1000':
        return True
    else:
        return False

def send_otp_to_email(email, token):
    send_mail(
                'Email Verification', 
                f'Your otp is {token}',
                 settings.EMAIL_HOST_USER,
                  [user.email], 
                  fail_silently=False,
                  )

def signup(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(email=form.cleaned_data.get('email'))
            token = str(random.randint(100000, 999999))
            user.otp = token
            token1 = str(random.randint(100000, 999999))
            user.otp_for_mobile = token1
            user.save()
            request.session['user_email'] = user.email
            request.session['user_phone'] = user.phone
            
            # Send OTP to user's phone
            phone_number = form.cleaned_data.get('phone')
            if phone_number:
                send_otp_to_phone(phone_number, token1)

            
            # Send OTP to user's email
            send_otp_to_email(user.email, token)
            
            messages.success(request, " Verification OTP is being sent on your registered Email and Phone Number")
            return redirect('verify')
        
        #recaptcha stuff
        clientkey = request.POST['g-recaptcha-response']
        secretkey = '6Lfi5U8kAAAAACmKRizYxZh6x7MnB85zUPPZy_-P'
        captchadata={
            'secret':secretkey,
            'response':clientkey
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data= captchadata)
        response = json.loads(r.text)
        verify = response['success']
        print('Your success is:', verify)
    
    return render(request, 'register/signup.html', {'form': form})

def verify(request):
    if request.method == 'POST':
        email_otp = request.POST.get('otp')
        phone_otp = request.POST.get('phone_otp') #entered by user
        email = request.session.get('user_email')
        phone = request.session.get('user_phone')
        if not email_otp or not phone_otp:
            messages.error(request, "Please enter both OTPs")
            return redirect('verify')
        user = User.objects.get(email=email)
        user1 = User.objects.get(phone=phone)
        if user.otp == email_otp and user.phone == phone and user.otp_for_mobile == phone_otp:
            user.is_verified = True
            user.save()
            messages.success(request, "Your account has been verified. Please login to complete your profile.")
            return redirect('auth_login')

        else:
            messages.error(request, "Invalid OTP")
            return redirect('verify')
    return render(request, 'register/verify.html')


from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView