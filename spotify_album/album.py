from typing import Optional

from auth import get_access_token
from spotify import SpotifyClient, SpotifyAlbumResponse


class Album:
    """Parse and store album data"""

    def __init__(self, album_data: SpotifyAlbumResponse, id: str):
        self.id = id
        self.artist = [artist["name"] for artist in album_data["artists"]]
        self.name = album_data["name"]
        self.release_year = album_data["release_date"].split("-")[0]

    @classmethod
    def from_id(cls, id: str, client: SpotifyClient) -> "Album":
        album_data = client.get_album(id)
        return cls(album_data, id)


if __name__ == "__main__":
    access_token: Optional[str] = get_access_token()

    if not access_token:
        raise ValueError("Could not retrieve Spotify access token")

    client = SpotifyClient(access_token)
    album = Album.from_id("71On7h3S7yH5D0Td6YNw1t", client)

    print({
        "artist": album.artist,
        "name": album.name,
        "release_year": album.release_year,
    })
