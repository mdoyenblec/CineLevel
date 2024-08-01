from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import WatchedMovie

@receiver(post_save, sender=WatchedMovie)
def movie_watched(sender, instance, created, **kwargs):
    if created:
        print(f"{instance.user.username} watched {instance.movie.title}")

@receiver(post_delete, sender=WatchedMovie)
def movie_unwatched(sender, instance, **kwargs):
    print(f"{instance.user.username} removed {instance.movie.title} from watched list")
