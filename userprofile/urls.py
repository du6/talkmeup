from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from userprofile import views

urlpatterns = [
    url(r'^userprofile/$', views.UserProfileList.as_view()),
    url(r'^userprofile/(?P<pk>[0-9]+)/$', views.UserProfileDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
