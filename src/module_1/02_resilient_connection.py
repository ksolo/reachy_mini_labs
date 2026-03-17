"""
Create a resilient connection, one that if it fails will attempt
to retry with exponential backoff
"""
from typing import Literal, Optional

from reachy_mini import ReachyMini


class ResilientReachyMini():

    def __init__(
            self,
            robot_name: str = 'reachy_mini',
            host: str = 'reachy-mini.local',
            port: int = 8000,
            connection_mode: Literal['auto', 'localhost_only', 'network'] = 'auto',
            spawn_daemon: bool = False,
            use_sim: bool = False,
            timeout: float = 5.0,
            automatic_body_yaw: bool = True,
            log_level: str = 'INFO',
            media_backend: str = 'default',
            localhost_only: Optional[bool] = None,
    ):
        self._reachy_mini = ReachyMini(
            robot_name=robot_name,
            host=host,
            port=port,
            connection_mode=connection_mode,
            spawn_daemon=spawn_daemon,
            use_sim=use_sim,
            timeout=timeout,
            automatic_body_yaw=automatic_body_yaw,
            log_level=log_level,
            media_backend=media_backend,
            localhost_only=localhost_only
        )


    def __del__(self):
        if hasattr(self._reachy_mini, "client"):
            self._reachy_mini.client.disconnect()
    
    def __enter__(self) -> "ResilientReachyMini":
        return self
    
    def __exit__(self, exc_type, exc, tb):
       self._reachy_mini.media_manager.close()
       self._reachy_mini.client.disconnect() 
