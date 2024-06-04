from .BaseProtocol import BaseProtocol

class TPKTProtocol(BaseProtocol):
    def __init__(self, version: int, reserved: int, length: int):
        self.version = version
        self.reserved = reserved
        self.length = length

    def to_byte(self):
        bites = bytearray()
        bites.append(self.version)
        bites.append(self.reserved)
        bites.extend(self.length.to_bytes(2, 'big'))
        return bites

    def to_bit(self):
        byte_representation = self.to_byte()
        return ''.join(f'{byte:08b}' for byte in byte_representation)