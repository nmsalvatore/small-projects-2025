from album import Album
from spotify import FakeSpotifyClient


fake_client = FakeSpotifyClient("fake_access_token")
album = Album.from_id("71On7h3S7yH5D0Td6YNw1t", fake_client)


def test_artist_name():
    assert album.artist == ["Johnny Blue Skies", "Sturgill Simpson"]


def test_album_name():
    assert album.name == "Passage Du Desir"


def test_album_release_year():
    assert album.release_year == "2024"
