import logging
import sys

from dependency_injector import containers, providers
from . import dispatcher, http


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=["config.yaml"])

    logging = providers.Resource(
        logging.basicConfig,
        stream=sys.stdout,
        level=config.log.level,
        format=config.log.format,
    )

    http_client = providers.Factory(http.HttpClient)

    dispatcher = providers.Factory(
        dispatcher.Dispatcher,
        monitors=providers.List(
            # TODO: Add monitors
        ),
    )
