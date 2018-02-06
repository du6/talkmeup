from django.conf.urls import url
from . import views

app_name = 'demo'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^check/(?P<performance_key>\w+)$', views.check, name='check'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^factors/(?P<performance_key>\w+)$', views.factors, name='factors'),
    url(r'^share$', views.share, name='share'),
    url(r'^thanks$', views.thanks, name='thanks'),
    url(r'^tips/(?P<performance_key>\w+)$', views.tips, name='tips'),
    url(r'^performance/$', views.PerformanceAdmin, name='performance_admin'),
]
