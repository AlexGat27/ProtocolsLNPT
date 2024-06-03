from .BaseProtocol import BaseProtocol
from enum import Enum

class COTPParamCode(Enum):
    TPDU_SIZE = 0xC0
    SRC_TSAP = 0xC1
    DST_TSAP = 0xC2

class COTPType(Enum):
    CR = 0xE0  # Connect Request
    CC = 0xD0  # Connect Confirm
    DR = 0x80  # Disconnect Request
    DC = 0xC0  # Disconnect Confirm
    DT = 0xF0  # Data Transfer
    AK = 0x60  # Data Acknowledge
    RJ = 0x50  # Reject
    ED = 0x10  # Expedited Data
    EA = 0x20  # Expedited Data Acknowledge

class COTPClass(Enum):
    CLASS_0 = 0x00  # Simple Class
    CLASS_1 = 0x01  # Basic Error Recovery Class
    CLASS_2 = 0x02  # Multiplexing Class
    CLASS_3 = 0x03  # Error Recovery and Multiplexing Class

class COTPParams:
    def __init__(self, code: COTPParamCode, length: int, value: int) -> None:
        self.code = code.value
        self.length = length
        self.value = value

class COTProtocol(BaseProtocol):
    def __init__(self, pdu_type: COTPType, dst_reference: int, src_reference: int, cotp_class: COTPClass, parameters: list[COTPParams]):
        self.pdu_type = pdu_type.value
        self.dst_reference = dst_reference
        self.src_reference = src_reference
        self.cotp_class = cotp_class.value
        self.parameters = parameters

    def to_byte(self):
        bites = bytearray()
        bites.append(self.pdu_type)
        bites.extend(self.dst_reference.to_bytes(2, 'big'))
        bites.extend(self.src_reference.to_bytes(2, 'big'))
        bites.append(self.cotp_class)
        for param in self.parameters:
            bites.append(param.code)
            bites.append(param.length)
            bites.extend(param.value.to_bytes(param.length, 'big'))     
        return bites

    def to_bit(self):
        byte_representation = self.to_byte()
        return ''.join(f'{byte:08b}' for byte in byte_representation)