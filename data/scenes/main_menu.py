import os
import time
from frostlight_engine import *
from data.classes.button import Button
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game

class SceneMainMenu:

    SCENE_NAME = "main_menu"

    def __init__(self,game:"Game"):
        self.game = game
        self.play_button = Button(self.game,os.path.join("ui","main_menu_button.png"),[100,100],[45,15],self.button_press_play)

    def button_press_play(self):
        self.game.scene_manager.load_scene(self.game.save_manager.load("current_scene","grass_island_small_house"))

    def update(self):
        self.play_button.update()

    def draw(self):
        self.game.window.fill(76,139,216)
        self.play_button.draw()