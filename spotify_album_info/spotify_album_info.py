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
        print(access_token)


get_access_token()
