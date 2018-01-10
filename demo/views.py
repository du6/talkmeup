from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-you.html')

def check(request):
    return render(request, 'check.html')

def contact(request):
    return render(request, 'contact.html')

def factors(request):
    return render(request, 'factors.html')

def share(request):
    return render(request, 'share.html')

def thanks(request):
    return render(request, 'thanks.html')

def tips(request):
    return render(request, 'tips.html')
