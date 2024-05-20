# django_app/views.py
from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def landing_page(request):
    if request.user.is_authenticated:
        return render(request, 'upload.html')
    return render(request, 'landing_page.html')

@login_required
def upload(request):
    context = {'backend_form': PhotoForm()}
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            if instance is None:
                messages.error(request, "Your image didn't pass moderation. Please try uploading another one.")
            else: 
                return redirect('display')
    return render(request, 'upload.html', context)

@login_required
def display(request):
    photos = Photo.objects.all()
    return render(request, 'display.html', {'photos': photos})