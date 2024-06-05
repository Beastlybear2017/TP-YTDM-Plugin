from .thumbnail import Thumbnail

class queueItem(object):
    title: str = ""
    author: str = ""
    duration: str = ""
    thumbnails: list[Thumbnail] = []
    selected: bool = False
    videoId: str = ""
    counterparts: None

    def __init__(self, data) -> None:
        self.title = data.get("title", "")
        self.author = data.get("author", "")
        self.duration = data.get("duration", "")
        self.thumbnails = [Thumbnail(item) for item in data['thumbnails']]