#from django.http import Http404
#from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Album, Song
from django.shortcuts import render

def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {"all_albums": all_albums})

def detail(request, album_id):
    #try:
    #    album = Album.objects.get(id=album_id)
    #except Album.DoesNotExist:
    #    raise Http404("Woops, this album doesn't exist")
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'music/detail.html', {"album": album})
