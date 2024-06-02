from Protocols import S7commSetupCommunication

def example_S7CommSetup():
    setup_communication_packet = S7commSetupCommunication(
        tcp_flags=[16, 32],
        cotp_pdu_type=15,
        s7_protocol_id=1,
        s7_message_type=0,
        s7_redundancy_id=1,
        s7_pdu_ref=100,
        s7_param_length=100,
        s7_data_length=200,
        s7_function=0xF0,
        s7_reservation=10,
        s7_max_amq_calling=512,
        s7_max_amq_called=512,
        s7_pdu_length=256
    )

    # Получаем байтовое представление пакета
    byte_representation = setup_communication_packet.to_byte()

    # Получаем битовое представление пакета
    bit_representation = setup_communication_packet.to_bit()

    # Выводим результаты
    print("Byte representation:", byte_representation)
    print("Bit representation:", bit_representation)