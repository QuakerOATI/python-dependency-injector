from aiohttp import web


async def index(request: web.Request) -> web.Response:
    query = request.query.get("query", "Dependency Injector")
    limit = int(request.query.get("limit", 10))

    gifs = []

    return web.json_response(
        {
            "query": query,
            "limit": limit,
            "gifs": gifs,
        },
    )
