from .BaseProtocol import BaseProtocol
from enum import Enum
from abc import ABC, abstractmethod


class S7MessageType(Enum):
    JOB = 0x01
    ACK_DATA = 0x03


class S7Function(Enum):
    SETUP_COMMUNICATION = 0xF0
    READ_VAR = 0x04
    WRITE_VAR = 0x05


class S7VariableSpec(Enum):
    VARIABLE_SPEC = 0x12

class S7BaseParams(ABC):
    def __init__(self, param_length: int, data_length: int) -> None:
        self.param_length = param_length
        self.data_length = data_length
    @abstractmethod
    def to_byte(self):
        pass

class S7AckDataReadParams(S7BaseParams):

    class ReturnCode(Enum):
        SUCCESS = 0xff

    class ClassError(Enum):
        NO_ERROR = 0x04

    class Data:
        def __init__(self, return_code: 'S7AckDataReadParams.ReturnCode', transport_size: int, value: int) -> None:
            self.return_code = return_code
            self.transport_size = transport_size
            self.length = (value.bit_length() + 7) // 8
            self.value = value

        def to_byte(self):
            bites = bytearray()
            bites.append(self.return_code.value)
            bites.append(self.transport_size)
            bites.extend(self.length.to_bytes(2, 'big'))
            bites.extend(self.value.to_bytes(self.length, 'big'))
            return bites


    def __init__(self, class_error: 'S7AckDataReadParams.ClassError', code_error: int, data: 'S7AckDataReadParams.Data') -> None:
        param_length = 2 + len(data.to_byte())
        super().__init__(param_length, data.length)
        self.class_error = class_error.value
        self.code_error = code_error
        self.data = data

    def to_byte(self):
        bites = bytearray()
        bites.append(self.class_error)
        bites.append(self.code_error)
        bites.extend(self.data.to_byte())
        return bites

class S7AckDataWriteParams(S7BaseParams):

    class ReturnCode(Enum):
        INVALID_ADDRESS = 0x00

    def __init__(self, return_code: ReturnCode) -> None:
        super().__init__(1, 1)
        self.return_code = return_code

    def to_byte(self):
        bites = bytearray()
        bites.append(self.return_code.value)
        return bites

class S7JobReadParams(S7BaseParams):

    def __init__(self, spec: int, addr_length: int, syntax_id: int, transport_size: int, 
                 length: int, db_index: int, var_area: str, var_address: int) -> None:
        param_length = 12
        super().__init__(param_length, 0)
        self.spec = spec  # 1 байт – спецификация переменной
        self.addr_length = addr_length  # 2 байт – длина дальнейшей адресации
        self.syntax_id = syntax_id  # 3 байт – синтаксический ID
        self.transport_size = transport_size  # 4 байт – транспортный размер
        self.length = length  # 5-6 байты – длина
        self.db_index = db_index  # 7-8 байты – индекс базы данных
        self.var_area = var_area  # 9 байт – область переменной
        self.var_address = var_address  # 10-12 байты – адрес переменной

    def to_byte(self):
        bites = bytearray()
        bites.append(self.spec)
        bites.append(self.addr_length)
        bites.append(self.syntax_id)
        bites.append(self.transport_size)
        bites.extend(self.length.to_bytes(2, 'big'))
        bites.extend(self.db_index.to_bytes(2, 'big'))
        bites.append(ord(self.var_area))
        bites.extend(self.var_address.to_bytes(3, 'big'))
        return bites

class S7JobWriteParams(S7BaseParams):

    def __init__(self, val_area: str) -> None:
        param_length = 1
        super().__init__(param_length, 0)
        self.val_area = val_area

    def to_byte(self):
        bites = bytearray()
        bites.append(ord(self.val_area))
        return bites

class S7SetupCommunicationParams(S7BaseParams):
    def __init__(self, function: S7Function, reserved: int, max_amq_calling: int, max_amq_called: int, pdu_length: int) -> None:
        param_length = 8
        super().__init__(param_length, 0)
        self.function = function  # 1 байт – функция (В данном случае Setup communication 0xf0)
        self.reserved = reserved  # 2 байт – резервация
        self.max_amq_calling = max_amq_calling  # 3-4 байты – max AmQ calling
        self.max_amq_called = max_amq_called  # 5-6 байты – max AmQ called
        self.pdu_length = pdu_length  # 7-8 байты – длина PDU

    def to_byte(self):
        bites = bytearray()
        bites.append(self.function.value)
        bites.append(self.reserved)
        bites.extend(self.max_amq_calling.to_bytes(2, 'big'))
        bites.extend(self.max_amq_called.to_bytes(2, 'big'))
        bites.extend(self.pdu_length.to_bytes(2, 'big'))
        return bites

class S7Protocol(BaseProtocol):
    def __init__(self, protocolID: int, message_type: S7MessageType, identificator: int, pdur_ref: int, function: S7Function, params: S7BaseParams):
        self.protocolID = protocolID
        self.message_type = message_type
        self.identificator = identificator
        self.pdur_ref = pdur_ref
        self.param_length = params.param_length
        self.data_length = params.data_length
        self.function = function
        self.params = params

    def to_byte(self):
        bites = bytearray()
        bites.append(self.protocolID)
        bites.append(self.message_type.value)
        bites.extend(self.identificator.to_bytes(2, 'big'))
        bites.extend(self.pdur_ref.to_bytes(2, 'big'))
        bites.append(self.function.value)
        bites.extend(self.param_length.to_bytes(2, 'big'))
        bites.extend(self.data_length.to_bytes(2, 'big'))
        bites.extend(self.params.to_byte())
        return bites

    def to_bit(self):
        byte_representation = self.to_byte()
        return ''.join(f'{byte:08b}' for byte in byte_representation)