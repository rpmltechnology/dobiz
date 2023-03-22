from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
import requests
from django.http import JsonResponse
from django.contrib import messages
from .models import *
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from math import ceil
import json
import os
from django.contrib import messages
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
from .serializers import *

#integration with razarpay
import razorpay

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
    else:
        form = ContactUser()
    return render(request, 'home.html', {'form': form})

#View Product
from django.contrib.auth.decorators import login_required
def viewproduct(request, **kwargs):
    user_id = kwargs.get('user_id')
    id = kwargs.get('id')
    products = get_object_or_404(Product, id=id)
    context = {'products': products, 'user_id': user_id}
    return render(request, 'viewproduct.html', context)


#order view

def order(request):
    return render(request, 'order.html')

#MOSTPOPULAR view

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
            'step':step,'faq':faq,'closure':closure}
    return render(request, f'mostpopular/{page}.html', context)

#MOSTPOPULAR API
@api_view(['GET', 'POST'])
def mostpopular_api(request, page):
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
        return Response({"Error", "Invalid Page"}, status=404)
    # fetch the data
    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.get(category=page_dict.get(page))
    minimum = MinimumRequirement.objects.get(category=page_dict.get(page))
    benefit = Benefits.objects.get(category=page_dict.get(page))
    document = DocumentRequired.objects.get(category=page_dict.get(page))
    incorporation = IncorporationProcess.objects.get(category=page_dict.get(page))
    compliance = Compliance.objects.get(category=page_dict.get(page))
    step = StepWiseProcedure.objects.get(category=page_dict.get(page))
    faq = FAQ.objects.get(category=page_dict.get(page))
    closure = Closure.objects.get(category=page_dict.get(page))

    # Serialize data
    product_serializer = ProductSerializer(products, many=True)
    meaning_serializer = MeaningSerializer(meaning)
    minimum_serializer = MinimumRequirementSerializer(minimum)
    beneift_serializer = BenefitsSerializer(benefit)
    document_serializer = DocumentRequiredSerializer(document)
    incorporation_serializer = IncorporationProcessSerializer(incorporation)
    compliance_serializer = ComplianceSerializer(compliance)
    step_serializer = StepWiseProcedureSerializer(step)
    faq_serializer = FAQSerializer(faq)
    closure_serializer = ClosureSerializer(closure)

    # create response data
    response_data = {
        'products': product_serializer.data,
        'meaning': meaning_serializer.data,
        'minimum': minimum_serializer.data,
        'benefit': beneift_serializer.data,
        'document': document_serializer.data,
        'incorporation': incorporation_serializer.data,
        'compliance': compliance_serializer.data,
        'step': step_serializer.data,
        'faq': faq_serializer.data,
        'closure': closure_serializer.data,
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
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    response_data['banner'] = BannerSerializer(banner).data
    response_data['price'] = PricingSumSerializer(price).data
    return JsonResponse(response_data, status=200)


    
  #SPECIAL BUSSINESS view  
def specialbussiness_page(request, page):
    page_dict = {
        'gst_r_i': 'GST Registration in India',
        'import_e_c_i': 'Import export Code',
        'microfinance_c_r': 'Microfinance Company Registration',
        'msme_r': 'MSME Registrationn',
        'nidhi_c_r': 'NIDHI Company Registration',
        'produce_c': 'Producer Company',
        'public_l_c_r': 'Public Limited Company registration'
    }

    if page not in page_dict:
        raise Http404('Invalid page')
    products = Product.objects.filter(category=page_dict.get(page))
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
            'step':step,'faq':faq,'closure':closure}
    return render(request, f'specialbussiness/{page}.html', context)

#SPECIAL BUSSINESS API 

@api_view(['GET', 'POST'])
def specialbussiness_api(request, page):
    page_dict = {
        'gst_r_i': 'GST Registration in India',
        'import_e_c_i': 'Import export Code',
        'microfinance_c_r': 'Microfinance Company Registration',
        'msme_r': 'MSME Registrationn',
        'nidhi_c_r': 'NIDHI Company Registration',
        'produce_c': 'Producer Company',
        'public_l_c_r': 'Public Limited Company registration'
    }
    if page not in page_dict:
        return Response({"Error", "Invalid Page"}, status=404)
    # fetch the data
    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.get(category=page_dict.get(page))
    minimum = MinimumRequirement.objects.get(category=page_dict.get(page))
    benefit = Benefits.objects.get(category=page_dict.get(page))
    document = DocumentRequired.objects.get(category=page_dict.get(page))
    incorporation = IncorporationProcess.objects.get(category=page_dict.get(page))
    compliance = Compliance.objects.get(category=page_dict.get(page))
    step = StepWiseProcedure.objects.get(category=page_dict.get(page))
    faq = FAQ.objects.get(category=page_dict.get(page))
    closure = Closure.objects.get(category=page_dict.get(page))

    # Serialize data
    product_serializer = ProductSerializer(products, many=True)
    meaning_serializer = MeaningSerializer(meaning)
    minimum_serializer = MinimumRequirementSerializer(minimum)
    beneift_serializer = BenefitsSerializer(benefit)
    document_serializer = DocumentRequiredSerializer(document)
    incorporation_serializer = IncorporationProcessSerializer(incorporation)
    compliance_serializer = ComplianceSerializer(compliance)
    step_serializer = StepWiseProcedureSerializer(step)
    faq_serializer = FAQSerializer(faq)
    closure_serializer = ClosureSerializer(closure)

    # create response data
    response_data = {
        'products': product_serializer.data,
        'meaning': meaning_serializer.data,
        'minimum': minimum_serializer.data,
        'benefit': beneift_serializer.data,
        'document': document_serializer.data,
        'incorporation': incorporation_serializer.data,
        'compliance': compliance_serializer.data,
        'step': step_serializer.data,
        'faq': faq_serializer.data,
        'closure': closure_serializer.data,
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
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    response_data['banner'] = BannerSerializer(banner).data
    response_data['price'] = PricingSumSerializer(price).data
    return JsonResponse(response_data, status=200)


#NGO view
def ngo_page(request, page):
    page_dict = {
        'trust_registration': 'Trust Registration',
        'society_registration': 'Society Registration',
        'section_8': 'Section 8 Company Registration',
        'roc': 'ROC Registrations with CSR-1',
        'patent': 'Patent registration',
        'startup': 'Startup Business',
    }

    if page not in page_dict:
        raise Http404('Invalid page')
    products = Product.objects.filter(category=page_dict.get(page))
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
            'step':step,'faq':faq,'closure':closure}
    return render(request, f'ngo/{page}.html', context)

