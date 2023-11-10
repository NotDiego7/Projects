import requests
from bs4 import BeautifulSoup

# TODO: Use BeautifulSoup to scrape the top 100 songs of a selected date
# TODO: Then extract all of the song titles
# TODO: Use Spotify to create a playlist based on these songs

user_defined_date = input("Specify a date in the following format (YYYY-MM-DD): ")
requests.get(url= f'https://www.billboard.com/charts/hot-100/{user_defined_date}/')
BeautifulSoup(markup= "")