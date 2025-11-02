from .packet import Packet
from .packet_registry import register_packet

@register_packet
class PacketUpdatePlayer(Packet):
    """
    [Server] <---> [Client]
    Packet id: 14
    Send between the server and client to communicate player attribute updates
    """
    PACKET_ID = 14
    session_id: str
    x: int
    y: int
    animation: str
    flipped: bool

    def __init__(self,session_id:str,x:int,y:int,animation:str,flipped:bool):
        super().__init__(session_id,x,y,animation,flipped)