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
    path('postComment/', views.postComment, name='postComment'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# from django_comments_xtd import views as xtd_views
# app_name = 'dobizblog'

# urlpatterns = [
#     path('', views.bloghome, name='bloghome'),
#     path('post/<int:pk>/', views.blogpost, name='blogpost'),
#     path('comments/', include('django_comments_xtd.urls')),
# ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)