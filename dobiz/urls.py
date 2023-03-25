from django.contrib import admin
from django.urls import path, include
from . import views

#managing media imports
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
#order now url
path('order', views.order, name='order'),

path('hire', views.hire, name='hire'),
path('jobs', views.jobs, name='jobs'),
path('contact', views.contact, name='contact'),
path('profile', views.profile, name='profile'),
path('signup/', views.signup,name='signup'),
path('verify/', views.verify, name='verify'),
path('auth_login',views.auth_login,name='auth_login'),
path('auth_logout',views.auth_logout,name='auth_logout'),
path('forgot_password/', views.forgot_password, name='forgot_password'),
path('password_otp/', views.password_otp, name='password_otp'),
path('password_reset/', views.password_reset, name='password_reset'),
    
    # Order Management
# path("checkout",views.checkout,name="checkout"),
path('order_history',views.order_history,name="order_history"),
path('cart',views.cart,name="cart"),
path('addToCart',views.addToCart, name="addToCart"),
# path('success',views.success, name="success"),
# path('handlerequest',views.handlerequest, name="handlerequest"),
path('viewproduct/user_id=<int:user_id>/product_id=<int:id>/', views.viewproduct, name="viewproduct"),

#MOST POPULAR URL
path('mostpopular_api/<str:page>/', views.mostpopular_api, name='mostpopular_api'),
path('mostpopular/<str:page>/', views.mostpopular_page, name='mostpopular'),


# SPECIAL BUSINESS URL
path('specialbusiness/<str:page>/', views.specialbussiness_page, name='specialbusiness'),
path('specialbusiness_api/<str:page>/', views.specialbussiness_api, name='specialbusiness_api'),

#NGO URL
path('ngo/<str:page>/', views.ngo_page, name='ngo'),
path('ngo_api/<str:page>/', views.ngo_api, name='ngo_api'),


# DO BUSINESS IN INDIA URL
path('do_bussiness/<str:page>/', views.do_bussiness, name='do_bussiness'),
path('do_bussiness_api/<str:page>/', views.do_bussiness_api, name='do_bussiness_api'),
    
#SETUP INDIAN BRANCH URL
path('setup/<str:page>/', views.setup, name='setup'),
path('setup_api/<str:page>/', views.setup_api, name='setup_api'),

#TRADEMARK URL
path('trademark/<str:page>/', views.trademark, name='trademark'),
path('trademark_api/<str:page>/', views.trademark_api, name='trademark_api'),


#COPYRIGHT & DESIGN url
path('copyright/<str:page>/', views.copyright, name='copyright'),
path('copyright_api/<str:page>/', views.copyright_api, name='copyright_api'),


#PATENT & IPR ENFORCEMENT URL
path('patent/<str:page>/', views.patent, name='patent'),
path('patent_api/<str:page>/', views.patent_api, name='patent_api'),


# FOOD BUSINESS url
path('foodbusiness/<str:page>/', views.foodbusiness, name='foodbusiness'),
path('foodbusiness_api/<str:page>/', views.foodbusiness_api, name='foodbusiness_api'),


# GENERAL LICENSE urls
path('general/<str:page>/', views.general, name='general'),
path('general_api/<str:page>/', views.general_api, name='general_api'),


# INDUSTRIAL LICENSE
path('industrial/<str:page>/', views.industrial, name='industrial'),
path('industrial_api/<str:page>/', views.industrial_api, name='industrial_api'),

# TAX REGISTRATIONS url
path('taxregister/<str:page>/', views.taxregister, name='taxregister'),
path('taxregister_api/<str:page>/', views.taxregister_api, name='taxregister_api'),

# TAX COMPLIANCE url
path('taxcompliance/<str:page>/', views.taxcompliance, name='taxcompliance'),
path('taxcompliance_api/<str:page>/', views.taxcompliance_api, name='taxcompliance_api'),


# PAYROLL & FUNDINGc url
path('payrollfunding/<str:page>/', views.payrollfunding, name='payrollfunding'),
path('payrollfunding_api/<str:page>/', views.payrollfunding_api, name='payrollfunding_api'),

# BASIC ROC COMPLIANCES url
path('basicroc/<str:page>/', views.basicroc, name='basicroc'),

path('basicroc_api/<str:page>/', views.basicroc_api, name='basicroc_api'),

# COMPANY CHANGES & RETURN url
path('companychanges/<str:page>/', views.companychanges, name='companychanges'),
path('companychanges_api/<str:page>/', views.companychanges_api, name='companychanges_api'),

#Exit Business
path('exitbussiness/<str:page>/', views.exitbussiness, name='exitbussiness'),
path('exitbussiness_api/<str:page>/', views.exitbussiness_api, name='exitbussiness_api'),

    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# path using <str>