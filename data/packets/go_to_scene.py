from .packet import Packet
from .packet_registry import register_packet

@register_packet
class PacketPlayerGoToScene(Packet):
    """
    [Client] ---> [Server]
    Packet id: 11
    Send to the server to with the wanted player name to get a session id
    """
    PACKET_ID = 11
    session_id: str
    scene: str
    name: str
    x: int
    y: int
    hat: int
    body: int

    def __init__(self,session_id,scene:str,name:str,x:int,y:int,hat:int,body:int):
        super().__init__(scene,session_id,name,x,y,hat,body)