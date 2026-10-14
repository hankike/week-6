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
