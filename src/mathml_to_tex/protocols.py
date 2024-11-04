from abc import ABC, abstractmethod

class MathMLElement(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def value(self) -> str:
        pass

    @property
    @abstractmethod
    def children(self) -> list:
        pass

    @property
    @abstractmethod
    def attributes(self) -> dict:
        pass

class ToLaTeXConverter(ABC):
    @abstractmethod
    def convert(self) -> str:
        pass

class GenericMathMLElement(MathMLElement):
    def __init__(self, name: str, value: str, children: list, attributes: dict):
        self._name = name
        self._value = value
        self._children = children
        self._attributes = attributes

    @property
    def name(self) -> str:
        return self._name

    @property
    def value(self) -> str:
        return self._value

    @property
    def children(self) -> list:
        return self._children

    @property
    def attributes(self) -> dict:
        return self._attributes

class VoidMathMLElement(MathMLElement):
    @property
    def name(self) -> str:
        return 'void'

    @property
    def value(self) -> str:
        return ''

    @property
    def children(self) -> list:
        return []

    @property
    def attributes(self) -> dict:
        return {}