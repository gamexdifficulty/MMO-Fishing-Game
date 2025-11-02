from .packet import Packet
from .packet_registry import register_packet

@register_packet
class PacketDoEmoji(Packet):
    """
    [Server] <---> [Client]
    Packet id: 16
    Send between the server and client to do a player emoji
    """
    PACKET_ID = 16
    session_id: str
    emoji: int

    def __init__(self,session_id:str,emoji:int):
        super().__init__(session_id,emoji)