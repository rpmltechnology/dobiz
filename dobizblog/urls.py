from django.contrib import admin
from django.urls import path, include
from . import views

#managing media imports
from django.conf import settings
from django.conf.urls.static import static
app_name = 'dobizblog'

urlpatterns = [
    path('', views.blog, name='bloghome'),
    path('postComment/', views.postComment, name='postComment'),
    path('blog/<str:page>/', views.blog_post, name='blog_post'),
    path('post/<int:pk>',views.oneblog, name='oneblog'),
    path('load', views.load_more, name='load'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)