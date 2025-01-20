import os
from typing import Optional

import requests
from dotenv import load_dotenv


load_dotenv()


def get_access_token() -> str:
    """Retrieve Spotify API access token """

    client_id: Optional[str] = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret: Optional[str] = os.getenv("SPOTIFY_CLIENT_SECRET")

    if not client_id:
        raise ValueError("Missing environment variable SPOTIFY_CLIENT_ID")
    if not client_secret:
        raise ValueError("Missing environment variable SPOTIFY_CLIENT_SECRET")

    response = requests.post(
        "https://accounts.spotify.com/api/token",
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret),
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    response.raise_for_status()
    return response.json()["access_token"]
