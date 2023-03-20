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
path("checkout",views.checkout,name="checkout"),
path('order_history',views.order_history,name="order_history"),
path('cart',views.cart,name="cart"),
path('addToCart',views.addToCart, name="addToCart"),
# path('success',views.success, name="success"),
# path('handlerequest',views.handlerequest, name="handlerequest"),


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

path('director_kyc', views.director_kyc, name='director_kyc'),

path('company_a_r', views.company_a_r, name='company_a_r'),

path('director_i_n', views.director_i_n, name='director_i_n'),

path('file_inc', views.file_inc, name='file_inc'),

path('post_i_c', views.post_i_c, name='post_i_c'),

path('roc_c', views.roc_c, name='roc_c'),

# COMPANY CHANGES & RETURN url

path('change_d', views.change_d, name='change_d'),

path('change_m_o', views.change_m_o, name='change_m_o'),

path('company_n_c', views.company_n_c, name='company_n_c'),

path('increase_a_c', views.increase_a_c, name='increase_a_c'),

path('registered_o_c', views.registered_o_c, name='registered_o_c'),

path('share_t_c', views.share_t_c, name='share_t_c'),

# CONVERT TO PRIVATE LIMITED url

path('llp_p_l', views.llp_p_l, name='llp_p_l'),

# OTHER CONVERSIONS url

path('active_c_d_c_s', views.active_c_d_c_s, name='active_c_d_c_s'),

path('dormant_a_s', views.dormant_a_s, name='dormant_a_s'),

# CLOSURE OF BUSINESS url

path('winging_u_c', views.winging_u_c, name='winging_u_c'),
path('sent_w_u_i', views.sent_w_u_i, name='sent_w_u_i'),



    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# path using <str>