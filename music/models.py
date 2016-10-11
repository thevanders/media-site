from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=256)
    #artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=500)
    album_cover = models.CharField(max_length=1000)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.album_title + " - Artist: " + self.artist

class Song(models.Model):
    song_title = models.CharField(max_length=250)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)

    def __str__(self):
        return self.song_title + " - Album: " + self.album.album_title + " - Artist: " + self.album.artist

#class Artist(models.Model):
#    artist_name = models.Charfield(max_length=256)
#    artist_bio = models.Charfield(max_length=10000)
#    artist_pic = models.Charfield(max_length=1000)

def create_album():
    artist_name = input("Artist name:")
    albums = input("Albums seperated by |")
    genre_name = input("Genre:")
    album_list = [x for x in albums.split("|")]
    for album in range(len(album_list)):
        a = Album(artist=artist_name, album_title=album_list[album],genre=genre_name)
        a.save()
