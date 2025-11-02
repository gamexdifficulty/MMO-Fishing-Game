from typing import get_type_hints

class Packet:
    PACKET_ID = None

    def __init__(self, *args):
        field_names = list(get_type_hints(self.__class__).keys())

        for name, value in zip(field_names, args):
            setattr(self, name, value)

        self.data = list(args)

    @classmethod
    def from_bytes(cls, args):
        return cls(*args)

    def get_sequence(self):
        field_types = list(get_type_hints(self.__class__).values())
        data = []
        for i, value in enumerate(self.data):
            dtype = field_types[i]
            if dtype == bool:
                data.append("b")
            elif dtype == int:
                data.append("i")
            elif dtype == str:
                data.append("s")
        return data
