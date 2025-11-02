from .packet import Packet
from .packet_registry import register_packet

@register_packet
class PacketLoadPlayer(Packet):
    """
    [Server] ---> [Client]
    Packet id: 12
    Send to the client to command the creation of a new player in the current player scene.
    This packet may be send multiple times when the main player enters a new scene
    """
    PACKET_ID = 12
    session_id: str
    name: str
    x: int
    y: int
    hat: int
    body: int

    def __init__(self,session_id:str,name:str,x:int,y:int,hat:int,body:int):
        super().__init__(session_id,name,x,y,hat,body)