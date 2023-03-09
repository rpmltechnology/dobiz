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


def mostpopular_page(request, page):
    page_dict = {
        'types_of_business': 'Types of Business',
        'sole_p_r': 'Sole Proprietorship Registration',
        'partnership_f_r': 'Partnership firm Registration',
        'one_p_c_r': 'One person Company Registration',
        'startup_i_r_dpiit': 'Startup India registration DPIIT',
        'company_r': 'Company Registration',
        'iip_r_i': 'IIP Registration in India'
    }

    if page not in page_dict:
        raise Http404('Invalid page')
    products = Product.objects.filter(category=page_dict.get(page))
    if page == 'sole_p_r':
        meaning = Meaning.objects.filter(category='Sole Proprietorship Registration').first()
        minimum = MinimumRequirement.objects.filter(category='Sole Proprietorship Registration').first()
        benefit = Benefits.objects.filter(category='Sole Proprietorship Registration').first()
        document = DocumentRequired.objects.filter(category='Sole Proprietorship Registration').first()
        incorporation = IncorporationProcess.objects.filter(category='Sole Proprietorship Registration').first()
        compliance = Compliance.objects.filter(category='Sole Proprietorship Registration').first()
        step = StepWiseProcedure.objects.filter(category='Sole Proprietorship Registration').first()

    # add these lines to fetch data for partnership_f_r page
    if page == 'partnership_f_r':
        meaning = Meaning.objects.filter(category='Partnership firm Registration').first()
        print('Meaning count:', Meaning.objects.count())
        minimum = MinimumRequirement.objects.filter(category='Partnership firm Registration').first()
        benefit = Benefits.objects.filter(category='Partnership firm Registration').first()
        document = DocumentRequired.objects.filter(category='Partnership firm Registration').first()
        incorporation = IncorporationProcess.objects.filter(category='Partnership firm Registration').first()
        compliance = Compliance.objects.filter(category='Partnership firm Registration').first()
        step = StepWiseProcedure.objects.filter(category='Partnership firm Registration').first()

    form = ContactUser()
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            return JsonResponse(serializer.data, status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)

    context = {'products': products, 'form': form, 'price':price,'banner': banner, 'meaning':meaning,'minimum':minimum,
            'benefit':benefit, 'document':document,'incorporation':incorporation,'compliance':compliance,
            'step':step}
    return render(request, f'mostpopular/{page}.html', context)

    path('mostpopular/<str:page>/', views.mostpopular_page, name='mostpopular'),

    @api_view(['GET','POST'])
