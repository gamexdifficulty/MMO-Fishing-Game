import time

class Animation:
    def __init__(self, game):
        self.game = game
        self.config = {}
        
        self.start_time = time.time()

    def register(self, state:str, time:float, sprites:list):
        self.config[state] = {"duration":time, "count":len(sprites), "sprites":sprites}

    def get(self, state) -> int:
        elapsed = (time.time() - self.start_time) % self.config[state]["duration"]
        frame_time = self.config[state]["duration"] / self.config[state]["count"]
        frame_index = int(elapsed / frame_time)
        return self.config[state]["sprites"][frame_index]