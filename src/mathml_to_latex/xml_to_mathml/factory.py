from .adapter import XmlToMathMLAdapter
from .services.error_handler import ErrorHandler
from .services.xml_elements_to_mathml_element import (
    ElementsToMathMLAdapter,
)


def make_xml_to_mathml_adapter() -> XmlToMathMLAdapter:
    xml_elements_to_mathml_element_adapter = ElementsToMathMLAdapter()
    error_handler = ErrorHandler()

    return XmlToMathMLAdapter(xml_elements_to_mathml_element_adapter, error_handler)
