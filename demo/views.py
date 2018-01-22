from random import shuffle

from django.shortcuts import render
from django.contrib import admin
from django.http import Http404

from .models import Performance

# Create your views here.

def get_top_positives(performance_key):
    positives = []
    performance = Performance.objects.get(key=performance_key)
    if (performance.smile > 3):
        positives.append("I like your smile!")
    if (performance.speech_rate == 3 or performance.speech_rate == 4):
        positives.append("Greate speech pace!")
    if (performance.emotion > 3):
        positives.append("You are enthusiastic!")
    if (performance.clearness > 3):
        positives.append("Awesome spoken English!")
    if (len(positives) > 3):
        shuffle(positives)
        return positives[0:3]
    return positives

def get_top_negatives(performance_key):
    negatives = []
    performance = Performance.objects.get(key=performance_key)
    if (performance.smile < 3):
        negatives.append("You may have more smiles!")
    if (performance.speech_rate < 3):
        negatives.append("You speak too slow!")
    if (performance.speech_rate > 4):
        negatives.append("You speak too fast!")
    if (performance.emotion < 3):
        negatives.append("Be more enthusiastic!")
    if (performance.filler_words < 3):
        negatives.append("You have too many filler words!")
    if (performance.eye_contact == 0):
        negatives.append("Talking with eye contact is important!")
    if (performance.nervousness < 3):
        negatives.append("Don't be nervous!")
    if (performance.pause < 3):
        negatives.append("You paused too much!")
    if (performance.clearness < 3):
        negatives.append("Practice more on spoken English!")
    if (len(negatives) > 3):
        shuffle(negatives)
        return negatives[0:3]
    return negatives

def get_percentage(performance_key):
    performance = Performance.objects.get(key=performance_key)
    percentage = performance.smile + performance.emotion + performance.filler_words \
                 + performance.eye_contact + performance.nervousness + performance.pause \
                 + performance.clearness
    return int(percentage * 100.0 / 31.0);

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-you.html')

def check(request, performance_key):
    percentage = get_percentage(performance_key)
    return render(request, 'check.html', {'performance_key': performance_key, 'percentage': percentage})

def contact(request):
    return render(request, 'contact.html')

def factors(request, performance_key):
    positives = get_top_positives(performance_key)
    return render(request, 'factors.html', {'positives': positives, 'performance_key': performance_key})

def share(request):
    return render(request, 'share.html')

def thanks(request):
    return render(request, 'thanks.html')

def tips(request, performance_key):
    negatives = get_top_negatives(performance_key)
    return render(request, 'tips.html', {'negatives': negatives})

class PerformanceAdmin(admin.ModelAdmin):
    fields = ('key', 'smile', 'speech_rate', 'emotion', 'filler_words', 'eye_contact', 'nervousness', 'pause', 'clearness', 'createdOn')
