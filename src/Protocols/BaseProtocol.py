from abc import ABC, abstractmethod

class BaseProtocol(ABC):

    @abstractmethod
    def to_byte(self): pass

    @abstractmethod
    def to_bit(self): pass