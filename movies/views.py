from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from .models import WatchedMovie, WatchlistMovie, Movie
import pandas as pd
import os

@login_required
def home(request):
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'senscritique_top_250.csv')
    print(f"Loading CSV file from: {file_path}")
    try:
        movies = pd.read_csv(file_path).to_dict(orient='records')
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        movies = []
    return render(request, 'movies/home.html', {'movies': movies})

@login_required
def levels(request):
    watched_movies = WatchedMovie.objects.filter(user=request.user)
    return render(request, 'movies/levels.html', {'watched_movies': watched_movies})


@login_required
def watchlist(request):
    watchlist_movies = WatchlistMovie.objects.filter(user=request.user)
    return render(request, 'movies/watchlist.html', {'watchlist_movies': watchlist_movies})



@login_required
def update_movie_status(request):
    if request.method == "POST":
        title = request.POST.get('title')
        year = request.POST.get('year')
        duration = request.POST.get('duration')
        genre = request.POST.get('genre')
        image = request.POST.get('image')
        action = request.POST.get('action')
        
        movie, created = Movie.objects.get_or_create(
            title=title, 
            year=year, 
            duration=duration, 
            genre=genre, 
            image=image
        )

        if action == "watched":
            WatchedMovie.objects.get_or_create(user=request.user, movie=movie)
        elif action == "watchlist":
            WatchlistMovie.objects.get_or_create(user=request.user, movie=movie)

    return redirect('home')

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


