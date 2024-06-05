from .player_state import PlayerState
from .video_state import VideoState
import json

class Parser(object):
    player_state: PlayerState = None
    video_state: str = None

    def __init__(self, data) -> None:
        self.player_state = PlayerState(data.get("player", {}))
        self.video_state = VideoState(data.get("video", {}))