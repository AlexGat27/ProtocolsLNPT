from .BaseProtocol import BaseProtocol

class Params:
    def __init__(self, code: int, length: int, value: int) -> None:
        self.code = code
        self.length = length
        self.value = value

class COTProtocol(BaseProtocol):
    def __init__(self, tcp_flags: list[int], trkt_version: int, trkt_length: int, cotp_pdu_type: int,
                 cotp_dst_reference: int, cotp_src_reference: int, cotp_class: int, cotp_parameters: list[Params]):
        self.tcp_flags = tcp_flags
        self.trkt_version = trkt_version
        self.trkt_length = trkt_length
        self.cotp_pdu_type = cotp_pdu_type
        self.cotp_dst_reference = cotp_dst_reference
        self.cotp_src_reference = cotp_src_reference
        self.cotp_class = cotp_class
        self.cotp_parameters = cotp_parameters

    def to_byte(self):
        byte_array = bytearray()
        tcp_flags_byte = 0
        for flag in self.tcp_flags:
            tcp_flags_byte |= flag

        byte_array.append(tcp_flags_byte)
        byte_array.append(self.trkt_version)
        byte_array.extend(self.trkt_length.to_bytes(2, 'big'))
        byte_array.append(self.cotp_pdu_type)
        byte_array.extend(self.cotp_dst_reference.to_bytes(2, 'big'))
        byte_array.extend(self.cotp_src_reference.to_bytes(2, 'big'))
        byte_array.append(self.cotp_class)
        for param in self.cotp_parameters:
            byte_array.append(param.code)
            byte_array.append(param.length)
            byte_array.append(param.value)
        return bytes(byte_array)

    def to_bit(self) -> str:
        byte_representation = self.to_byte()
        # Преобразуем байты в битовое представление
        bit_string = ''.join(f'{byte:08b}' for byte in byte_representation)
        return bit_string