#NGO API
@api_view(['GET', 'POST'])
def ngo_api(request, page):
    page_dict = {
        'trust_registration': 'Trust Registration',
        'society_registration': 'Society Registration',
        'section_8': 'Section 8 Company Registration',
        'roc': 'ROC Registrations with CSR-1',
        'patent': 'Patent registration',
        'startup': 'Startup Business',
    }
    if page not in page_dict:
        return Response({"Error", "Invalid Page"}, status=404)
    # fetch the data
    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.get(category=page_dict.get(page))
    minimum = MinimumRequirement.objects.get(category=page_dict.get(page))
    benefit = Benefits.objects.get(category=page_dict.get(page))
    document = DocumentRequired.objects.get(category=page_dict.get(page))
    incorporation = IncorporationProcess.objects.get(category=page_dict.get(page))
    compliance = Compliance.objects.get(category=page_dict.get(page))
    step = StepWiseProcedure.objects.get(category=page_dict.get(page))
    faq = FAQ.objects.get(category=page_dict.get(page))
    closure = Closure.objects.get(category=page_dict.get(page))

    # Serialize data
    product_serializer = ProductSerializer(products, many=True)
    meaning_serializer = MeaningSerializer(meaning)
    minimum_serializer = MinimumRequirementSerializer(minimum)
    beneift_serializer = BenefitsSerializer(benefit)
    document_serializer = DocumentRequiredSerializer(document)
    incorporation_serializer = IncorporationProcessSerializer(incorporation)
    compliance_serializer = ComplianceSerializer(compliance)
    step_serializer = StepWiseProcedureSerializer(step)
    faq_serializer = FAQSerializer(faq)
    closure_serializer = ClosureSerializer(closure)

    # create response data
    response_data = {
        'products': product_serializer.data,
        'meaning': meaning_serializer.data,
        'minimum': minimum_serializer.data,
        'benefit': beneift_serializer.data,
        'document': document_serializer.data,
        'incorporation': incorporation_serializer.data,
        'compliance': compliance_serializer.data,
        'step': step_serializer.data,
        'faq': faq_serializer.data,
        'closure': closure_serializer.data,
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
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    response_data['banner'] = BannerSerializer(banner).data
    response_data['price'] = PricingSumSerializer(price).data
    return JsonResponse(response_data, status=200)

#do bussines in india view
def do_bussiness(request, page):
    page_dict = {
        'company_f_i':'Company By Foreign Individuals',
        'doing_b_i': 'Doing Business In India',
        'sector_w_fdi_l': 'Sector Wise FDI Limits',
        'scvbo': 'Subsidiary Company Vs Branch Office'
    }
    if page not in page_dict:
        raise Http404('Invalid page')

    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()

    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')

    form = ContactUser()
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serialzer = ContactUserSerializer(form.instance)
            return JsonResponse(serialzer.data, satus=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)

    context = {'products': products, 'form': form, 'price':price,'banner': banner, 'meaning':meaning,'minimum':minimum,
            'benefit':benefit, 'document':document,'incorporation':incorporation,'compliance':compliance,
            'step':step,'faq':faq,'closure':closure}
    return render(request, f'do_bussiness/{page}.html', context)

@api_view(['GET','POST'])
def do_bussiness_api(request, page):
    page_dict = {
        'company_f_i':'Company By Foreign Individuals',
        'doing_b_i': 'Doing Business In India',
        'sector_w_fdi_l': 'Sector Wise FDI Limits',
        'scvbo': 'Subsidiary Company Vs Branch Office'
    }
    if page not in page_dict:
        raise Http404('Invalid page')

    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()

    # Serialize data
    product_serializer = ProductSerializer(products, many=True)
    meaning_serializer = MeaningSerializer(meaning)
    minimum_serializer = MinimumRequirementSerializer(minimum)
    beneift_serializer = BenefitsSerializer(benefit)
    document_serializer = DocumentRequiredSerializer(document)
    incorporation_serializer = IncorporationProcessSerializer(incorporation)
    compliance_serializer = ComplianceSerializer(compliance)
    step_serializer = StepWiseProcedureSerializer(step)
    faq_serializer = FAQSerializer(faq)
    closure_serializer = ClosureSerializer(closure)
     # create response data
    response_data = {
        'products': product_serializer.data,
        'meaning': meaning_serializer.data,
        'minimum': minimum_serializer.data,
        'benefit': beneift_serializer.data,
        'document': document_serializer.data,
        'incorporation': incorporation_serializer.data,
        'compliance': compliance_serializer.data,
        'step': step_serializer.data,
        'faq': faq_serializer.data,
        'closure': closure_serializer.data,
    }
    #Handle Post Request
    if request.method == 'POST':
        form = ContactUser(request.Post)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            response_data['form'] = serializer.data
            return JsonResponse(response_data,status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    #Handling GET request
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    response_data['banner'] = BannerSerializer(banner).data
    response_data['price'] = PricingSumSerializer(price).data
    return JsonResponse(response_data, status=200)


#SETUP INDIAN BRANCH view
def setup(request,page):
    page_dict ={
        'branch_o_f_c':'Branch Office of Foreign Company',
        'liaison_o_r':'Liaison Office Registration',
        'project_o_r':'Project Office Registration'
    }
    if page not in page_dict:
        raise Http404('Invalid page')

    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()

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
            'step':step,'faq':faq,'closure':closure}
    return render(request, f'setup_india_branch/{page}.html', context)

@api_view(['GET','POST'])
def setup_api(request,page):
    page_dict ={
        'branch_o_f_c':'Branch Office of Foreign Company',
        'liaison_o_r':'Liaison Office Registration',
        'project_o_r':'Project Office Registration'
    }
    if page not in page_dict:
        raise Http404('Invalid page')

    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()
    # Serialize data
    product_serializer = ProductSerializer(products, many=True)
    meaning_serializer = MeaningSerializer(meaning)
    minimum_serializer = MinimumRequirementSerializer(minimum)
    beneift_serializer = BenefitsSerializer(benefit)
    document_serializer = DocumentRequiredSerializer(document)
    incorporation_serializer = IncorporationProcessSerializer(incorporation)
    compliance_serializer = ComplianceSerializer(compliance)
    step_serializer = StepWiseProcedureSerializer(step)
    faq_serializer = FAQSerializer(faq)
    closure_serializer = ClosureSerializer(closure)
     # create response data
    response_data = {
        'products': product_serializer.data,
        'meaning': meaning_serializer.data,
        'minimum': minimum_serializer.data,
        'benefit': beneift_serializer.data,
        'document': document_serializer.data,
        'incorporation': incorporation_serializer.data,
        'compliance': compliance_serializer.data,
        'step': step_serializer.data,
        'faq': faq_serializer.data,
        'closure': closure_serializer.data,
    }
    #Handle Post Request
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            response_data['form'] = serializer.data
            return JsonResponse(response_data,status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    #Handling GET request
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    response_data['banner'] = BannerSerializer(banner).data
    response_data['price'] = PricingSumSerializer(price).data
    return JsonResponse(response_data, status=200)

#TRADEMAR view
def trademark(request,page):
    page_dict = {
        'renewal_tr': 'Renewal trademark registration',
        'trademark_mt':'Trademark meaning types',
        'trademark_r':'Trademark registration'
    }
    if page not in page_dict:
        raise Http404('Invalid page')

    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()

    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')

    form = ContactUser()
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            return JsonResponse(serializer.data,status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)

    context = {'products': products, 'form': form, 'price':price,'banner': banner, 'meaning':meaning,'minimum':minimum,
            'benefit':benefit, 'document':document,'incorporation':incorporation,'compliance':compliance,
            'step':step,'faq':faq,'closure':closure}
    return render(request, f'trademark/{page}.html', context)


@api_view(['GET','POST'])
def trademark_api(request,page):
    page_dict = {
        'renewal_tr': 'Renewal trademark registration',
        'trademark_mt':'Trademark meaning types',
        'trademark_r':'Trademark registration'
    }
    if page not in page_dict:
        raise Http404('Invalid page')

    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()
    # Serialize data
    product_serializer = ProductSerializer(products, many=True)
    meaning_serializer = MeaningSerializer(meaning)
    minimum_serializer = MinimumRequirementSerializer(minimum)
    beneift_serializer = BenefitsSerializer(benefit)
    document_serializer = DocumentRequiredSerializer(document)
    incorporation_serializer = IncorporationProcessSerializer(incorporation)
    compliance_serializer = ComplianceSerializer(compliance)
    step_serializer = StepWiseProcedureSerializer(step)
    faq_serializer = FAQSerializer(faq)
    closure_serializer = ClosureSerializer(closure)
     # create response data
    response_data = {
        'products': product_serializer.data,
        'meaning': meaning_serializer.data,
        'minimum': minimum_serializer.data,
        'benefit': beneift_serializer.data,
        'document': document_serializer.data,
        'incorporation': incorporation_serializer.data,
        'compliance': compliance_serializer.data,
        'step': step_serializer.data,
        'faq': faq_serializer.data,
        'closure': closure_serializer.data,
    }
    #Handle Post Request
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            response_data['form'] = serializer.data
            return JsonResponse(response_data,status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    #Handling GET request
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    response_data['banner'] = BannerSerializer(banner).data
    response_data['price'] = PricingSumSerializer(price).data
    return JsonResponse(response_data, status=200)

#COPYRIGHT & DESIGN view
def copyright(request,page):
    page_dict={
        'copyright_r':'Copyright registration',
        'coptright_t':'Copyright types',
        'design_r':'Design Registration',
        'interrnational_cr':'International Copyright Registration',
        
    }
    if page not in page_dict:
        raise Http404('Invalid Page')

    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()

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
            'step':step,'faq':faq,'closure':closure}
    return render(request, f'copyright/{page}.html', context)

@api_view(['GET','POST'])
def copyright_api(request,page):
    page_dict={
        'copyright_r':'Copyright registration',
        'coptright_t':'Copyright types',
        'design_r':'Design Registration',
        'interrnational_cr':'International Copyright Registration',
        
    }
    if page not in page_dict:
        raise Http404('Invalid Page')

    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()
    # Serialize data
    product_serializer = ProductSerializer(products, many=True)
    meaning_serializer = MeaningSerializer(meaning)
    minimum_serializer = MinimumRequirementSerializer(minimum)
    beneift_serializer = BenefitsSerializer(benefit)
    document_serializer = DocumentRequiredSerializer(document)
    incorporation_serializer = IncorporationProcessSerializer(incorporation)
    compliance_serializer = ComplianceSerializer(compliance)
    step_serializer = StepWiseProcedureSerializer(step)
    faq_serializer = FAQSerializer(faq)
    closure_serializer = ClosureSerializer(closure)
     # create response data
    response_data = {
        'products': product_serializer.data,
        'meaning': meaning_serializer.data,
        'minimum': minimum_serializer.data,
        'benefit': beneift_serializer.data,
        'document': document_serializer.data,
        'incorporation': incorporation_serializer.data,
        'compliance': compliance_serializer.data,
        'step': step_serializer.data,
        'faq': faq_serializer.data,
        'closure': closure_serializer.data,
    }
    #Handle Post Request
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            response_data['form'] = serializer.data
            return JsonResponse(response_data,status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    #Handling GET request
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    response_data['banner'] = BannerSerializer(banner).data
    response_data['price'] = PricingSumSerializer(price).data
    return JsonResponse(response_data, status=200)

#PATENT & IPR ENFORCEMENT view 
def patent(request,page):
    page_dict={
        'intellectual_pr':'Intellectual property rights',
        'international_tf':'International trademark filing',
        'patent_r':'Patent Registration',
        'patent_s':'Patent search',
        'software_p':'Software patent'
    }
    if page not in page_dict:
        raise Http404('Invalid Page')

    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()

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
            'step':step,'faq':faq,'closure':closure}
    return render(request, f'patent/{page}.html', context)

@api_view(['GET','POST'])
def patent_api(request,page):
    page_dict={
        'intellectual_pr':'Intellectual property rights',
        'international_tf':'International trademark filing',
        'patent_r':'Patent Registration',
        'patent_s':'Patent search',
        'software_p':'Software patent'
    }
    if page not in page_dict:
        raise Http404('Invalid Page')

    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()
    # Serialize data
    product_serializer = ProductSerializer(products, many=True)
    meaning_serializer = MeaningSerializer(meaning)
    minimum_serializer = MinimumRequirementSerializer(minimum)
    beneift_serializer = BenefitsSerializer(benefit)
    document_serializer = DocumentRequiredSerializer(document)
    incorporation_serializer = IncorporationProcessSerializer(incorporation)
    compliance_serializer = ComplianceSerializer(compliance)
    step_serializer = StepWiseProcedureSerializer(step)
    faq_serializer = FAQSerializer(faq)
    closure_serializer = ClosureSerializer(closure)
     # create response data
    response_data = {
        'products': product_serializer.data,
        'meaning': meaning_serializer.data,
        'minimum': minimum_serializer.data,
        'benefit': beneift_serializer.data,
        'document': document_serializer.data,
        'incorporation': incorporation_serializer.data,
        'compliance': compliance_serializer.data,
        'step': step_serializer.data,
        'faq': faq_serializer.data,
        'closure': closure_serializer.data,
    }
    #Handle Post Request
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            response_data['form'] = serializer.data
            return JsonResponse(response_data,status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    #Handling GET request
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    response_data['banner'] = BannerSerializer(banner).data
    response_data['price'] = PricingSumSerializer(price).data
    return JsonResponse(response_data, status=200)
#>FOOD BUSINESS view
def foodbusiness(request,page):
    page_dict={
        'fssai_a_r':'FSSAI Annual Return',
        'fssai_c_l':'FSSAI Central License',
        'fssai_l_r':'FSSAI License Renewal',
        'fssai_r':'FSSAI Registration',
        'fssai_s_l':'FSSAI State License',
        'fssai_a':'fssai-applicability'
        
    }
    if page not in page_dict:
        raise Http404('Invalid Page')

    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()

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
            'step':step,'faq':faq,'closure':closure}
    return render(request, f'foodbusiness/{page}.html', context)
@api_view(['GET','POST'])
def foodbusiness_api(request,page):
    page_dict={
        'fssai_a_r':'FSSAI Annual Return',
        'fssai_c_l':'FSSAI Central License',
        'fssai_l_r':'FSSAI License Renewal',
        'fssai_r':'FSSAI Registration',
        'fssai_s_l':'FSSAI State License',
        'fssai_a':'fssai-applicability'
        
    }
    if page not in page_dict:
        raise Http404('Invalid Page')

    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()
     # Serialize data
    product_serializer = ProductSerializer(products, many=True)
    meaning_serializer = MeaningSerializer(meaning)
    minimum_serializer = MinimumRequirementSerializer(minimum)
    beneift_serializer = BenefitsSerializer(benefit)
    document_serializer = DocumentRequiredSerializer(document)
    incorporation_serializer = IncorporationProcessSerializer(incorporation)
    compliance_serializer = ComplianceSerializer(compliance)
    step_serializer = StepWiseProcedureSerializer(step)
    faq_serializer = FAQSerializer(faq)
    closure_serializer = ClosureSerializer(closure)
     # create response data
    response_data = {
        'products': product_serializer.data,
        'meaning': meaning_serializer.data,
        'minimum': minimum_serializer.data,
        'benefit': beneift_serializer.data,
        'document': document_serializer.data,
        'incorporation': incorporation_serializer.data,
        'compliance': compliance_serializer.data,
        'step': step_serializer.data,
        'faq': faq_serializer.data,
        'closure': closure_serializer.data,
    }
    #Handle Post Request
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            response_data['form'] = serializer.data
            return JsonResponse(response_data,status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    #Handling GET request
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    response_data['banner'] = BannerSerializer(banner).data
    response_data['price'] = PricingSumSerializer(price).data
    return JsonResponse(response_data, status=200)
# GENERAL LICENSE view
def general(request,page):
    page_dict = {
        'apeda_r_e':'APEDA Registration For Exporter',
        'shop_e_r':'Shop and Establishment Registration',
        'trade_l_r':'Trade License Registration'
        
    }
    if page not in page_dict:
        raise Http404('Invalid Page')
    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()

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
            'step':step,'faq':faq,'closure':closure}
    return render(request, f'generallicense/{page}.html', context)
@api_view(['GET','POST'])
def general_api(request,page):
    page_dict = {
        'apeda_r_e':'APEDA Registration For Exporter',
        'shop_e_r':'Shop and Establishment Registration',
        'trade_l_r':'Trade License Registration'
        
    }
    if page not in page_dict:
        raise Http404('Invalid Page')

    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()
     # Serialize data
    product_serializer = ProductSerializer(products, many=True)
    meaning_serializer = MeaningSerializer(meaning)
    minimum_serializer = MinimumRequirementSerializer(minimum)
    beneift_serializer = BenefitsSerializer(benefit)
    document_serializer = DocumentRequiredSerializer(document)
    incorporation_serializer = IncorporationProcessSerializer(incorporation)
    compliance_serializer = ComplianceSerializer(compliance)
    step_serializer = StepWiseProcedureSerializer(step)
    faq_serializer = FAQSerializer(faq)
    closure_serializer = ClosureSerializer(closure)
     # create response data
    response_data = {
        'products': product_serializer.data,
        'meaning': meaning_serializer.data,
        'minimum': minimum_serializer.data,
        'benefit': beneift_serializer.data,
        'document': document_serializer.data,
        'incorporation': incorporation_serializer.data,
        'compliance': compliance_serializer.data,
        'step': step_serializer.data,
        'faq': faq_serializer.data,
        'closure': closure_serializer.data,
    }
    #Handle Post Request
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            response_data['form'] = serializer.data
            return JsonResponse(response_data,status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    #Handling GET request
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    response_data['banner'] = BannerSerializer(banner).data
    response_data['price'] = PricingSumSerializer(price).data
    return JsonResponse(response_data, status=200)
# INDUSTRIAL LICENSE
def industrial(request, page):
    page_dict={
        'barcode_r':'Barcode-registration',
        'dot_isp_l':'Dot isp licence',
        'dot_osp_l_r':'DOT OSP License Registration',
        'gst_r_f':'GST Return Filing',
        'import_e_c_r':'Import Export Code Renewal',
        'psara_l':'PSARA License'
        
    }
    if page not in page_dict:
        raise Http404('Invalid Page')
    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()

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
            'step':step,'faq':faq,'closure':closure}
    return render(request, f'industriallicense/{page}.html', context)
@api_view(['GET','POST'])
def industrial_api(request, page):
    page_dict={
        'barcode_r':'Barcode-registration',
        'dot_isp_l':'Dot isp licence',
        'dot_osp_l_r':'DOT OSP License Registration',
        'gst_r_f':'GST Return Filing',
        'import_e_c_r':'Import Export Code Renewal',
        'psara_l':'PSARA License'
        
    }
    if page not in page_dict:
        raise Http404('Invalid Page')
    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()
     # Serialize data
    product_serializer = ProductSerializer(products, many=True)
    meaning_serializer = MeaningSerializer(meaning)
    minimum_serializer = MinimumRequirementSerializer(minimum)
    beneift_serializer = BenefitsSerializer(benefit)
    document_serializer = DocumentRequiredSerializer(document)
    incorporation_serializer = IncorporationProcessSerializer(incorporation)
    compliance_serializer = ComplianceSerializer(compliance)
    step_serializer = StepWiseProcedureSerializer(step)
    faq_serializer = FAQSerializer(faq)
    closure_serializer = ClosureSerializer(closure)
     # create response data
    response_data = {
        'products': product_serializer.data,
        'meaning': meaning_serializer.data,
        'minimum': minimum_serializer.data,
        'benefit': beneift_serializer.data,
        'document': document_serializer.data,
        'incorporation': incorporation_serializer.data,
        'compliance': compliance_serializer.data,
        'step': step_serializer.data,
        'faq': faq_serializer.data,
        'closure': closure_serializer.data,
    }
    #Handle Post Request
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            response_data['form'] = serializer.data
            return JsonResponse(response_data,status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    #Handling GET request
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    response_data['banner'] = BannerSerializer(banner).data
    response_data['price'] = PricingSumSerializer(price).data
    return JsonResponse(response_data, status=200)


# TAX REGISTRATIONS view
def taxregister(request,page):
    page_dict={
        'cloud_a':'Cloud-accounting',
        'gst_r_in_i':'GST Registration in india',
        'import_e_c_i':'Import export Code'
        
    }
    if page not in page_dict:
        raise Http404('Invalid Page')
    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()

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
            'step':step,'faq':faq,'closure':closure}
    return render(request, f'taxregistration/{page}.html', context)
@api_view(['GET','POST'])
def taxregister_api(request, page):
    page_dict={
       'cloud_a':'Cloud-accounting',
        'gst_r_in_i':'GST Registration in india',
        'import_e_c_i':'import-export-code-iec'
        
    }
    if page not in page_dict:
        raise Http404('Invalid Page')
    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()
     # Serialize data
    product_serializer = ProductSerializer(products, many=True)
    meaning_serializer = MeaningSerializer(meaning)
    minimum_serializer = MinimumRequirementSerializer(minimum)
    beneift_serializer = BenefitsSerializer(benefit)
    document_serializer = DocumentRequiredSerializer(document)
    incorporation_serializer = IncorporationProcessSerializer(incorporation)
    compliance_serializer = ComplianceSerializer(compliance)
    step_serializer = StepWiseProcedureSerializer(step)
    faq_serializer = FAQSerializer(faq)
    closure_serializer = ClosureSerializer(closure)
     # create response data
    response_data = {
        'products': product_serializer.data,
        'meaning': meaning_serializer.data,
        'minimum': minimum_serializer.data,
        'benefit': beneift_serializer.data,
        'document': document_serializer.data,
        'incorporation': incorporation_serializer.data,
        'compliance': compliance_serializer.data,
        'step': step_serializer.data,
        'faq': faq_serializer.data,
        'closure': closure_serializer.data,
    }
    #Handle Post Request
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            response_data['form'] = serializer.data
            return JsonResponse(response_data,status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    #Handling GET request
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    response_data['banner'] = BannerSerializer(banner).data
    response_data['price'] = PricingSumSerializer(price).data
    return JsonResponse(response_data, status=200)

# TAX COMPLIANCE view
def taxcompliance(request,page):
    page_dict={
        'ad_tax':'Advance-tax',
        'income_t_r_f':'Income-tax-return-filing',
        'professional_t_r':'Professional Tax Registration',
        'registration_l':'registration-licenses',
        'tax_a_s':'Tax Assessment & Scrutiny',
        'tax_a_c':'tax-audit by ca',
        'tax_d_s':'tax-deducted-source'
        
    }
    if page not in page_dict:
        raise Http404('Invalid Page')
    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()

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
            'step':step,'faq':faq,'closure':closure}
    return render(request, f'taxcompliance/{page}.html', context)
@api_view(['GET','POST'])
def taxcompliance_api(request,page):
    page_dict={
        'ad_tax':'Advance-tax',
        'income_t_r_f':'Income-tax-return-filing',
        'professional_t_r':'Professional Tax Registration',
        'registration_l':'registration-licenses',
        'tax_a_s':'Tax Assessment & Scrutiny',
        'tax_a_c':'tax-audit by ca',
        'tax_d_s':'tax-deducted-source'
        
    }
    if page not in page_dict:
        raise Http404('Invalid Page')
    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()
    # Serialize data
    product_serializer = ProductSerializer(products, many=True)
    meaning_serializer = MeaningSerializer(meaning)
    minimum_serializer = MinimumRequirementSerializer(minimum)
    beneift_serializer = BenefitsSerializer(benefit)
    document_serializer = DocumentRequiredSerializer(document)
    incorporation_serializer = IncorporationProcessSerializer(incorporation)
    compliance_serializer = ComplianceSerializer(compliance)
    step_serializer = StepWiseProcedureSerializer(step)
    faq_serializer = FAQSerializer(faq)
    closure_serializer = ClosureSerializer(closure)
     # create response data
    response_data = {
        'products': product_serializer.data,
        'meaning': meaning_serializer.data,
        'minimum': minimum_serializer.data,
        'benefit': beneift_serializer.data,
        'document': document_serializer.data,
        'incorporation': incorporation_serializer.data,
        'compliance': compliance_serializer.data,
        'step': step_serializer.data,
        'faq': faq_serializer.data,
        'closure': closure_serializer.data,
    }
    #Handle Post Request
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            response_data['form'] = serializer.data
            return JsonResponse(response_data,status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    #Handling GET request
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    response_data['banner'] = BannerSerializer(banner).data
    response_data['price'] = PricingSumSerializer(price).data
    return JsonResponse(response_data, status=200)

# PAYROLL & FUNDING view
def payrollfunding(request,page):
    page_dict={
        'epf_r':'EPF Registration',
        'esic_r':'esic-registration',
        'tax_p':'Tax and Payroll',
        
    }
    if page not in page_dict:
        raise Http404('Invalid Page')
    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()

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
            'step':step,'faq':faq,'closure':closure}
    return render(request, f'payrollfunding/{page}.html', context)

@api_view(['GET','POST'])
def payrollfunding_api(request,page):
    page_dict={
        'epf_r':'EPF Registration',
        'esic_r':'esic-registration',
        'tax_p':'Tax and Payroll',
        
    }
    if page not in page_dict:
        raise Http404('Invalid Page')
    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()
    # Serialize data
    product_serializer = ProductSerializer(products, many=True)
    meaning_serializer = MeaningSerializer(meaning)
    minimum_serializer = MinimumRequirementSerializer(minimum)
    beneift_serializer = BenefitsSerializer(benefit)
    document_serializer = DocumentRequiredSerializer(document)
    incorporation_serializer = IncorporationProcessSerializer(incorporation)
    compliance_serializer = ComplianceSerializer(compliance)
    step_serializer = StepWiseProcedureSerializer(step)
    faq_serializer = FAQSerializer(faq)
    closure_serializer = ClosureSerializer(closure)
     # create response data
    response_data = {
        'products': product_serializer.data,
        'meaning': meaning_serializer.data,
        'minimum': minimum_serializer.data,
        'benefit': beneift_serializer.data,
        'document': document_serializer.data,
        'incorporation': incorporation_serializer.data,
        'compliance': compliance_serializer.data,
        'step': step_serializer.data,
        'faq': faq_serializer.data,
        'closure': closure_serializer.data,
    }
    #Handle Post Request
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            response_data['form'] = serializer.data
            return JsonResponse(response_data,status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    #Handling GET request
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    response_data['banner'] = BannerSerializer(banner).data
    response_data['price'] = PricingSumSerializer(price).data
    return JsonResponse(response_data, status=200)
# BASIC ROC COMPLIANCES view
def basicroc(request,page):
    page_dict={
        'director_kyc':'2022 Director KYC [DIR-3-KYC]',
        'company_a_r':'Company Annual Return',
        'director_i_n':'Director Identification Number',
        'file_inc':'File INC 20-A',
        'post_i_c':'Post Incorporation Compliance',
        'roc_c':'Roc'
    }
    if page not in page_dict:
        raise Http404('Invalid Page')
    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()

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
            'step':step,'faq':faq,'closure':closure}
    return render(request, f'basicroc/{page}.html', context)
@api_view(['GET','POST'])
def basicroc_api(request,page):
    page_dict={
        'director_kyc':'2022 Director KYC [DIR-3-KYC]',
        'company_a_r':'Company Annual Return',
        'director_i_n':'Director Identification Number (DIN)',
        'file_inc':'File INC 20-A (Business Commencement)',
        'post_i_c':'Post Incorporation Compliance',
        'roc_c':'Roc'
    }
    if page not in page_dict:
        raise Http404('Invalid Page')
    products = Product.objects.filter(category=page_dict.get(page))
    meaning = Meaning.objects.filter(category=page_dict.get(page)).first()
    minimum = MinimumRequirement.objects.filter(category=page_dict.get(page)).first()
    benefit = Benefits.objects.filter(category=page_dict.get(page)).first()
    document = DocumentRequired.objects.filter(category=page_dict.get(page)).first()
    incorporation = IncorporationProcess.objects.filter(category=page_dict.get(page)).first()
    compliance = Compliance.objects.filter(category=page_dict.get(page)).first()
    step = StepWiseProcedure.objects.filter(category=page_dict.get(page)).first()
    faq = FAQ.objects.filter(category=page_dict.get(page)).first()
    closure = Closure.objects.filter(category=page_dict.get(page)).first()
    # Serialize data
    product_serializer = ProductSerializer(products, many=True)
    meaning_serializer = MeaningSerializer(meaning)
    minimum_serializer = MinimumRequirementSerializer(minimum)
    beneift_serializer = BenefitsSerializer(benefit)
    document_serializer = DocumentRequiredSerializer(document)
    incorporation_serializer = IncorporationProcessSerializer(incorporation)
    compliance_serializer = ComplianceSerializer(compliance)
    step_serializer = StepWiseProcedureSerializer(step)
    faq_serializer = FAQSerializer(faq)
    closure_serializer = ClosureSerializer(closure)
     # create response data
    response_data = {
        'products': product_serializer.data,
        'meaning': meaning_serializer.data,
        'minimum': minimum_serializer.data,
        'benefit': beneift_serializer.data,
        'document': document_serializer.data,
        'incorporation': incorporation_serializer.data,
        'compliance': compliance_serializer.data,
        'step': step_serializer.data,
        'faq': faq_serializer.data,
        'closure': closure_serializer.data,
    }
    #Handle Post Request
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            serializer = ContactUserSerializer(form.instance)
            response_data['form'] = serializer.data
            return JsonResponse(response_data,status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    #Handling GET request
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    response_data['banner'] = BannerSerializer(banner).data
    response_data['price'] = PricingSumSerializer(price).data
    return JsonResponse(response_data, status=200)
    
# COMPANY CHANGES & RETURN view

def change_d(request):
    return render(request, 'companychanges/change_d.html')


def change_m_o(request):
    return render(request, 'companychanges/change_m_o.html')


def company_n_c(request):
    return render(request, 'companychanges/company_n_c.html')


def increase_a_c(request):
    return render(request, 'companychanges/increase_a_c.html')


def registered_o_c(request):
    return render(request, 'companychanges/registered_o_c.html')


def share_t_c(request):
    return render(request, 'companychanges/share_t_c.html')

# CONVERT TO PRIVATE LIMITED view

def llp_p_l(request):
    return render(request, 'convert_to_private_comp/llp_p_l.html')


# OTHER CONVERSIONS view 

def active_c_d_c_s(request):
    return render(request, 'otherconversion/active_c_d_c_s.html')

def dormant_a_s(request):
    return render(request, 'otherconversion/dormant_a_s.html')

# CLOSURE OF BUSINESS view

def winging_u_c(request):
    return render(request, 'closure_bussiness/winging_u_c.html')

def sent_w_u_i(request):
    return render(request, 'closure_bussiness/sent_w_u_i.html')


def hire(request):
    return render(request, 'common_pages/hire.html')

def jobs(request):
    return render(request, 'jobs.html')


def contact(request):
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactUser()
    return render(request, 'contact.html', {'form': form})

def profile(request):
    form1 = ProfileUser()
    if request.method =='POST':
        form1 = ProfileUser(request.POST)
        if form1.is_valid():
            form1.save()
            messages.success(request, 'Your profile is being succesfully created')
            return redirect('home')
        else:
            messages.error(request, 'Please fill all fields correctly as mentioned')
            return render(request, 'register/profile.html', {'form1':ProfileUser})
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
        # print('Your success is:', verify)
    return render(request, 'register/profile.html', {'form1':ProfileUser})


def signup(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(email=form.cleaned_data.get('email'))
            token = str(random.randint(100000, 999999))
            user.otp = token
            user.save()
            request.session['user_email'] = user.email
            send_mail(
                'Email Verification', 
                f'Your otp is {token}',
                 settings.EMAIL_HOST_USER,
                  [user.email], 
                  fail_silently=False,
                  )
            messages.success(request, " Verification email is being sent on your Registered Email")
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
    return render(request, 'register/signup.html',{'form':form})

def verify(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        email = request.session.get('user_email')
        if not otp:
            messages.error(request, "Please enter OTP")
            return redirect('verify')
        user = User.objects.get(email=email)
        if user.otp == otp:
            user.is_verified =True
            user.save()
            messages.success(request, " Your accounts has been verified please Login to complete your profile")
            return redirect('auth_login')
        else:
            messages.error(request, "Invalid OTP")
            return redirect('verify')
    return render(request, 'register/verify.html')

def auth_login(request):
    if request.method == 'POST':
        loginusername = request.POST['username']
        loginpassword = request.POST['password']
        user = authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('auth_login')
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

    return render(request, 'register/auth_login.html')
def auth_logout(request):
    logout(request)
    messages.success(request, 'You have been sucessfully logged out')
    return redirect('home')
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            token = str(random.randint(100000, 999999))
            user.otp_for_forgot_pass = token
            user.save()
            request.session['user_email'] = user.email
            send_mail(
                'Password Reset', 
                f'Your otp is {token}',
                 settings.EMAIL_HOST_USER,
                  [user.email], 
                  fail_silently=False,
                  )
            messages.success(request, "OTP has been sent to your email")
            return redirect('password_otp')
        except User.DoesNotExist:
            messages.error(request, "Email is not registered")
            return redirect('forgot_password')
    return render(request, 'register/forgot_password.html')
def password_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        email = request.session.get('user_email')
        if not otp:
            messages.error(request, "Please enter OTP")
            return redirect('password_otp')
        user = User.objects.get(email=email)
        if user.otp_for_forgot_pass == otp:
            request.session['otp_verified'] = True
            messages.success(request, "OTP verified, please set a new password")
            return redirect('password_reset')
        else:
            messages.error(request, "Invalid OTP")
            return redirect('password_otp')
    return render(request, 'register/password_otp.html')
def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = request.session.get('user_email')
            user = User.objects.get(email=email)
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            update_session_auth_hash(request, user) 
            messages.success(request, "Password reset successful, please login")
            return redirect('auth_login')
        else:
            messages.error(request, "Form is not valid")
            return render(request, 'password_reset.html', {'form': form})
    else:
        form = PasswordResetForm()
        return render(request, 'register/password_reset.html', {'form': form})
from datetime import datetime


# Order Management
# def checkout(request):
#     id = request.GET.get("id")
#     order_id = request.GET.get("order_id")
#     try:
#         product = Product.objects.get(id=id)
#         if order_id:
#             print("Oder id ", order_id)
#             order = Order.objects.get(id=order_id)
#         else:
#             order = Order()
#         final_price = product.gst + product.other_cost + product.Dobiz_India_Filings

#         if request.method == 'POST' and request.POST.get("coupan"):
#             try:
#                 coupan = request.POST.get("coupan")
#                 offer = Coupan.objects.filter(active=1).get(coupan=coupan)
#                 final_price = final_price - offer.amount
#             except Exception as e:
#                 print("Error : ", e)

#         elif request.method == 'POST':
#             remark = request.POST.get("remark")
#             user = User.objects.get(id=request.user.id)

#             order.product = product
#             order.user = user
#             order.is_cart = 0
#             order.status = "Success"
#             order.name = user.name
#             order.email = user.email
#             order.remarks = remark
#             order.buy_time = datetime.now()
#             order.save()
#             return redirect("/order_history")
#         client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
#         amount = int(final_price * 100)
#         Print('*****************************')
#         print(payment)
#         Print('*****************************')
#         payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': 1})
#         order.razor_pay_order_id = payment['id']
#         order.save()
#         context = {"product": product,
#                    "final_price": final_price,
#                    "payment": payment
#                    }
#     except:
#         context = {}
#     return render(request, "order/checkout.html", context)

def order_history(request):
    orders = Order.objects.filter(user__id = request.user.id).filter(is_cart=0).order_by("-id")
    context = {"orders":orders}
    return render(request,"order/order_history.html",context)


from django.utils import timezone

def cart(request):
    items = Order.objects.filter(user__id=request.user.id).filter(is_cart=1).order_by("-id")
    coupan = request.POST.get("coupan")
    final_price = 0
    for item in items:
        final_price += item.product.price

    if request.method == 'POST' and coupan:
        try:
            coupan = coupan.upper()
            offer = Coupan.objects.filter(active=1).get(coupan=coupan) #checks for username and user
            for item in items:
                product = item.product
                if offer.percentage is not None and offer.amount is not None:
                    product_cost = product.Dobiz_India_Filings + product.gst + product.other_cost
                    discounted_price_percentage = product_cost - (product_cost * offer.percentage / 100)
                    discounted_price_amount = product_cost - offer.amount
                    if discounted_price_percentage > discounted_price_amount:
                        product_cost = discounted_price_percentage
                    else:
                        product_cost = discounted_price_amount
                elif offer.percentage is not None:
                    product_cost = product.Dobiz_India_Filings + product.gst + product.other_cost
                    product_cost = product_cost - (product_cost * offer.percentage / 100)
                elif offer.amount is not None:
                    product_cost = product.Dobiz_India_Filings + product.gst + product.other_cost
                    product_cost = product_cost - offer.amount
                item.final_price = product_cost
                item.save()
            if offer.percentage is not None:
                final_price -= final_price * offer.percentage / 100
                messages.success(request, "Coupon Applied")
            else:
                final_price -= offer.amount
                messages.success(request, "Coupon Applied")
        except Coupan.DoesNotExist:
            messages.error(request, "Invalid Coupon, Please Try Again")
        except Exception as e:
            print("Error : ", e)

    client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
    amount = int(final_price * 100)
    payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': 1})

    # Check if the payment is successful
    if payment['status'] == 'captured':
        # Create an order object for each item in the cart with the payment status 'success'
        for item in items:
            product = item.product
            user = request.user
            order = Order.objects.create(product=product, user=user, is_cart=0, status='success', name=user.name, email=user.email, buy_time=timezone.now(), razor_pay_order_id=payment['id'])

    context = {"items": items,
               "final_price": final_price,
               "payment": payment,
               "coupan":coupan
              }
    return render(request, "order/cart.html", context)





@csrf_exempt
def addToCart(request):
    id = request.POST.get("id")
    product = Product.objects.get(id = id)
    user = User.objects.get(id = request.user.id)
    order = Order()
    remark = ""
    order.product = product
    order.user = user
    order.is_cart = 1
    order.status ="In Cart"
    order.name = user.name
    order.email = user.email
    order.remarks = remark
    order.buy_time = datetime.now()
    order.save()
    return JsonResponse({"Success":1})

# def dashboar(requets):
#     user = user.res(user)
#     coupan = couapn.objet(userid=user)
#     for i in couan:
#         order = Order.object.filter(coupan.id)
#         tim
        
#         yar
#         month
#         week