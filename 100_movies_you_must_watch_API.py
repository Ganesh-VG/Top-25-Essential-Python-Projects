from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

movies_text = response.text

soup = BeautifulSoup(movies_text, "html.parser")

# print(soup.prettify())

text = soup.findAll(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")

title_text = [ti.getText() for ti in text]

title_text = title_text[::-1]

for title in title_text:
    with open("top_movies.txt", mode="a") as file:
        file.write(f"{title}\n")