def mostpopular_api(request,page):
    page_dict = {
        'types_of_business': 'Types of Business',
        'sole_p_r': 'Sole Proprietorship Registration',
        'partnership_f_r': 'Partnership firm Registration',
        'one_p_c_r': 'One person Company Registration',
        'startup_i_r_dpiit': 'Startup India registration DPIIT',
        'company_r': 'Company Registration',
        'iip_r_i': 'IIP Registration in India'
    }
    if page not in page_dict:
        return Response({"Error","Invalid Page"},status=404)
    #fetch the data
    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.get(category=page_dict.get(page))
    minimum = MinimumRequirement.objects.get(category=page_dict.get(page))
    benefit = Benefits.objects.get(category=page_dict.get(page))
    document = DocumentRequired.objects.get(category=page_dict.get(page))
    incorporation = IncorporationProcess.objects.get(category=page_dict.get(page))
    compliance = Compliance.objects.get(category=page_dict.get(page))
    step = StepWiseProcedure.objects.get(category=page_dict.get(page))

    # Serialize data
    product_serializer = ProductSerializer(products,many=True)
    meaning_serializer = MeaningSerializer(meaning)
    minimum_serializer = MinimumRequirementSerializer(minimum)
    beneift_serializer = BenefitsSerializer(benefit)
    document_serializer = DocumentRequiredSerializer(document)
    incorporation_serializer = IncorporationProcessSerializer(incorporation)
    compliance_serializer = ComplianceSerializer(compliance)
    step_serializer = StepWiseProcedureSerializer(step)

    #create reponse data
    response_data = {
        'products':product_serializer.data,
        'meaning': meaning_serializer.data,
        'minimum':minimum_serializer.data,
        'benefit':beneift_serializer.data,
        'document':document_serializer.data,
        'incorporation':incorporation_serializer.data,
        'compliance':compliance_serializer.data,
        'step':step_serializer.data
    }

    # Handle POST request
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            response_data['form'] = serializer.data
            return JsonResponse(response_data, status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)

    # Handle GET request
    response_data['banner'] = BannerSerializer(Banner.objects.get(category='CommonBanner')).data
    return JsonResponse(response_data, status=200)
    
     path('mostpopular_api/<str:page>/', views.mostpopular_api, name='mostpopular_api'),


     def types_of_business(request):
    products = Product.objects.filter(category='Types of Business')
    meaning = Meaning.objects.filter(category='Types of Business')
    minimum = MinimumRequirement.objects.filter(category='Types of Business')
    benefit = Benefits.objects.filter(category='Types of Business')
    document = DocumentRequired.objects.filter(category='Types of Business')
    incorporation = IncorporationProcess.objects.filter(category='Types of Business')
    compliance = Compliance.objects.filter(category='Types of Business')
    step = StepWiseProcedure.objects.filter(category='Types of Businessn')
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')

    form = ContactUser()
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            return JsonResponse(serializer.data, status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    context = {'products': products, 'form': form, 'price':price,'banner': banner, 'meaning':meaning,'minimum':minimum,
            'benefit':benefit, 'document':document,'incorporation':incorporation,'compliance':compliance,
            'step':step}
    return render(request, 'mostpopular/types_of_business.html',context)

def sole_p_r(request):
    products = Product.objects.filter(category='Sole Proprietorship Registration')
    meaning = Meaning.objects.filter(category='Sole Proprietorship Registration').first()
    minimum = MinimumRequirement.objects.filter(category='Sole Proprietorship Registration').first()
    benefit = Benefits.objects.filter(category='Sole Proprietorship Registration').first()
    document = DocumentRequired.objects.filter(category='Sole Proprietorship Registration').first()
    incorporation = IncorporationProcess.objects.filter(category='Sole Proprietorship Registration').first()
    compliance = Compliance.objects.filter(category='Sole Proprietorship Registration').first()
    step = StepWiseProcedure.objects.filter(category='Sole Proprietorship Registration').first()
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    form = ContactUser()
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            return JsonResponse(serializer.data, status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    context = {'products': products, 'form': form, 'price':price,'banner': banner, 'meaning':meaning,'minimum':minimum,
            'benefit':benefit, 'document':document,'incorporation':incorporation,'compliance':compliance,
            'step':step}
    return render(request, 'mostpopular/sole_p_r.html',context)

def partnership_f_r(request):
    products = Product.objects.filter(category='Partnership firm Registration')
    meaning = Meaning.objects.filter(category='Partnership Firm Registration').first()
    print(meaning)
    minimum = MinimumRequirement.objects.filter(category='Partnership firm Registration').first()
    benefit = Benefits.objects.filter(category='Partnership firm Registration').first()
    document = DocumentRequired.objects.filter(category='Partnership firm Registration').first()
    incorporation = IncorporationProcess.objects.filter(category='Partnership firm Registration').first()
    compliance = Compliance.objects.filter(category='Partnership firm Registration').first()
    step = StepWiseProcedure.objects.filter(category='Partnership firm Registration').first()
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    form = ContactUser()
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            return JsonResponse(serializer.data, status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    context = {'products': products, 'form': form, 'price':price,'banner': banner, 'meaning':meaning,'minimum':minimum,
            'benefit':benefit, 'document':document,'incorporation':incorporation,'compliance':compliance,
            'step':step}
    return render(request, 'mostpopular/partnership_f_r.html',context)

def one_p_c_r(request):
    products = Product.objects.filter(category='One person Company Registration')
    form = ContactUser()
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            return JsonResponse(serializer.data, status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    context = {'products':products,'form': form}
    return render(request, 'mostpopular/one_p_c_r.html',context)

def startup_i_r_dpiit(request):
    products = Product.objects.filter(category='Startup India registration DPIIT')
    form = ContactUser()
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            return JsonResponse(serializer.data, status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    context = {'products':products,'form': form}
    return render(request, 'mostpopular/startup_i_r_dpiit.html',context)

def company_r(request):
    products = Product.objects.filter(category='Company Registration')
    form = ContactUser()
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            return JsonResponse(serializer.data, status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    context = {'products':products,'form': form}
    return render(request, 'mostpopular/company_r.html',context)

def iip_r_i(request):
    products = Product.objects.filter(category='IIP Registration in India')
    form = ContactUser()
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            return JsonResponse(serializer.data, status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    context = {'products':products,'form': form}
    return render(request, 'mostpopular/iip_r_i.html',context)
path('types_of_business', views.types_of_business, name='types_of_business'),

path('sole_p_r', views.sole_p_r, name='sole_p_r'),

path('partnership_f_r', views.partnership_f_r, name='partnership_f_r'),

path('one_p_c_r', views.one_p_c_r, name='one_p_c_r'),

path('startup_i_r_dpiit', views.startup_i_r_dpiit, name='startup_i_r_dpiit'),

path('company_r', views.company_r, name='company_r'),

path('iip_r_i', views.iip_r_i, name='iip_r_i'),