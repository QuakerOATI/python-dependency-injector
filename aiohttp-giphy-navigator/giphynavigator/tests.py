from unittest import mock

import pytest

from giphynavigator.application import create_app
from giphynavigator.giphy import GiphyClient


@pytest.fixture
def app():
    app = create_app()
    yield app
    app.container.unwire()


@pytest.fixture
def client(app, aiohttp_client, event_loop):
    return event_loop.run_until_complete(aiohttp_client(app))


@pytest.mark.asyncio
async def test_index(client, app):
    giphy_client_mock = mock.AsyncMock(spec=GiphyClient)
    giphy_client_mock.search.return_value = {
        "data": [
            {"url": "https://giphy.com/some-gif.gif"},
            {"url": "https://giphy.com/some-other-gif.gif"},
        ],
    }

    with app.container.giphy_client.override(giphy_client_mock):
        response = await client.get(
            "/",
            params={
                "query": "test",
                "limit": 10,
            },
        )

    assert response.status == 200
    data = await response.json()
    assert data == {
        "query": "test",
        "limit": 10,
        "gifs": [
            {"url": "https://giphy.com/some-gif.gif"},
            {"url": "https://giphy.com/some-other-gif.gif"},
        ],
    }


@pytest.mark.asyncio
async def test_index_no_data(client, app):
    giphy_client_mock = mock.AsyncMock(spec=GiphyClient)
    giphy_client_mock.search.return_value = {
        "data": [],
    }

    with app.container.giphy_client.override(giphy_client_mock):
        response = await client.get("/")

    assert response.status == 200
    data = await response.json()
    assert data["gifs"] == []


@pytest.mark.asyncio
async def test_index_default_params(client, app):
    giphy_client_mock = mock.AsyncMock(spec=GiphyClient)
    giphy_client_mock.search.return_value = {
        "data": [],
    }

    with app.container.giphy_client.override(giphy_client_mock):
        response = await client.get("/")
    assert response.status == 200
    data = await response.json()
    assert data["query"] == app.container.config.default.query()
    assert data["limit"] == app.container.config.default.limit()
