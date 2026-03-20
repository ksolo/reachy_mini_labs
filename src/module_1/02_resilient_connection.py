"""
Create a resilient connection, one that if it fails will attempt
to retry with exponential backoff
"""
import logging
from typing import Literal, Optional, Callable

from reachy_mini import ReachyMini


logger = logging.getLogger("resilient-session")


class ResilientSession:
    def __init__(self, max_retries=10, backoff_base=1.0, backoff_max=30.0):
        self._mini = None
        self._max_retries = max_retries
        self._backoff_base = backoff_base
        self._backoff_max = backoff_max

    def _connect_with_retry(self):
        """Retry ReachyMini() with exponential backoff."""
        for attempt in range(self._max_retries):
            try:
                self._mini = ReachyMini()
                self._mini.__enter__()  # start the SDK session
                print(f"Connected on attempt {attempt + 1}")
                return
            except TimeoutError:
                delay = min(self._backoff_base * (2 ** attempt), self._backoff_max)
                print(f"Attempt {attempt + 1} failed, retrying in {delay:.1f}s...")
                time.sleep(delay)
        raise TimeoutError(f"Could not connect after {self._max_retries} attempts")

    def _cleanup_current(self):
        """Exit the current ReachyMini context, if any."""
        if self._mini:
            try:
                self._mini.__exit__(None, None, None)
            except Exception:
                pass  # best-effort cleanup
            self._mini = None

    def reconnect(self):
        """Tear down current connection, establish a new one."""
        print("Reconnecting...")
        self._cleanup_current()
        self._connect_with_retry()

    @property
    def mini(self):
        return self._mini

    # The outer context manager owns the SESSION lifetime,
    # not any single ReachyMini connection's lifetime.
    # reconnect() may destroy and recreate ReachyMini
    # instances multiple times within one 'with' block.
    def __enter__(self):
        self._connect_with_retry()
        return self

    def __exit__(self, *args):
        self._cleanup_current()
