class SceneManager:
    def __init__(self,game):
        self.game = game
        self.scenes = {}
        self.current_scene = None

    def update(self):
        if self.current_scene != None:
            self.scenes[self.current_scene].update()

    def draw(self):
        if self.current_scene != None:
            self.scenes[self.current_scene].draw()

    def register_scene(self, scene_name, scene):
        self.scenes[scene_name] = scene

    def load_scene(self, scene_name):
        self.current_scene = scene_name