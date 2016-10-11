from django.contrib import admin
from .models import Album, Song

admin.site.register(Album, admin_class=None)
admin.site.register(Song, admin_class=None)
