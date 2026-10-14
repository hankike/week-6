# your code here ...

import requests


class Genius:
    def __init__(self, access_token):
        """Initialize the Genius API Client."""
        self.access_token = access_token
        self.base_url = "https://api.genius.com"

    def search(self, search_term):
        """Search the Genius API for a given term."""
        url = f"{self.base_url}/search"

        params = {
            "q": search_term,
            "access_token": self.access_token
        }

        response = requests.get(url, params=params)
        response.raise_for_status()

        return response.json()

    def get_artist(self, search_term):
        # Here is how we search for the artist
        search_data = self.search(search_term)

        # Here we extract the "primary" artist ID from the first "hit"
        artist_id = search_data["response"]["hits"][0]["result"]["primary_artist"]["id"]

        # Now we request artist info
        url = f"{self.base_url}/artists/{artist_id}"

        params = {
            "access_token": self.access_token
        }

        response = requests.get(url, params=params)
        response.raise_for_status()

        return response.json()
