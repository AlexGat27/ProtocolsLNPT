from Protocols import S7Protocol, S7MessageType, S7Function, S7SetupCommunicationParams, S7VariableSpec, S7AckDataReadParams, S7AckDataWriteParams, S7JobReadParams, S7JobWriteParams

def example_S7_Setup():
    # Создаем объект параметров SetupCommunication
    setup_params = S7SetupCommunicationParams(
        function=S7Function.SETUP_COMMUNICATION,
        reserved=0x00,
        max_amq_calling=100,
        max_amq_called=200,
        pdu_length=300,
    )

    # Инициализируем объект протокола S7
    s7_protocol = S7Protocol(
        protocolID=1,
        message_type=S7MessageType.JOB,
        identificator=1234,
        pdur_ref=5678,
        function=S7Function.SETUP_COMMUNICATION,
        params=setup_params
    )

    # Преобразуем объект протокола в байтовое представление
    protocol_bytes = s7_protocol.to_byte()

    # Преобразуем объект протокола в битовое представление
    protocol_bits = s7_protocol.to_bit()

    # Выводим результаты
    print("\nБайтовое представление протокола S7 с функцией Setup Communication:")
    print(protocol_bytes)
    print("Битовое представление протокола S7 с функцией Setup Communication:")
    print(protocol_bits)

def example_S7_AckRead():
    # Создаем объект данных для ACK сообщения чтения переменной
    data = S7AckDataReadParams.Data(
        return_code=S7AckDataReadParams.ReturnCode.SUCCESS,
        transport_size=8,
        value=123
    )

    # Создаем объект параметров ACK сообщения чтения переменной
    ack_data_read_params = S7AckDataReadParams(
        class_error=S7AckDataReadParams.ClassError.NO_ERROR,
        code_error=0,
        data=data,
    )

    # Инициализируем объект протокола S7
    s7_protocol = S7Protocol(
        protocolID=1,
        message_type=S7MessageType.ACK_DATA,
        identificator=5678,
        pdur_ref=1234,
        function=S7Function.READ_VAR,
        params=ack_data_read_params
    )

    # Преобразуем объект протокола в байтовое представление
    protocol_bytes = s7_protocol.to_byte()

    # Преобразуем объект протокола в битовое представление
    protocol_bits = s7_protocol.to_bit()

    # Выводим результаты
    print("\nБайтовое представление протокола S7 Ack Data с функцией Read Var:")
    print(protocol_bytes)
    print("Битовое представление протокола S7 Ack Data с функцией Read Var:")
    print(protocol_bits)

def example_S7_JobRead():
    job_read_params = S7JobReadParams(
        spec=0x12,
        addr_length=2,
        syntax_id=0x10,
        transport_size=1,
        length=5,
        db_index=1,
        var_area='Q',
        var_address=1000,
    )

    # Инициализируем объект протокола S7
    s7_protocol = S7Protocol(
        protocolID=1,
        message_type=S7MessageType.JOB,
        identificator=1234,
        pdur_ref=5678,
        function=S7Function.READ_VAR,
        params=job_read_params
    )

    # Преобразуем объект протокола в байтовое представление
    protocol_bytes = s7_protocol.to_byte()

    # Преобразуем объект протокола в битовое представление
    protocol_bits = s7_protocol.to_bit()

    # Выводим результаты
    print("\nБайтовое представление протокола S7 Job с функцией Read Var:")
    print(protocol_bytes)
    print("Битовое представление протокола S7 Job с функцией Read Var:")
    print(protocol_bits)

def example_S7_Write():
    # Создаем объект параметров записи переменной
    job_write_params = S7JobWriteParams(
        val_area='I',
    )

    # Инициализируем объект протокола S7 для записи переменной
    s7_write_protocol = S7Protocol(
        protocolID=1,
        message_type=S7MessageType.JOB,
        identificator=1234,
        pdur_ref=5678,
        function=S7Function.WRITE_VAR,
        params=job_write_params
    )

    # Преобразуем объект протокола записи переменной в байтовое представление
    write_protocol_bytes = s7_write_protocol.to_byte()

    # Преобразуем объект протокола записи переменной в битовое представление
    write_protocol_bits = s7_write_protocol.to_bit()

    # Создаем объект параметров подтверждения записи переменной
    ack_write_params = S7AckDataWriteParams(
        return_code=S7AckDataWriteParams.ReturnCode.INVALID_ADDRESS,
    )

    # Инициализируем объект протокола S7 для подтверждения записи переменной
    s7_ack_write_protocol = S7Protocol(
        protocolID=1,
        message_type=S7MessageType.ACK_DATA,
        identificator=5678,
        pdur_ref=1234,
        function=S7Function.WRITE_VAR,
        params=ack_write_params
    )

    # Преобразуем объект протокола подтверждения записи переменной в байтовое представление
    ack_write_protocol_bytes = s7_ack_write_protocol.to_byte()

    # Преобразуем объект протокола подтверждения записи переменной в битовое представление
    ack_write_protocol_bits = s7_ack_write_protocol.to_bit()

    # Выводим результаты
    print("\nБайтовое представление протокола записи переменной S7 Job с функцией Write:")
    print(write_protocol_bytes)
    print("Битовое представление протокола записи переменной S7 Job с функцией Write:")
    print(write_protocol_bits)

    print("\nБайтовое представление протокола подтверждения записи переменной S7 Ack Data с функцией Write:")
    print(ack_write_protocol_bytes)
    print("Битовое представление протокола подтверждения записи переменной S7 Ack Data с функцией Write:")
    print(ack_write_protocol_bits)
