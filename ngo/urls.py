from django.contrib import admin
from django.urls import path, include
from . import views
#managing media imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url
from django.views.static import serve
app_name ='ngo'
urlpatterns =[
    path('<str:page>', views.NGO, name='ngo'),

]