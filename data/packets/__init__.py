import importlib
import pkgutil
import inspect
from typing import TYPE_CHECKING

from .packet_registry import PACKET_REGISTRY, register_packet

__all__ = []

if TYPE_CHECKING:
    from .change_cosmetics import PacketChangeCosmetics
    from .client_exit import PacketClientLeft
    from .do_emoji import PacketDoEmoji
    from .go_to_scene import PacketPlayerGoToScene
    from .load_player import PacketLoadPlayer
    from .request_session_id import PacketRequestSessionID
    from .return_session_id import PacketReturnSessionID
    from .unload_player import PacketUnloadPlayer
    from .update_player import PacketUpdatePlayer

package_name = __name__

for _, module_name, _ in pkgutil.iter_modules(__path__):
    if module_name in ("packet", "packet_registry"):
        continue

    module = importlib.import_module(f"{package_name}.{module_name}")

    for name, obj in inspect.getmembers(module, inspect.isclass):
        if obj.__module__ == module.__name__:
            globals()[name] = obj
            __all__.append(name)
