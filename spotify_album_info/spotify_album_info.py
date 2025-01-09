import os

import requests
from dotenv import load_dotenv


load_dotenv()


def get_access_token():
    """Retrieve Spotify API access token """

    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")

    response = requests.post(
        "https://accounts.spotify.com/api/token",
        data={"grant_type": "client_credentials"},
        auth=(CLIENT_ID, CLIENT_SECRET),
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    if response.ok:
        access_token = response.json()["access_token"]
        return access_token


def get_album_details(id):
    """Fetch album details from Spotify API"""

    response = requests.get(
        f"https://api.spotify.com/v1/albums/{id}",
        headers={"Authorization": f"Bearer {get_access_token()}"}
    )

    body = response.json()

    print({
        "artist_name": body["artists"][0]["name"],
        "title": body["name"],
        "release_date": body["release_date"],
        "img_src": body["images"][1]["url"]
    })


get_album_details("71On7h3S7yH5D0Td6YNw1t")
