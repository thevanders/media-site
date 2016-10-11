from django.http import Http404
from django.http import HttpResponse
from .models import Album, Song
from django.shortcuts import render

def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {"all_albums": all_albums})

def detail(request, album_id):
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Woops, this album doesn't exist")
    return render(request, 'music/detail.html', {"album": album})
