

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
import requests
from django.http import JsonResponse
from django.contrib import messages
from dobiz.models import *
from django.views.decorators.csrf import csrf_exempt
from dobiz.forms import *
from math import ceil
import json
import os
#register login and logout
from django.contrib.sites.shortcuts import get_current_site
import random
from django.core.mail import send_mail
from django.conf import settings
import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
#DJANGO DRF IMPORTS
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dobiz.serializers import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Sum
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from datetime import date, datetime,timedelta
import datetime
# Create your views here.
def NGO(request, page):
    allpage = Page.objects.all()
    page_dict = {
        'section-8-company-registration': 'Section 8 Company Registration',
        'society-registration': 'Society Registration',
        'trust-registration': 'Trust Registration',
        '80G&12a-registration': '80G&12A Registration',
        '80G&12a-registration': '80G&12A Registration',
        'ngo-csr-1-filing': 'NGO CSR - 1 Filing',
        'fcra-registration': 'FCRA Registration',
        'niti-aayog-registration': 'NITI Aayog Registration (Darpan)',
    }
    if page not in page_dict:
        raise Http404('Invalid page')
        
    # Filter products based on the category and is_packed field
    packed_products = Product.objects.filter(category=page_dict.get(page), is_package=True)
    non_packed_products = Product.objects.filter(category=page_dict.get(page), is_package=False)

    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()

    form = ContactUser()
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    # Get the URLs of the first product in the lists
    non_packed_product_url = None
    if non_packed_products.exists():
        non_packed_product_url = request.build_absolute_uri(reverse('viewproduct', kwargs={'id': non_packed_products[0].id}))
    #Getting diffn betn prices and estimated delivery date
    diffn = None
    diffn_percentage = None
    for p in non_packed_products:
        diffn = int(p.market_price) - p.Dobiz_India_Filings
        diffn_percentage = round((diffn / int(p.market_price)) * 100, 2)
        if p.estimated_delivery_days is not None:
            p.estimated_delivery_date = date.today() + timedelta(days=p.estimated_delivery_days)
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            return JsonResponse(serializer.data, status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)

    context = { 'non_packed_products': non_packed_products, 'packed_products': packed_products, 'form': form, 'price':price,'banner': banner, 'meaning':meaning,'minimum':minimum,
            'benefit':benefit, 'document':document,'incorporation':incorporation,'compliance':compliance,
            'step':step,'faq':faq,'closure':closure,'allpage':allpage,'non_packed_product_url':non_packed_product_url,'diffn':diffn,'diffn_percentage':diffn_percentage}
    return render(request, f'{page}.html', context)