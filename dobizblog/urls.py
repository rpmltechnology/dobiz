from django.contrib import admin
from django.urls import path, include
from . import views

#managing media imports
from django.conf import settings
from django.conf.urls.static import static
app_name = 'dobizblog'

urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path('post/<int:pk>/', views.blogpost, name='blogpost'),

]