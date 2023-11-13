from bs4 import BeautifulSoup
import requests, spotipy
from spotipy.oauth2 import SpotifyOAuth

# from google import generativeai as palm
# import google

# TODO: Use Spotify to create a playlist based on these songs

CLIENT_ID = '320c531fc51b4c8f8b8278ff1c9a74bb'
CLIENT_SECRET = '9b5094c57cf64a629d3b11c5a1b72c7c'

user_defined_date = input("Specify a date in the following format (YYYY-MM-DD): ")

# ------------------ Get Top 100 Songs of user_defined_date ------------------ #
request_response = requests.get(url= f'https://www.billboard.com/charts/hot-100/{user_defined_date}/')
request_response.raise_for_status()
response_markup = request_response.content

soup = BeautifulSoup(markup= response_markup, features="html.parser")
elems = soup.select(selector= f'div.o-chart-results-list-row-container')



song_data = [{elem.select_one(selector= '#title-of-a-story').string.strip(): elem.select_one(selector= 'span.c-label.a-no-trucate.a-font-primary-s.lrv-u-font-size-14\@mobile-max.u-line-height-normal\@mobile-max.u-letter-spacing-0021.lrv-u-display-block.a-truncate-ellipsis-2line.u-max-width-330.u-max-width-230\@tablet-only').string.strip()} for elem in elems] # Song as key and value as artist for efficiency's sake
print(song_data[0])


# ---------------------------------- Spotify --------------------------------- #
REDIRECT_URI = 'http://example.com'
SCOPE = 'playlist-modify-public'
playlist_id = '4hRoihtBsU3Rzhc8bXuut7'

sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)

auth_url = sp_oauth.get_authorize_url()
print("Please authorize the application by visiting this URL:", auth_url)

response = input("Enter the URL you were redirected to after authorization: ")
code = sp_oauth.parse_response_code(response)

token_info = sp_oauth.get_access_token(code)
access_token = token_info['access_token']

spotify = spotipy.Spotify(auth=access_token)


for song in song_data:
    title = tuple(song.items())[0][0]
    artist = tuple(song.items())[0][1]
    search_and_get_song_uri(spotify, title, artist)
    break



def search_and_get_song_uri(spotify, title, artist):
    results = spotify.search(q= f"{title} {artist}", type= "track")
    print(results)


# --------------------------- Google Generative AI --------------------------- #
# PALM_KEY = 'AIzaSyCzeG9tUGbeeODMYCvrY9btm8UQupprjb8'

# user_input = input('Input: ')

# palm.configure(api_key= PALM_KEY)
# PaLMs_reply = palm.chat(prompt= [user_input])
# print(palm.annotations)

# print(PaLMs_reply.last)





