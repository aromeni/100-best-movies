from bs4 import BeautifulSoup
import requests

# Define the URL for the website
url = "https://www.empireonline.com/movies/features/best-movies-2/"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Request successful!")
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
    exit()

# Parse the HTML content using BeautifulSoup
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# Find all movie titles (stored in <h3> tags with a specific class)
all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

# Extract the text from each title tag and reverse the list to get the correct order
movie_titles = [movie.getText() for movie in all_movies][::-1]

# Save the movie titles to a text file
with open("movies.txt", mode="w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")
        print(f"Saved: {movie}")

print("Movies have been successfully saved to 'movies.txt'")
