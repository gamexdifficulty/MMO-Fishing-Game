from .packet import Packet
from .packet_registry import register_packet

@register_packet
class PacketReturnSessionID(Packet):
    """
    [Server] ---> [Client]
    Packet id: 2
    Send to the client to confirm the login and give the session id
    """
    PACKET_ID = 2
    session_id: str
    def __init__(self,session_id:str):
        super().__init__(session_id)