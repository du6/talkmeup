from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from userprofile.models import LeavedMessage, CompanyUserProfile, PersonalUserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Input a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        

class CompanySignUpForm(forms.ModelForm):
    class Meta:
        model = CompanyUserProfile
        fields = ('email', )


class PersonalSignUpForm(forms.ModelForm):
    class Meta:
        model = PersonalUserProfile
        fields = ('email', )


class LeavedMessageForm(forms.ModelForm):
    class Meta:
        model = LeavedMessage
        fields = ('name', 'email', 'message',)
