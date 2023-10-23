from dependency_injector.wiring import Provide, inject

from .containers import Container
from .dispatcher import Dispatcher


@inject
def main(dispatcher: Dispatcher = Provide[Container.dispatcher]) -> None:
    dispatcher.run()


if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    main()
