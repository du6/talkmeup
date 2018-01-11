from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from userprofile.models import ContactedUserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Input a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        

class CompanySignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Input a valid email address.')
    companyName = forms.CharField(max_length=100)
    message = forms.CharField(max_length=500)
    
    class Meta:
        model = User
        fields = ('companyName', 'username', 'email', 'password1', 'password2', 'message')


class ContactedUserForm(forms.ModelForm):
    class Meta:
        model = ContactedUserProfile
        fields = ('contactName', 'contactEmail', 'contactPhone', 'contactMessage', )
