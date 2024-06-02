from Protocols import S7commJobReadVar

def example_S7CommJobReadVar():
    # Создание экземпляра класса S7commJobReadVar
    s7_job_read_packet = S7commJobReadVar(
        tcp_flags=[0x10, 0x08],  # Пример значений флагов TCP
        cotp_pdu_type=0x0f,
        s7_function="Read Var",
        s7_specification=18,  # Пример данных
        s7_length=8,
        s7_db_index=14,
        s7_area="Q",
        s7_address="DB14.DBW0"
    )

    # Получение байтового представления
    byte_representation = s7_job_read_packet.to_byte()
    print("Byte representation:", byte_representation)

    # Получение битового представления
    bit_representation = s7_job_read_packet.to_bit()
    print("Bit representation:", bit_representation)
