from .converters import state_converter, repeatMode_converter
from .queue import queueItem

class PlayerState(object):
    state: str = "Unknown"
    video_progress: float = 0
    volume: int = 0
    muted: bool = False
    adPlaying: bool = False
    queue: list[queueItem] = []
    auto_play: bool = False
    isGenerating: bool = False
    isInfinite: bool = False
    repeatMode: str = "Unknown"
    selectedItemIndex: int = 0

    def __init__(self, data) -> None:
        self.state = state_converter.get(data.get("trackState", -1), "Unknown")
        self.video_progress = data.get("videoProgress", 0.0)
        self.volume = data.get("volume", 0)
        self.muted = data.get("muted", False)
        self.adPlaying = data.get("adPlaying", False)
        self.auto_play = data.get("autoplay", False)
        self.queue = [queueItem(item) for item in data['queue']['items']]
        self.isGenerating = data.get("isGenerating", False)
        self.isInfinite = data.get("isInfinite", False)
        self.repeatMode = repeatMode_converter.get(data.get("repeatMode", -1), "Unknown")
        self.selectedItemIndex = data.get("selectedItemIndex", 0)