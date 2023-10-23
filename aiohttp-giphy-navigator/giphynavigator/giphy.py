from aiohttp import ClientSession, ClientTimeout, ClientResponse
from typing import Any


class GiphyClient:
    """Minimal client for the giphy API."""

    API_URL = "https://api/giphy.com/v1"

    def __init__(self, api_key, timeout) -> None:
        self._api_key = api_key
        self._timeout = ClientTimeout(timeout)

    # TODO: Replace type annotation for return value
    async def search(self, query, limit) -> Any:
        """Search for gifs using giphy API and return results."""
        url = f"{self.API_URL}/gifs/search"
        params = {
            "q": query,
            "api_key": self._api_key,
            "limit": limit,
        }
        async with ClientSession(timeout=self._timeout) as session:
            async with session.get(url, params=params) as response:
                if response.status != 200:
                    response.raise_for_status()
                return await response.json()
