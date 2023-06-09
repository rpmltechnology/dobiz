
from django.contrib import admin
from django.urls import path, include
# from cookie_consent.views import cookie_consent
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dobiz.urls')),
    path('blog',include('dobizblog.urls')),
    path('hire',include('dobizhire.urls')),
    # path('cookie-consent/', cookie_consent, name='cookie_consent'),
]
