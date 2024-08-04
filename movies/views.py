from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.core import serializers
from django.http import JsonResponse
from .models import WatchedMovie, Movie, Level
from collections import Counter
import random
import json
import csv
import os


def landing(request):
    return render(request, 'movies/landing.html')

@login_required
def home(request):
    movies = []
    query = request.GET.get('query', '')

    csv_file_path = os.path.join('movies', 'data', 'senscritique_top_250.csv')
    
    watched_movies = WatchedMovie.objects.filter(user=request.user).values_list('movie__title', flat=True)
    
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                try:
                    movie = {
                        'title': row['Title'],
                        'year': row['Year'],
                        'duration': row['Duration'],
                        'genre': row['Genre'],
                        'image': row['Image'],
                        'watched': row['Title'] in watched_movies
                    }
                    if query.lower() in movie['title'].lower():
                        movies.append(movie)
                except KeyError as e:
                    print(f"Missing column in CSV: {e}")
    except FileNotFoundError:
        print(f"File {csv_file_path} not found.")
    
    context = {'movies': movies, 'query': query}
    return render(request, 'movies/home.html', context)

@login_required
def levels(request):
    watched_movies_count = WatchedMovie.objects.filter(user=request.user).count()
    user_level = Level.objects.filter(min_movies_watched__lte=watched_movies_count).order_by('-min_movies_watched').first()
    levels = Level.objects.all()

    # Calcul de la progression vers le prochain niveau
    next_level = Level.objects.filter(min_movies_watched__gt=watched_movies_count).order_by('min_movies_watched').first()
    if next_level:
        total_movies_needed = next_level.min_movies_watched
        movies_needed = total_movies_needed - watched_movies_count
        progress_percentage = (watched_movies_count / total_movies_needed) * 100
    else:
        progress_percentage = 100  # Si l'utilisateur est au niveau le plus élevé

    # Liste des niveaux débloqués
    unlocked_levels = Level.objects.filter(min_movies_watched__lte=watched_movies_count)

    context = {
        'user_level': user_level,
        'watched_movies_count': watched_movies_count,
        'levels': levels,
        'progress_percentage': progress_percentage,
        'unlocked_levels': unlocked_levels,
    }
    return render(request, 'movies/levels.html', context)

@login_required
def watchlist(request):
    watched_movies = WatchedMovie.objects.filter(user=request.user).select_related('movie')
    context = {'watched_movies': watched_movies}
    return render(request, 'movies/watchlist.html', context)

@login_required
def update_movie_status(request):
    if request.method == "POST":
        title = request.POST.get("title")
        year = request.POST.get("year")
        duration = request.POST.get("duration")
        genre = request.POST.get("genre")
        image = request.POST.get("image")
        
        movie, created = Movie.objects.get_or_create(
            title=title,
            year=year,
            duration=duration,
            genre=genre,
            image=image
        )
        
        watched_movie = WatchedMovie.objects.filter(user=request.user, movie=movie).first()
        
        if watched_movie:
            watched_movie.delete()
        else:
            WatchedMovie.objects.create(user=request.user, movie=movie)
        
        return redirect('home')

    return redirect('home')


@login_required
def recommend_movies(request):
    user = request.user
    watched_movies = WatchedMovie.objects.filter(user=user)
    watched_genres = [wm.movie.genre for wm in watched_movies]

    # Compter les genres les plus fréquents
    genre_counter = Counter(watched_genres)
    favorite_genres = [genre for genre, count in genre_counter.most_common()]

    # Recommander des films qui appartiennent aux genres préférés
    recommended_movies = Movie.objects.filter(genre__in=favorite_genres).exclude(watchedmovie__user=user)

    context = {
        'recommended_movies': recommended_movies,
        'favorite_genres': favorite_genres
    }
    return render(request, 'movies/recommendations.html', context)




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'movies/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'movies/login.html', {'form': form})
