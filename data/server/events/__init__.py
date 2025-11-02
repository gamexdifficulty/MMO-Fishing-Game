import importlib
import pkgutil
import inspect
from typing import TYPE_CHECKING

__all__ = []

from .player_change_cosmetic import EventPlayerChangeCosmetic
from .player_change_scene import EventPlayerChangeScene
from .player_do_emoji import EventPlayerDoEmoji
from .player_leave import EventPlayerLeave

package_name = __name__

for _, module_name, _ in pkgutil.iter_modules(__path__):
    module = importlib.import_module(f"{package_name}.{module_name}")

    for name, obj in inspect.getmembers(module, inspect.isclass):
        if obj.__module__ == module.__name__:
            globals()[name] = obj
            __all__.append(name)
