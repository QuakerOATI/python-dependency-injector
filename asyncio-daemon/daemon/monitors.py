import logging
from abc import ABC, abstractmethod


class Monitor(ABC):
    """Base class for Monitors."""

    def __init__(self, check_every: int) -> None:
        self.check_every = check_every
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    async def check(self) -> None:
        ...
