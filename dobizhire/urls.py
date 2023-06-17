from django.contrib import admin
from django.urls import path, include
from . import views
#managing media imports
from django.conf import settings
from django.conf.urls.static import static
from django. urls import re_path as url
from django. views. static import serve
app_name = 'dobizhire'
urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('', views.hire, name='hire'),
    path('post/<int:id>/', views.viewjobs, name='viewjobs'),
    path('opportunities/<int:id>/', views.opportunities, name='opportunities'),
    path('thank/', views.thank, name='thank'),
]
handler404 = 'dobiz.views.four0four'

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)