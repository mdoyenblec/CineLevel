from django.contrib import admin
from .models import Movie, WatchedMovie

admin.site.register(Movie)
admin.site.register(WatchedMovie)
