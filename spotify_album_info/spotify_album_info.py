import requests
from bs4 import BeautifulSoup


class Album:
    """Store album info from a Spotify URL"""

    def __init__(self, url):
        self.url = url
        self._info = None

    def _fetch_album_info(self):
        """Fetch and store album info"""
        if self._info is None:
            soup = self._get_soup()
            description = self._get_description(soup)

            # Fetch album properties
            artist = description.split('\u00B7')[0].strip()
            year = description.split('\u00B7')[2].strip()
            title = soup.css.select_one("meta[property='og:title']")["content"]
            cover_src = soup.css.select_one("img[loading='eager']")["src"]

            self._info = {
                "artist": artist,
                "title": title,
                "year": year,
                "cover_src": cover_src
            }
            return self._info

    def get_album_info(self):
        return self._fetch_album_info()

    def get_artist(self):
        return self._info["artist"]

    def get_cover_src(self):
        return self._info["cover_src"]

    def get_title(self):
        return self._info["title"]

    def get_year(self):
        return self._info["year"]

    def _get_description(self, soup):
        return soup.css.select_one("meta[property='og:description']")["content"]

    def _get_soup(self):
        r = requests.get(self.url)
        return BeautifulSoup(r.text, "html.parser")


album = Album("https://open.spotify.com/album/51CQQ3tQLRZlZJZ5jcpoGE?si=yNKelaznQVOLDnjRch54vA")
print(album.get_album_info())
