"""talkmeup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from userprofile import views as userprofile_views
from uploads import views as upload_views

urlpatterns = [
    url(r'^demo/', include('demo.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^$', userprofile_views.home, name='home'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('userprofile.urls')),
    url(r'^coach/', include('coach.urls')),
    url(r'^signup$', userprofile_views.signup, name='signup'),
    url(r'^company-signup$', userprofile_views.company_signup, name='company-signup'),
    url(r'^uploads/', include('uploads.urls')),
    url(r'^contact/', userprofile_views.contact, name='contact'),
]

if settings.DEBUG is True:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
