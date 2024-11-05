from typing import List
from xml.dom.minidom import parseString, Element
import re

from ..el_to_tex.protocols import MathMLElement
from .services.error_handler import ErrorHandler
from .services.xml_elements_to_mathml_element import (
    ElementsToMathMLAdapter,
)


class XmlToMathMLAdapter:
    def __init__(
        self, elements_converter: ElementsToMathMLAdapter, error_handler: ErrorHandler
    ):
        self._xml = ""
        self._elements_converter = elements_converter
        self._error_handler = error_handler

    def convert(self, xml: str) -> List[MathMLElement]:
        self._xml = self._remove_line_breaks(xml)
        self._xml = self._remove_ms_word_prefixes(self._xml)

        return self._elements_converter.convert(self._mathml_elements)

    def _fix_error(self, error: Exception) -> None:
        self._xml = self._error_handler.fix_error(self._xml, error)

    def _remove_line_breaks(self, xml: str) -> str:
        line_break_pattern = re.compile(r"\n|\r\n|\r")
        return line_break_pattern.sub("", xml)

    def _remove_ms_word_prefixes(self, xml: str) -> str:
        ms_word_prefix_pattern = re.compile(r"mml:")
        return ms_word_prefix_pattern.sub("", xml)

    @property
    def _mathml_elements(self) -> List[Element]:
        try:
            dom = parseString(self._xml)
            elements = dom.getElementsByTagName("math")
        except Exception as e:
            self._fix_error(e)
            return self._mathml_elements

        return list(elements)
