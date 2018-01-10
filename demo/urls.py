from django.conf.urls import url
from . import views

app_name = 'demo'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^check$', views.check, name='check'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^factors$', views.factors, name='factors'),
    url(r'^share$', views.share, name='share'),
    url(r'^thanks$', views.thanks, name='thanks'),
    url(r'^tips$', views.tips, name='tips'),
]
