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

#MOST POPULAR 
path('mostpopular_api/<str:page>/', views.mostpopular_api, name='mostpopular_api'),



#MOST POPULAR API

path('mostpopular/<str:page>/', views.mostpopular_page, name='mostpopular'),

# SPECIAL BUSINESS

path('specialbusiness/<str:page>/', views.special_business_page, name='specialbusiness'),

# SPECIAL BUSINESS API
path('specialbussiness_api/<str:page>/', views.specialbussiness_api, name='specialbussiness_api'),


#ngo url
path('trust_registration', views.trust_registration, name='trust_registration'),

path('society_registration', views.society_registration, name='society_registration'),

path('section_8', views.section_8, name='section_8'),

path('roc', views.roc, name='roc'),

path('patent', views.patent, name='patent'),

path('startup', views.startup, name='startup'),



#do bussines in india url

path('company_f_i', views.company_f_i, name='company_f_i'),

path('doing_b_i', views.doing_b_i, name='doing_b_i'),

path('sector_w_fdi_l', views.sector_w_fdi_l, name='sector_w_fdi_l'),

path('scvbo', views.scvbo, name='scvbo'),

    
#SETUP INDIAN BRANCH url

path('branch_o_f_c', views.branch_o_f_c, name='branch_o_f_c'),

path('liaison_o_r', views.liaison_o_r, name='liaison_o_r'),

path('project_o_r', views.project_o_r, name='project_o_r'),

#TRADEMAR url
path('renewal_tr', views.renewal_tr, name='renewal_tr'),

path('trademark_mt', views.trademark_mt, name='trademark_mt'),

path('trademark_r', views.trademark_r, name='trademark_r'),

#COPYRIGHT & DESIGN url

path('copyright_r', views.copyright_r, name='copyright_r'),

path('coptright_t', views.coptright_t, name='coptright_t'),

path('design_r', views.design_r, name='design_r'),

path('interrnational_cr', views.interrnational_cr, name='interrnational_cr'),

#PATENT & IPR ENFORCEMENT urls

path('intellectual_pr', views.intellectual_pr, name='intellectual_pr'),

path('international_tf', views.international_tf, name='international_tf'),

path('patent_r', views.patent_r, name='patent_r'),

path('patent_s', views.patent_s, name='patent_s'),

path('software_p', views.software_p, name='software_p'),
# >FOOD BUSINESS url

path('fssai_a_r', views.fssai_a_r, name='fssai_a_r'),

path('fssai_c_l', views.fssai_c_l, name='fssai_c_l'),

path('fssai_l_r', views.fssai_l_r, name='fssai_l_r'),

path('fssai_r', views.fssai_r, name='fssai_r'),

path('fssai_s_l', views.fssai_s_l, name='fssai_s_l'),

path('fssai_a', views.fssai_a, name='fssai_a'),

# GENERAL LICENSE urls

path('apeda_r_e', views.apeda_r_e, name='apeda_r_e'),

path('shop_e_r', views.shop_e_r, name='shop_e_r'),

path('trade_l_r', views.trade_l_r, name='trade_l_r'),

# INDUSTRIAL LICENSE
path('barcode_r', views.barcode_r, name='barcode_r'),

path('dot_isp_l', views.dot_isp_l, name='dot_isp_l'),

path('dot_osp_l_r', views.dot_osp_l_r, name='dot_osp_l_r'),

path('gst_r_f', views.gst_r_f, name='gst_r_f'),

path('import_e_c_r', views.import_e_c_r, name='import_e_c_r'),

path('psara_l', views.psara_l, name='psara_l'),

# TAX REGISTRATIONS url

path('cloud_a', views.cloud_a, name='cloud_a'),

path('gst_r_in_i', views.gst_r_in_i, name='gst_r_in_i'),

path('import_e_c_i', views.import_e_c_i, name='import_e_c_i'),


# TAX COMPLIANCE url

path('ad_tax', views.ad_tax, name='ad_tax'),

path('income_t_r_f', views.income_t_r_f, name='income_t_r_f'),

path('professional_t_r', views.professional_t_r, name='professional_t_r'),

path('registration_l', views.registration_l, name='registration_l'),

path('tax_a_s', views.tax_a_s, name='tax_a_s'),

path('tax_a_c', views.tax_a_c, name='tax_a_c'),

path('tax_d_s', views.tax_d_s, name='tax_d_s'),

# PAYROLL & FUNDINGc url

path('epf_r', views.epf_r, name='epf_r'),

path('esic_r', views.esic_r, name='esic_r'),

path('tax_p', views.tax_p, name='tax_p'),

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