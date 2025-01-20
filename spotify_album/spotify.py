from typing import Literal, TypedDict

import requests


class SpotifyAlbumResponse(TypedDict):
    artists: list[dict]
    name: str
    release_date: str


class SpotifyClient:
    """A client for the Spotify API"""

    def __init__(self, access_token: str):
        self._access_token = access_token

    def get_album(self, id: str) -> SpotifyAlbumResponse:
        response = requests.get(
            f"https://api.spotify.com/v1/albums/{id}",
            headers={"Authorization": f"Bearer {self._access_token}"}
        )
        return response.json()


class FakeSpotifyClient(SpotifyClient):
    """A fake Spotify client"""

    def get_album(self, id: str) -> SpotifyAlbumResponse:
        return {
            "artists": [
                {"name": "Johnny Blue Skies"},
                {"name": "Sturgill Simpson"}
            ],
            "name": "Passage Du Desir",
            "release_date": "2024"
        }
