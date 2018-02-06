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
        positives.append("You can break ice with your smile!")
    if (performance.speech_rate == 3 or performance.speech_rate == 4):
        positives.append("You speak at an effective pace!")
    if (performance.emotion > 3):
        positives.append("You can engage the audience with your enthusiasm!")
    if (performance.filler_words > 3):
        positives.append("No, or very few, fillers!")
    if (performance.eye_contact == 1):
        positives.append("You engage the audience with appropriate eye contact!")
    if (performance.nervousness > 3):
        positives.append("You are confident and calm and have a reassuring impact on your audience!")
    if (performance.pause > 3):
        positives.append("You speak with a wonderful rhythm that is comfortable to listen to!")
    if (performance.clearness > 3):
        positives.append("You can clearly deliver your thoughts with masterful articulation.")
    if (len(positives) > 3):
        shuffle(positives)
        return positives[0:3]
    return positives

def get_top_negatives(performance_key):
    negatives = []
    performance = Performance.objects.get(key=performance_key)
    if (performance.smile < 3):
        negatives.append("When you smile at your audience, they will smile back.  You will feel more comfortable and the audience will perceive you as confident. So let’s wear that warm smile on your face!")
    if (performance.speech_rate < 3):
        negatives.append("You speak too slow. Try adjust your speech rate to 120-150 words per minute!")
    if (performance.speech_rate > 4):
        negatives.append("You speak too fast. Try adjust your speech rate to 120-150 words per minute!")
    if (performance.emotion < 3):
        negatives.append("Try varying your emotional tone a bit and you’ll connect with your audience in the deepest way possible!")
    if (performance.filler_words < 3):
        negatives.append("Get comfortable with brief pauses and you will have fewer fillers!")
    if (performance.eye_contact == 0):
        negatives.append("Here’s a trick to make good eye contact: briefly look INTO the eyes, instead of look AT.")
    if (performance.nervousness < 3):
        negatives.append("Remember you’re the owner of your thoughts! And you are more charming when you’re calm!  Slight changes to your body when you are about to speak are normal and helpful when channeled into your delivery.")
    if (performance.pause < 3):
        negatives.append("Use pauses and vocal stress to emphasize key points – But not too much.")
    if (performance.clearness < 3):
        negatives.append("Make sure you pronounce words clearly at a moderate pace.")
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
