import requests
import os

from django.http import HttpResponse, HttpResponseServerError, Http404, JsonResponse
from django.forms.models import model_to_dict

from .models import Performance
from .ml_grader import ML_grade


# Create your views here.

def html(text):
    return "<html><body>%s</body></html>" % text

def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    if len(url) == 0:
        return False
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

def upload(request):
    download_link = request.GET.get('url', '')
    if not is_downloadable(download_link):
        return HttpResponseServerError(html("Url %s is not downloadable:" % download_link))
    r = requests.get(download_link, allow_redirects=True)
    filename = download_link.split("/")[-1]
    fullpath = os.getcwd() + '/media/videos/' + filename
    performance_key = filename.split(".")[0]
    if Performance.objects.filter(key=performance_key).exists():
        return HttpResponseServerError(html("File %s already exists!" % performance_key))
    open(fullpath, 'wb').write(r.content)
    result = ML_grade(fullpath, len(fullpath), 0)
    performance = Performance(
        key=performance_key,
        smile=result[1],
        speech_rate=result[2],
        emotion=result[3],
        filler_words=result[4],
        eye_contact=result[5],
        nervousness=result[6],
        pause=result[7],
        clearness=result[8])
    performance.save()
    return HttpResponse(html("Upload succeed!"))

def data(request):
    key = request.GET.get('key', '')
    if not Performance.objects.filter(key=key).exists():
        raise Http404("Video does not exist!") 
    performance = Performance.objects.get(key=key)
    return JsonResponse(model_to_dict(performance), safe=False)
    
