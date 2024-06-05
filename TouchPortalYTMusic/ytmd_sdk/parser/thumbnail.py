class Thumbnail(object):
    url: str = ""
    width: int = 0
    height: int = 0

    def __init__(self, data) -> None:
        self.url = data.get("url", "")
        self.width = data.get("width", 0)
        self.height = data.get("height", 0)