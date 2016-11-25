from django.shortcuts import render
from .models import Photo
from .forms import PhotoForm

# Create your views here.
def gallery(request):
    photos = Photo.objects.all()
    return  render(request, "gallery/index.html", {"photos": photos})

def upload(request):
    return render(request, "gallery/upload.html")