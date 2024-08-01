from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, signup, login_view, levels, watchlist, update_movie_status

urlpatterns = [
    path('', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('levels/', levels, name='levels'),
    path('watchlist/', watchlist, name='watchlist'),
    path('home/', home, name='home'),
    path('update_movie_status/', update_movie_status, name='update_movie_status'),
]
