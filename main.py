from frostlight_engine import *

from data.classes.network import NetworkManager
from data.classes.player_manager import PlayerManager
from data.classes.scene_manager import SceneManager
from data.classes.overlay_manager import OverlayManager
from data.classes.save_manager import SaveManager
from data.classes.player import Player
from data.classes.font import Font
from data.classes.time import Time

class Game(FrostlightEngine):
    def __init__(self):
        super().__init__(canvas_size=[320,180],fps_limit=165)
        self.running = True
        self.debug = True

        self.state = "main_menu"

        self.input.bind("emoji1",KEYBOARD.NUM_1,CLICKED)
        self.input.bind("emoji2",KEYBOARD.NUM_2,CLICKED)
        self.input.bind("emoji3",KEYBOARD.NUM_3,CLICKED)
        self.input.bind("emoji4",KEYBOARD.NUM_4,CLICKED)
        self.input.bind("emoji5",KEYBOARD.NUM_5,CLICKED)
        self.input.bind("emoji6",KEYBOARD.NUM_6,CLICKED)
        self.input.bind("emoji7",KEYBOARD.NUM_7,CLICKED)
        self.input.bind("emoji8",KEYBOARD.NUM_8,CLICKED)
        self.input.bind("emoji9",KEYBOARD.NUM_9,CLICKED)

        self.input.bind("left",KEYBOARD.LEFT,PRESSED)
        self.input.bind("left",KEYBOARD.A,PRESSED)
        self.input.bind("right",KEYBOARD.RIGHT,PRESSED)
        self.input.bind("right",KEYBOARD.D,PRESSED)

        self.input.bind("up",KEYBOARD.UP,PRESSED)
        self.input.bind("up",KEYBOARD.W,PRESSED)
        self.input.bind("down",KEYBOARD.DOWN,PRESSED)
        self.input.bind("down",KEYBOARD.S,PRESSED)

        self.input.bind("accept",MOUSE.LEFT,PRESSED)
        self.input.bind("accept",KEYBOARD.ENTER,PRESSED)

        self.save_manager = SaveManager(self)
        self.network_manager = NetworkManager(self)
        self.scene_manager = SceneManager(self)
        self.player_manager = PlayerManager(self)
        self.overlay_manager = OverlayManager(self)

        self.font = Font(self,1)
        self.time = Time(self)
        self.player = Player(self,True)

        self.player_manager.register_player(self.player)

        self.scene_manager.load_scene("main_menu")

        self.network_manager.run()
    
    def event_quit(self):
        self.running = False
        self.network_manager.close()
    
    def update(self):
        if self.state != "main_menu":
            self.time.update()
        
        self.scene_manager.update()
        self.overlay_manager.update()

    def draw(self):
        self.scene_manager.draw()
        self.overlay_manager.draw()

game = Game()
game.run()