## Setting up
import requests
import dotenv
import os
import shutil
from time import sleep

dotenv.load_dotenv()

BASE_URL = "https://ws.audioscrobbler.com/2.0"
API_KEY = os.getenv("LASTFM_APIKEY")
LASTFM_USER = os.getenv("LASTFM_USER")

headers = {
    'user_agent': "lastfm-currentsong-testing"
}

while True:
    response = requests.get(BASE_URL + f"?method=user.getrecenttracks&user={LASTFM_USER}&api_key={API_KEY}&format=json", headers=headers)

    response_json = response.json()

    usable_info = response_json["recenttracks"]["track"][0]

    # actually using the stuff
    artist = usable_info["artist"]["#text"]
    track = usable_info["name"]
    image_url = usable_info["image"][3]["#text"]

    image = requests.get(image_url, stream = True)

    with open("currentsong.txt","w", encoding="utf-8") as textfile:
        textfile.write(artist + " - " + track)

    os.system("cls||clear")
    print(artist + " - " + track)

    if image.status_code == 200:
        with open("image.png",'wb') as imagefile:
            shutil.copyfileobj(image.raw, imagefile)
    else:
        print("Couldn't retrieve image")
    
    sleep(5)