import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def scrape_senscritique_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    movies = []
    movie_elements = soup.find_all('div', class_='sc-40dee1ba-0 kaIbyk')
    
    for movie in movie_elements:
        try:
            title_tag = movie.find('h3', class_='sc-e6f263fc-0 cTitej')
            title_text = title_tag.text.strip()
            title_french = title_text.split(' (')[0].strip() if ' (' in title_text else title_text
            year = title_text.split(' (')[1].replace(')', '') if ' (' in title_text else 'N/A'
        except:
            title_french = 'N/A'
            year = 'N/A'
        
        try:
            info_tag = movie.find('p', {'data-testid': 'other-infos'})
            duration = info_tag.find('span', {'data-testid': 'duration'}).text.strip() if info_tag.find('span', {'data-testid': 'duration'}) else 'N/A'
            genre = info_tag.find('span', {'data-testid': 'genres'}).text.strip() if info_tag.find('span', {'data-testid': 'genres'}) else 'N/A'
        except:
            duration = 'N/A'
            genre = 'N/A'
        
        try:
            image_tags = movie.find_all('img', {'data-testid': 'poster-img'})
            image_url = 'N/A'
            for img in image_tags:
                if img['src'].startswith('https://'):
                    image_url = img['src']
                    break
        except:
            image_url = 'N/A'
        
        movies.append({
            'Title': title_french,
            'Year': year,
            'Duration': duration,
            'Genre': genre,
            'Image': image_url
        })
    
    return movies

def scrape_all_pages(base_url, num_pages):
    all_movies = []
    for page in range(1, num_pages + 1):
        url = f"{base_url}?page={page}"
        movies = scrape_senscritique_page(url)
        all_movies.extend(movies)
        print(f"Scraped page {page}/{num_pages}")
    return all_movies

def save_to_csv(movies):
    directory = os.path.join(os.path.dirname(__file__), 'data')
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    file_path = os.path.join(directory, 'senscritique_top_250.csv')
    df = pd.DataFrame(movies)
    df.insert(0, 'Rank', range(1, len(df) + 1))
    df.to_csv(file_path, index=False)
    print(f"Saved to {file_path}")

if __name__ == "__main__":
    base_url = 'https://www.senscritique.com/liste/top_250_movies_the_ultimate_bucket_list_for_the_cineast/3422710'
    num_pages = 10  # Vous pouvez ajuster le nombre de pages à scraper
    all_movies = scrape_all_pages(base_url, num_pages)
    save_to_csv(all_movies)
