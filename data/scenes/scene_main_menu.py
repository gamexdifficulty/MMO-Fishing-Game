import os
import time
from frostlight_engine import *

class SceneMainMenu:
    def __init__(self,game):
        self.game = game
        self.island_sprite = Sprite(os.path.join("scene1","island.png"))
        self.house_sprite = Sprite(os.path.join("scene1","house.png"))
        self.water_sprite = Sprite(os.path.join("scene1","waterfg.png"))
        self.cloud_sprite = Sprite(os.path.join("scene1","clouds.png"))
        self.overlay_sprite = Sprite("overlay.png")

        self.water_sprite.set_custom_shader("water_wave.frag")
        self.overlay_sprite.set_custom_shader("menu_bg.frag")

    def update(self):
        self.water_sprite.set_custom_uniforms("uTime",time.time() % 1000)

    def draw(self):
        self.game.window.fill(76,139,216)
        self.game.window.render(self.island_sprite,[0,0])
        self.game.window.render(self.water_sprite,[0,155])
        self.game.window.render(self.house_sprite,[0,0])
        self.game.window.render(self.cloud_sprite,[0,0])
        self.game.window.render(self.overlay_sprite,[0,0])