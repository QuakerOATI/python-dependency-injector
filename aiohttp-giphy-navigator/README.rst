Giphy: aiohttp client
=====================

Useful Ideas
------------

- Config is imported from config.yaml, but additional config information from env variables is added to the container after its instantiation
- Automatically wire container by using the wiring_config property of the DeclarativeContainer class
- :code:`Handler` <- :code:`Client` -> :code:`Service` dependency decomposition
- Pattern for cleaning up containers in pytest fixtures
