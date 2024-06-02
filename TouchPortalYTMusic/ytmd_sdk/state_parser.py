import json

class StateParser(object):
    def __init__(self):
        self.state = None

    def parse(self, data: dict):
        self.state = json.loads(data)

    def get_player_state(self) -> str:
        """get player state

        Returns:
            str: Unknown|Paused|Playing|Buffering
        """

        state = {
            -1: "Unknown",
            0: "Paused",
            1: "Playing",
            2: "Buffering"
        }
        return state[self.state["player"]['trackState']]
    
    def get_video_progress(self):
        return self.state["player"]["videoProgress"]
    