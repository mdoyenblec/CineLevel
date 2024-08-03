from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    duration = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    image = models.URLField()

    def __str__(self):
        return self.title

class WatchedMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} watched {self.movie.title}"

class Level(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    min_movies_watched = models.IntegerField()
    description = models.TextField(default='Aucune description')

    def __str__(self):
        return self.name
