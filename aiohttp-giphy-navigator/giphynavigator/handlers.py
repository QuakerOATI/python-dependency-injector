from aiohttp import web
from dependency_injector.wiring import Provide, inject
from typing import Any

from .services import SearchService
from .containers import Container


@inject
async def index(
    request: web.Request,
    search_service: SearchService = Provide[Container.search_service],
) -> Any:
    query = request.query.get("query", "Dependency Injector")
    limit = int(request.query.get("limit", 10))

    gifs = await search_service.search(query, limit)

    return web.json_response(
        {
            "query": query,
            "limit": limit,
            "gifs": gifs,
        },
    )
