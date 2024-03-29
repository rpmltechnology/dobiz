from django.contrib import admin
from django.urls import path, include
from . import views
#managing media imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url
from django.views.static import serve
urlpatterns = [
url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
#cookie
path('privacy-policy',views.privacy,name='privacy-policy'),
path('cancellation-policy',views.cancellation,name='cancellation-policy'),
path('refund-policy',views.refund,name='refund-policy'),
path('terms-and-conditions',views.terms,name='terms-and-conditions'),

path('', views.home, name='home'),
#order now url

path('search', views.search, name="search"),
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
path('order', views.order, name='order'),
path('ordersucess', views.ordersucess, name='ordersucess'),
path('orderfail', views.orderfail, name='orderfail'),
path('cancel-order/<int:order_id>/', views.cancel_order, name='cancel_order'),
path('cancel_order_page/<int:order_id>/', views.cancel_order_page, name='cancel_order_page'),
path('cancelstatus',views.cancelstatus,name='cancelstatus'),
path("checkout",views.checkout,name="checkout"),
path('order_history',views.order_history,name="order_history"),
# path('cart',views.cart,name="cart"),
path('card',views.card,name="card"),
path('addToCart',views.addToCart, name="addToCart"),
path('dashboard',views.dashboard, name="dashboard"),
path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
# path('success',views.success, name="success"),
# path('handlerequest',views.handlerequest, name="handlerequest"),
path('viewproduct/product_id=<int:id>/', views.viewproduct, name='viewproduct'),

#CommonPages
path('commonPages', views.commonPages, name='commonPages'),

#MOST POPULAR URL
path('mostpopular_api/<str:page>/', views.mostpopular_api, name='mostpopular_api'),



# SPECIAL BUSINESS URL
path('specialbusiness/<str:page>/', views.specialbussiness_page, name='specialbusiness'),
path('specialbusiness_api/<str:page>/', views.specialbussiness_api, name='specialbusiness_api'),

#NGO URL
path('ngo/<str:page>/', views.ngo_page, name='ngo'),
path('ngo_api/<str:page>/', views.ngo_api, name='ngo_api'),


#Startup Services URL
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

    
]
handler404 = 'dobiz.views.four0four'
handler500 = 'dobiz.views.server_error'

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
