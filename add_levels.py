import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinelevel.settings')
django.setup()

from movies.models import Level

levels = [
    {"name": "Niveau 1", "title": "Spectateur Novice", "min_movies_watched": 1},
    {"name": "Niveau 2", "title": "Cinéphile Aspirant", "min_movies_watched": 5},
    {"name": "Niveau 3", "title": "Enthousiaste de Cinéma", "min_movies_watched": 10},
    {"name": "Niveau 4", "title": "Aficionado du Film", "min_movies_watched": 15},
    {"name": "Niveau 5", "title": "Explorateur Cinématographique", "min_movies_watched": 20},
    {"name": "Niveau 6", "title": "Connaisseur d'Écran", "min_movies_watched": 25},
    {"name": "Niveau 7", "title": "Scribe de l'Écran Argenté", "min_movies_watched": 30},
    {"name": "Niveau 8", "title": "Passionné de Cinéma", "min_movies_watched": 35},
    {"name": "Niveau 9", "title": "Expert en Films", "min_movies_watched": 40},
    {"name": "Niveau 10", "title": "Savant du Cinéma", "min_movies_watched": 45},
    {"name": "Niveau 11", "title": "Sage de l'Écran", "min_movies_watched": 50},
    {"name": "Niveau 12", "title": "Érudit Cinématographique", "min_movies_watched": 55},
    {"name": "Niveau 13", "title": "Maître du Film", "min_movies_watched": 60},
    {"name": "Niveau 14", "title": "Fanatique de Cinéma", "min_movies_watched": 65},
    {"name": "Niveau 15", "title": "Guru de l'Écran", "min_movies_watched": 70},
    {"name": "Niveau 16", "title": "Luminaire Cinématographique", "min_movies_watched": 75},
    {"name": "Niveau 17", "title": "Virtuose du Film", "min_movies_watched": 80},
    {"name": "Niveau 18", "title": "Magnat du Cinéma", "min_movies_watched": 85},
    {"name": "Niveau 19", "title": "Icône du Film", "min_movies_watched": 90},
    {"name": "Niveau 20", "title": "Légende Cinématographique", "min_movies_watched": 100},
]

for level in levels:
    Level.objects.create(**level)
