from Protocols import Params, COTProtocol

def example_COTP():
    # Создание списка параметров COTP
    cotp_parameters = [
        Params(code=1, length=1, value=10),
        Params(code=2, length=2, value=11),
        Params(code=3, length=2, value=12)
    ]

    # Создание объекта протокола
    cot_protocol = COTProtocol(
        tcp_flags=[0x0018],  # Пример значения флагов TCP
        trkt_version=1,
        trkt_length=253,
        cotp_pdu_type=0x0f,
        cotp_dst_reference=123,
        cotp_src_reference=124,
        cotp_class=16,
        cotp_parameters=cotp_parameters
    )

    # Получение байтового представления
    byte_representation = cot_protocol.to_byte()
    print("Byte representation:", byte_representation)

    # Получение битового представления
    bit_representation = cot_protocol.to_bit()
    print("Bit representation:", bit_representation)