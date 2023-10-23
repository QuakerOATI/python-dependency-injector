from dependency_injector import containers, providers

from . import giphy


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=["config.yaml"])

    giphy_client = providers.Factory(
        giphy.GiphyClient,
        api_key=config.giphy.api_key,
        timeout=config.giphy.request_timeout,
    )
