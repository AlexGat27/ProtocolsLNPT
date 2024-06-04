from Protocols import TPKTProtocol

def example_TPKT():
    tpkt = TPKTProtocol(version=3, reserved=0, length=1024)
    tpkt_bytes = tpkt.to_byte()
    tpkt_bits = tpkt.to_bit()

    print("\nTPKT bytes:", tpkt_bytes)
    print("TPKT bits:", tpkt_bits)