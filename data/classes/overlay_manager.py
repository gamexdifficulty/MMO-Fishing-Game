import pkgutil
import inspect
import importlib
import data.overlays

class OverlayManager:
    def __init__(self, game):
        self.game = game
        self.overlay = {}
        self.overlay_current = None
        self.overlay_active = False

        for module_info in pkgutil.iter_modules(data.overlays.__path__):
            module = importlib.import_module(f"{data.overlays.__name__}.{module_info.name}")
            for _, obj in inspect.getmembers(module, inspect.isclass):
                if hasattr(obj, "OVERLAY_NAME"):
                    instance = obj(self.game)
                    self.register_overlay(instance)

    def update(self):
        if self.overlay_current != None:
            self.overlay[self.overlay_current].update()

    def draw(self):
        if self.overlay_current != None:
            self.overlay[self.overlay_current].draw()

    def register_overlay(self, overlay):
        overlay_name = overlay.OVERLAY_NAME
        self.overlay[overlay_name] = overlay

    def load_overlay(self, overlay_name):
        self.overlay_current = overlay_name
        self.overlay_active = True

    def unload_overlay(self):
        self.overlay_current = None
        self.overlay_active = False
        