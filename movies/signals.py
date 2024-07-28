from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import WatchedMovie, WatchlistMovie, Movie

@receiver(post_save, sender=WatchedMovie)
def add_to_watched(sender, instance, created, **kwargs):
    if created:
        WatchlistMovie.objects.filter(user=instance.user, movie=instance.movie).delete()

@receiver(post_save, sender=WatchlistMovie)
def add_to_watchlist(sender, instance, created, **kwargs):
    if created:
        WatchedMovie.objects.filter(user=instance.user, movie=instance.movie).delete()
