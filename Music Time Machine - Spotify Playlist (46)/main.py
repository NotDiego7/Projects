import requests, os
from google import generativeai as palm
from bs4 import BeautifulSoup
import google

# TODO: Use BeautifulSoup to scrape the top 100 songs of a selected date
# TODO: Then extract all of the song titles
# TODO: Use Spotify to create a playlist based on these songs

# user_defined_date = input("Specify a date in the following format (YYYY-MM-DD): ")

# request_response = requests.get(url= f'https://www.billboard.com/charts/hot-100/{user_defined_date}/')
# request_response.raise_for_status()
# response_markup = request_response.content

# soup = BeautifulSoup(markup= response_markup, features="html.parser")
# elems = soup.select(selector= f'div.o-chart-results-list-row-container')


# top_100_songs = [elem.select_one(selector= '#title-of-a-story').string.split() for elem in elems] # Should convert each elem in list to a hashmap with artist as key and song as value

# for i in top_100_songs:
#     print(i)

PALM_KEY = 'AIzaSyCzeG9tUGbeeODMYCvrY9btm8UQupprjb8'

user_input = input('Input: ')

palm.configure(api_key= PALM_KEY)
PaLMs_reply = palm.chat(prompt= [user_input])
print(palm.annotations)

print(PaLMs_reply.last)





