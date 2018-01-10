from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from rest_framework import permissions
from rest_framework import generics

from userprofile.forms import LeavedMessageForm, SignUpForm, CompanySignUpForm, PersonalSignUpForm
from userprofile.models import UserProfile, CompanyUserProfile, PersonalUserProfile
from userprofile.permissions import IsOwner
from userprofile.serializers import UserProfileSerializer
from userprofile.tokens import account_activation_token


class UserProfileList(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return UserProfile.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsOwner,)


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.save()
            UserProfile.objects.create(owner=user)
            user.userprofile.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'userprofile/signup.html', {'form': form})


def company_contact(request):
    if request.method == 'POST':
        form = CompanySignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if not CompanyUserProfile.objects.filter(email=email):
                form.save()
    return redirect('home')


def personal_contact(request):
    if request.method == 'POST':
        form = PersonalSignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if not PersonalUserProfile.objects.filter(email=email):
                form.save()
    return redirect('home')


def save_profile_for_social_user(backend, user, response, *args, **kwargs):
    if not UserProfile.objects.filter(owner=user):
        UserProfile.objects.create(owner=user)
        user.userprofile.save()


def leave_message(request):
    if request.method == 'POST':
        form = LeavedMessageForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('home')
