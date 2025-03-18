import requests
import os
from dotenv import load_dotenv



load_dotenv()
spotify_api_key = os.environ['SPOTIFY_API_KEY']


# Spotify API URL is called using Rapid API
URL = "https://spotify23.p.rapidapi.com/search/"
API_KEY = spotify_api_key
# querystring is passed to spotify API
# query is the string we search for
def fetch_songs(emotion, singer=None):

    query = f"geners={emotion}"
    if singer:
        query+=f"artist={singer}"
    querystring = {"q": f"{query}", "type": "multi",
                "offset": "0", "limit": "50",
                "numberOfTopResults": "10"}
    # headers contain the API key and API host
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }
    # we use the requests library to sent a HTTP
    # GET request to the specified URL
    response = requests.get(URL, headers=headers,
                            params=querystring)

   
    songs = []
    data = response.json()['tracks']['items']
    # Our response has 10 results, we list
    # # them down using for loop
    for i in range(10):
        # data = 
        song, album = data[i]['data']['name'],  data[i]['data']['albumOfTrack']['name']
        print(f"song name: {song} \nalbum name: {album} \n")
        songs.append([song, album])
    
    return songs

# print(fetch_songs('angry', 'karan aujla'))