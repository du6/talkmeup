from django.contrib import admin

from django.contrib import admin
from .models import UserProfile, PersonalUserProfile, CompanyUserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(PersonalUserProfile)
admin.site.register(CompanyUserProfile)
