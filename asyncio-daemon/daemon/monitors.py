import logging
import time
from typing import Dict, Any
from abc import ABC, abstractmethod

from .http import HttpClient


class Monitor(ABC):
    """Base class for Monitors."""

    def __init__(self, check_every: int) -> None:
        self.check_every = check_every
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    async def check(self) -> None:
        ...


class HttpMonitor(Monitor):
    def __init__(
        self,
        http_client: HttpClient,
        options: Dict[str, Any],
    ) -> None:
        self._client = http_client
        self._method = options.pop("method")
        self._url = options.pop("url")
        self._timeout = options.pop("timeout")
        super().__init__(check_every=options.pop("check_every"))

    async def check(self) -> None:
        start = time.time()

        response = await self._client.request(
            method=self._method,
            url=self._url,
            timeout=self._timeout,
        )

        end = time.time()
        duration = end - start

        self.logger.info(
            "Check:\n"
            "   %s %s\n"
            "   response code: %s\n"
            "   content length: %s\n"
            "   time elapsed: %s seconds\n",
            self._method,
            self._url,
            response.status,
            response.content_length,
            round(duration, 3),
        )
