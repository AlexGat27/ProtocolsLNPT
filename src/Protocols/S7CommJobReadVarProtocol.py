from .BaseProtocol import BaseProtocol

class S7commJobReadVar(BaseProtocol):
    def __init__(self, tcp_flags: list[int], cotp_pdu_type: int, s7_function: str, s7_specification: int, s7_length: int, s7_db_index: int, s7_area: str, s7_address: str):
        self.tcp_flags = tcp_flags
        self.cotp_pdu_type = cotp_pdu_type
        self.s7_function = s7_function
        self.s7_specification = s7_specification
        self.s7_length = s7_length
        self.s7_db_index = s7_db_index
        self.s7_area = s7_area
        self.s7_address = s7_address

    def to_byte(self):
        byte_array = bytearray()

        tcp_flags_byte = 0
        for flag in self.tcp_flags:
            tcp_flags_byte |= flag

        byte_array.append(tcp_flags_byte)
        byte_array.append(self.cotp_pdu_type)
        byte_array.extend(self.s7_function.encode(encoding="utf8"))  # Преобразуем строку функции в байты
        byte_array.append(self.s7_specification)
        byte_array.extend(self.s7_length.to_bytes(2, 'big'))
        byte_array.extend(self.s7_db_index.to_bytes(2, 'big'))
        byte_array.append(ord(self.s7_area))  # Преобразуем строку области в ее ASCII-код
        byte_array.extend(self.s7_address.encode())

        return bytes(byte_array)

    def to_bit(self):
        byte_representation = self.to_byte()
        bit_string = ''.join(f'{byte:08b}' for byte in byte_representation)
        return bit_string
