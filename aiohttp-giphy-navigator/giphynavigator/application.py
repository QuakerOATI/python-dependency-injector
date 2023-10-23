from aiohttp import web

from .containers import Container
from . import handlers


def create_app() -> web.Application:
    container = Container()

    app = web.Application()
    app.container = container
    app.add_routes(
        [
            web.get("/", handlers.index),
        ]
    )
    return app


if __name__ == "__main__":
    app = create_app()
    web.run_app(app)
