from .BaseProtocol import BaseProtocol

class S7commSetupCommunication(BaseProtocol):
    def __init__(self, tcp_flags: list[int], cotp_pdu_type: int, s7_protocol_id: int, s7_message_type: int, s7_redundancy_id: int,
                 s7_pdu_ref: int, s7_param_length: int, s7_data_length: int, s7_function: int, s7_reservation: int,
                 s7_max_amq_calling: int, s7_max_amq_called: int, s7_pdu_length: int):
        self.tcp_flags = tcp_flags
        self.cotp_pdu_type = cotp_pdu_type
        self.s7_protocol_id = s7_protocol_id
        self.s7_message_type = s7_message_type
        self.s7_redundancy_id = s7_redundancy_id
        self.s7_pdu_ref = s7_pdu_ref
        self.s7_param_length = s7_param_length
        self.s7_data_length = s7_data_length
        self.s7_function = s7_function
        self.s7_reservation = s7_reservation
        self.s7_max_amq_calling = s7_max_amq_calling
        self.s7_max_amq_called = s7_max_amq_called
        self.s7_pdu_length = s7_pdu_length

    def to_byte(self):
        byte_array = bytearray()

        tcp_flags_byte = 0
        for flag in self.tcp_flags:
            tcp_flags_byte |= flag

        byte_array.append(tcp_flags_byte)
        byte_array.append(self.cotp_pdu_type)
        byte_array.append(self.s7_protocol_id)
        byte_array.append(self.s7_message_type)
        byte_array.extend(self.s7_redundancy_id.to_bytes(2, 'big'))
        byte_array.extend(self.s7_pdu_ref.to_bytes(2, 'big'))
        byte_array.extend(self.s7_param_length.to_bytes(2, 'big'))
        byte_array.extend(self.s7_data_length.to_bytes(2, 'big'))
        byte_array.append(self.s7_function)
        byte_array.append(self.s7_reservation)
        byte_array.extend(self.s7_max_amq_calling.to_bytes(2, 'big'))
        byte_array.extend(self.s7_max_amq_called.to_bytes(2, 'big'))
        byte_array.extend(self.s7_pdu_length.to_bytes(2, 'big'))

        return bytes(byte_array)

    def to_bit(self):
        byte_representation = self.to_byte()
        bit_string = ''.join(f'{byte:08b}' for byte in byte_representation)
        return bit_string
