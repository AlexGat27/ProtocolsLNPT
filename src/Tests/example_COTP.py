from Protocols import COTProtocol, COTPClass, COTPParamCode, COTPParams, COTPType

def example_COTP():
    parameters = [
        COTPParams(COTPParamCode.TPDU_SIZE, 1, 9),  # tpdu-size with length 1 byte and value 9 (512 bytes)
        COTPParams(COTPParamCode.SRC_TSAP, 2, 0x2000),  # src-tsap with length 2 bytes and value 0x2000
        COTPParams(COTPParamCode.DST_TSAP, 2, 0x2100)   # dst-tsap with length 2 bytes and value 0x2100
    ]

    cotp = COTProtocol(COTPType.CR, 1, 2, COTPClass.CLASS_0, parameters)
    cotp_bytes = cotp.to_byte()
    cotp_bits = cotp.to_bit()

    print("\nCOTP bytes:", cotp_bytes)
    print("COTP bits:", cotp_bits)