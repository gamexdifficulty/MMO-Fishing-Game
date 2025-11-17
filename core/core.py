from init import *

from core.builder import *
from core.log_manager import *
from core.window import *
from core.input import Input

class Core:
    def __init__(self,args={},*loop_functions):
        self.main_loop_running = True
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.last_time = time.time()
        self.fps_limit = args["fps_limit"]

        self.loop_functions = loop_functions

        self.build_manager = Builder()
        self.event_manager = None
        self.input_manager = Input()
        self.logger = Logger()
        self.save_manager = None

        self.event_window_resize = None
        self.event_quit = None

        self.logger.info("Started Frostlightengine version 2.0.0 [DEV]")

    def get_fps(self) -> int:
        return int(min(self.clock.get_fps(),99999999))

    def start_main_loop(self) -> None:
        pygame.event.set_allowed([pygame.QUIT,
                                  pygame.WINDOWMOVED, pygame.VIDEORESIZE,
                                  pygame.KEYDOWN, pygame.KEYUP,
                                  pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION,
                                  pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN, pygame.JOYAXISMOTION, pygame.JOYHATMOTION,
                                  pygame.JOYDEVICEADDED, pygame.JOYDEVICEREMOVED])
        
        while self.main_loop_running:
            try:
                self.clock.tick(self.fps_limit)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.main_loop_running = False
                        if self.event_quit != None:
                            self.event_quit()
                        self.logger.info("Closed window, stopping game.")

                    # Window events
                    if event.type == pygame.WINDOWRESIZED:
                        if self.event_window_resize != None:
                            self.event_window_resize([event.x,event.y])

                    elif event.type == pygame.WINDOWMOVED:
                        self.last_time = time.time()
                        self.delta_time = 0

                    # Keyboard events
                    elif event.type == pygame.KEYDOWN:
                        self.input_manager._handle_key_event(event)

                    elif event.type == pygame.KEYUP:
                        self.input_manager._handle_key_event(event)

                    # Mouse events
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        self.input_manager._handle_mouse_event(event)

                    elif event.type == pygame.MOUSEBUTTONUP:
                        self.input_manager._handle_mouse_event(event)

                    # Joystick events
                    elif event.type == pygame.JOYBUTTONDOWN:
                        self.input_manager._handle_joy_event(event)

                    elif event.type == pygame.JOYBUTTONUP:
                        self.input_manager._handle_joy_event(event)

                    elif event.type == pygame.JOYAXISMOTION:
                        self.input_manager._handle_joy_event(event)

                    elif event.type == pygame.JOYHATMOTION:
                        self.input_manager._handle_joy_event(event)

                    elif event.type == pygame.JOYDEVICEADDED:
                        self.input_manager._init_joysticks()

                    elif event.type == pygame.JOYDEVICEREMOVED:
                        self.input_manager._init_joysticks()

                self.delta_time = time.time() - self.last_time
                self.last_time = time.time()

                for function in self.loop_functions:
                    function()
            except Exception as e:
                if type(Exception) == KeyboardInterrupt:
                    self.main_loop_running = False
                    self.event_quit()
                else:
                    self.logger.error("Error while running main loop.")
