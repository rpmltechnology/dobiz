from django.contrib import admin
from django.urls import path, include
from . import views

#managing media imports
from django.conf import settings
from django.conf.urls.static import static
from django. views. static import serve
from django. urls import re_path as url
app_name = 'dobizblog'

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('', views.blog, name='bloghome'),
    path('postComment/', views.postComment, name='postComment'),
    path('blog/<str:page>/', views.blog_post, name='blog_post'),
    path('post/<int:pk>',views.oneblog, name='oneblog'),
    path('load', views.load_more, name='load'),

]

handler404 = 'dobiz.views.four0four'

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

