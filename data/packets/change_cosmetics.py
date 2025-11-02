from .packet import Packet
from .packet_registry import register_packet

@register_packet
class PacketChangeCosmetics(Packet):
    """
    [Server] <---> [Client]
    Packet id: 15
    Send between the server and client to change a players cosmetics
    """
    PACKET_ID = 15
    session_id: str
    hat: int
    body: int

    def __init__(self,session_id:str,hat:int,body:int):
        super().__init__(session_id,hat,body)