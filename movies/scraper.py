import requests
from bs4 import BeautifulSoup

def scrape_movies():
    url = "https://www.imdb.com/list/ls055386972/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = soup.find_all('div', class_='lister-item mode-detail')

    movie_list = []

    for movie in movies:
        name = movie.h3.a.text
        year = movie.find('span', class_='lister-item-year').text
        rating = movie.find('span', class_='ipl-rating-star__rating')
        rating = rating.text if rating else 'N/A'
        image = movie.find('img')['src']

        movie_list.append({
            'name': name,
            'year': year,
            'rating': rating,
            'image': image
        })

    return movie_list
