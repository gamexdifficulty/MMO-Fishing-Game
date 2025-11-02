from .packet import Packet
from .packet_registry import register_packet

@register_packet
class PacketUnloadPlayer(Packet):
    """
    [Server] ---> [Client]
    Packet id: 13
    Send to the client to command the deletion of a new player in the current player scene.
    This is used, when a player leafs a scene.
    """
    PACKET_ID = 13
    session_id: str

    def __init__(self,session_id:str):
        super().__init__(session_id)