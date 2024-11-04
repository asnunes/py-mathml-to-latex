from src.xml_to_mathml.adapter import XmlToMathMLAdapter
from src.xml_to_mathml.services.error_handler import ErrorHandler
from src.xml_to_mathml.services.xml_elements_to_mathml_element import ElementsToMathMLAdapter


def make_xml_to_mathml_adapter() -> XmlToMathMLAdapter:
    xml_elements_to_mathml_element_adapter = ElementsToMathMLAdapter()
    error_handler = ErrorHandler()

    return XmlToMathMLAdapter(xml_elements_to_mathml_element_adapter, error_handler)