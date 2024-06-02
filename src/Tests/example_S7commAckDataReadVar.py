from Protocols import S7commAckDataReadVar

def example_S7commAckDataReadVar():
    # Создание экземпляра класса S7commAckDataReadVar
    s7_ack_data = S7commAckDataReadVar(
        tcp_flags=[16, 32],  # Флаги TCP
        cotp_pdu_type=15,  # Тип PDU COTP
        s7_rosctr=0,  # ROSCTR
        error_class=0,  # Класс ошибки
        error_code=0,  # Код ошибки
        return_code=0,  # Возвращаемый код
        transport_size=1,  # Транспортный размер
        length=2,  # Длина
        data_value=255  # Значение данных
    )

    # Получение байтового представления
    byte_representation = s7_ack_data.to_byte()
    print("Byte representation:", byte_representation)

    # Получение битового представления
    bit_representation = s7_ack_data.to_bit()
    print("Bit representation:", bit_representation)
