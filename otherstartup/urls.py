from django.contrib import admin
from django.urls import path, include
from . import views
#managing media imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url
from django.views.static import serve
app_name ='otherstartup'
urlpatterns =[
    # path('mostpopular_api/<str:page>/', views.mostpopular_api, name='mostpopular_api'),
    path('<str:page>', views.startup, name='start-up-services'),

]