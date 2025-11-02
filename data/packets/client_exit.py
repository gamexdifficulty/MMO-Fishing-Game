from .packet import Packet
from .packet_registry import register_packet

@register_packet
class PacketClientLeft(Packet):
    """
    [Client] ---> [Server]
    Packet id: 0
    Send to the server to close the connection
    """
    PACKET_ID = 0