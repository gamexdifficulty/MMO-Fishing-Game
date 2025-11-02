from .packet import Packet
from .packet_registry import register_packet

@register_packet
class PacketRequestSessionID(Packet):
    """
    [Client] ---> [Server]
    Packet id: 1
    Send to the server to with the wanted player name to get a session id
    """
    PACKET_ID = 1
    name: str
    def __init__(self,name:str):
        super().__init__(name)