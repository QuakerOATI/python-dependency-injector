import asyncio
import logging
import signal
import time
from typing import List

from .monitors import Monitor


class Dispatcher:
    """Scheduler and task runner for Monitors."""

    def __init__(self, monitors: List[Monitor]) -> None:
        self._monitors = monitors
        self._monitor_tasks: List[asyncio.Task] = []
        self._logger = logging.getLogger(self.__class__.__name__)
        self._stopping = False

    def run(self) -> None:
        asyncio.run(self.start())

    async def start(self) -> None:
        self._logger.info("Starting...")
        for monitor in self._monitors:
            self._monitor_tasks.append(
                asyncio.create_task(self._run_monitor(monitor)),
            )

        asyncio.get_event_loop().add_signal_handler(signal.SIGTERM, self.stop)
        asyncio.get_event_loop().add_signal_handler(signal.SIGINT, self.stop)

        await asyncio.gather(*self._monitor_tasks, return_exceptions=True)

        self.stop()

    def stop(self) -> None:
        if self._stopping:
            return

        self._stopping = True
        self._logger.info("Stopping...")

        # QUESTION: Why zip with self._monitors if the monitor is not used?
        for task, monitor in zip(self._monitor_tasks, self._monitors):
            task.cancel()

        self._monitor_tasks.clear()
        self._logger.info("Shutdown successfully")

    @staticmethod
    async def _run_monitor(monitor: Monitor) -> None:
        def _until_next(last: float) -> float:
            duration = time.time() - last
            return monitor.check_every - duration

        while True:
            start = time.time()
            try:
                await monitor.check()
            except asyncio.CancelledError:
                break
            except Exception:
                monitor.logger.exception("Error executing monitor check")

            await asyncio.sleep(_until_next(last=start))
