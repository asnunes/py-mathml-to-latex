from .el_to_tex.adapter import MathMLElementToLatexConverterAdapter
from .xml_to_mathml.factory import make_xml_to_mathml_adapter


class MathMLToLaTeX:
    @staticmethod
    def convert(mathml: str) -> str:
        mathml_elements = make_xml_to_mathml_adapter().convert(mathml)
        mathml_elements_to_latex_converters = [
            MathMLElementToLatexConverterAdapter().to_latex_converter(mathml_element)
            for mathml_element in mathml_elements
        ]
        return "".join(
            [
                to_latex_converters.convert()
                for to_latex_converters in mathml_elements_to_latex_converters
            ]
        ).strip()
