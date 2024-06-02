from .BaseProtocol import BaseProtocol

class S7commAckDataReadVar(BaseProtocol):
    def __init__(self, tcp_flags: list[int], cotp_pdu_type: int, s7_rosctr: int, error_class: int, error_code: int, return_code: int, transport_size: int, length: int, data_value: int):
        self.tcp_flags = tcp_flags
        self.cotp_pdu_type = cotp_pdu_type
        self.s7_rosctr = s7_rosctr
        self.error_class = error_class
        self.error_code = error_code
        self.return_code = return_code
        self.transport_size = transport_size
        self.length = length
        self.data_value = data_value

    def to_byte(self):
        byte_array = bytearray()

        tcp_flags_byte = 0
        for flag in self.tcp_flags:
            tcp_flags_byte |= flag

        byte_array.append(tcp_flags_byte)
        byte_array.append(self.cotp_pdu_type)
        byte_array.append(self.s7_rosctr)
        byte_array.append(self.error_class)
        byte_array.append(self.error_code)
        byte_array.append(self.return_code)
        byte_array.append(self.transport_size)
        byte_array.extend(self.length.to_bytes(2, 'big'))
        byte_array.append(self.data_value)

        return bytes(byte_array)

    def to_bit(self):
        byte_representation = self.to_byte()
        bit_string = ''.join(f'{byte:08b}' for byte in byte_representation)
        return bit_string
