import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinelevel.settings')
django.setup()

from movies.models import Level

levels = [
    {"name": "Niveau 1", "title": "Spectateur Novice 🎬", "min_movies_watched": 1, "description": "Vous avez trouvé le bouton play. Continuez, ce n'est que le début !"},
    {"name": "Niveau 2", "title": "Cinéphile Aspirant 🍿", "min_movies_watched": 5, "description": "Vous commencez à voir des génériques de fin. C'est prometteur !"},
    {"name": "Niveau 3", "title": "Enthousiaste de Cinéma 🎥", "min_movies_watched": 10, "description": "Votre passion pour le grand écran grandit. Popcorn obligatoire !"},
    {"name": "Niveau 4", "title": "Aficionado du Film 🎞️", "min_movies_watched": 15, "description": "Vous connaissez maintenant les répliques par cœur. Encore 35 films et on vous offre une réplique !"},
    {"name": "Niveau 5", "title": "Connaisseur de Cinéma 📽️", "min_movies_watched": 20, "description": "Vous êtes presque un critique. Ne vous arrêtez pas là !"},
    {"name": "Niveau 6", "title": "Critique Amateur 📝", "min_movies_watched": 25, "description": "Vous commencez à voir les films d'un autre œil. Est-ce que vous sentez l'Oscar ?"},
    {"name": "Niveau 7", "title": "Cinéphile Dévoué 🎟️", "min_movies_watched": 30, "description": "Vous regardez des films plus vite que votre ombre. Clint Eastwood serait fier !"},
    {"name": "Niveau 8", "title": "Analyste de Films 🧐", "min_movies_watched": 35, "description": "Vous pouvez désormais discuter des subtilités de Kubrick sans problème."},
    {"name": "Niveau 9", "title": "Expert en Cinéma 🎬", "min_movies_watched": 40, "description": "Votre avis commence à peser dans le monde du cinéma. Scorsese vous écoute."},
    {"name": "Niveau 10", "title": "Maître du Cinéma 🎥", "min_movies_watched": 45, "description": "Vous êtes devenu une référence cinématographique. Bravo, maître Yoda du cinéma !"},
    {"name": "Niveau 11", "title": "Cinémathécaire 📚", "min_movies_watched": 50, "description": "Votre collection ferait pâlir la Bibliothèque du Congrès."},
    {"name": "Niveau 12", "title": "Historien du Cinéma 🕰️", "min_movies_watched": 55, "description": "Vous avez tout vu, du noir et blanc au 3D. Chapeau bas !"},
    {"name": "Niveau 13", "title": "Savant du Cinéma 📖", "min_movies_watched": 60, "description": "Votre savoir en matière de cinéma est digne d'une encyclopédie."},
    {"name": "Niveau 14", "title": "Erudit du Cinéma 🎓", "min_movies_watched": 65, "description": "Vous comprenez les films dans toutes leurs dimensions. Nolan vous doit beaucoup !"},
    {"name": "Niveau 15", "title": "Philosophe du Cinéma 🧠", "min_movies_watched": 70, "description": "Vos discussions sur le cinéma ressemblent à des dissertations philosophiques."},
    {"name": "Niveau 16", "title": "Cinématographe 🎥", "min_movies_watched": 75, "description": "Vous êtes prêt à faire votre propre film. Hitchcock peut trembler !"},
    {"name": "Niveau 17", "title": "Artiste du Cinéma 🎨", "min_movies_watched": 80, "description": "Vous voyez le cinéma comme une forme d'art pure. Bravo, artiste !"},
    {"name": "Niveau 18", "title": "Poète du Cinéma ✒️", "min_movies_watched": 85, "description": "Vos interprétations sont poétiques. Fellini applaudit !"},
    {"name": "Niveau 19", "title": "Gourou du Cinéma 🧘‍♂️", "min_movies_watched": 90, "description": "Votre sagesse en matière de cinéma est recherchée. Tarantino vous suit !"},
    {"name": "Niveau 20", "title": "Légende du Cinéma 🌟", "min_movies_watched": 100, "description": "Vous êtes une légende vivante du cinéma. Spielberg vous envie !"}
]

Level.objects.all().delete()
for level in levels:
    Level.objects.create(**level)

