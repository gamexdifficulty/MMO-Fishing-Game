# data/packets/packet_registry.py
PACKET_REGISTRY = {}

def register_packet(cls):
    PACKET_REGISTRY[cls.PACKET_ID] = cls
    return cls
