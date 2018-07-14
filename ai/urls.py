from django.conf.urls import url
from . import views

app_name = 'ai'

urlpatterns = [
    url(r'^upload/', views.upload, name='upload'),
    url(r'^data/', views.data, name='data'),
]
