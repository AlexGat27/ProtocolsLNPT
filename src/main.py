from Tests import example_S7CommSetup, example_COTP, example_S7commAckDataReadVar, example_S7CommJobReadVar

if __name__ == "__main__":
    example_S7CommJobReadVar()
    print('\n')
    example_COTP()
    print('\n')
    example_S7commAckDataReadVar()
    print('\n')
    example_S7CommSetup()