import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response_text = response.text
movie_titles = []

soup = BeautifulSoup(response_text, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in movies]
movie_titles.reverse()

with open("top_movies.txt", "w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")
