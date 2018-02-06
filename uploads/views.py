import os

from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from demo.models import Performance
from demo.ml_grader import ML_grade

from uploads.models import Document
from uploads.forms import DocumentForm


def home_(request):
    documents = Document.objects.all()
    return render(request, 'templates/home.html', { 'documents': documents })


def upload_simple(request):
    print("in upload\n")
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'uploads/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'uploads/upload.html')


def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            filename = form.save()
            uploaded_file_url = filename.description
        return render(request, 'uploads/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    else:
        form = DocumentForm()
    return render(request, 'uploads/upload.html', {
        'form': form
    })


def upload_demo(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            filename = form.save()
            fullpath = os.getcwd() + '/media/documents/' + filename.description
            performance_key = filename.description.split(".")[0]
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
        return redirect('/demo/check/' + performance_key)
    return redirect('/demo/about')
