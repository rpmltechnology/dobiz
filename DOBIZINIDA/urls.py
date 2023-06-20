
from django.contrib import admin
from django.urls import path, include
# from cookie_consent.views import cookie_consent
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dobiz.urls')),
    path('blog',include('dobizblog.urls')),
    path('hire/',include('dobizhire.urls')),
    path('foreign-owners/',include('foreignowner.urls')),
    path('ngo/',include('ngo.urls')),
    path('indian-owners/',include('indainowner.urls')),
     path('start-up-services/',include('otherstartup.urls')),
    # path('cookie-consent/', cookie_consent, name='cookie_consent'),
]
