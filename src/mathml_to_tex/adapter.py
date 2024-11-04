from src.mathml_to_tex.protocols import MathMLElement, ToLaTeXConverter
from .services.normalizer import WhiteSpaceNormalizer
from .usecases import Void, MI, MO, MN

class MathMLElementToLatexConverterAdapter:
    def to_latex_converter(self, mathml_element: MathMLElement):
        name = mathml_element.name
        converter = self._from_mathml_element_to_latex_converter().get(name, Void)

        return converter(mathml_element)

    def _from_mathml_element_to_latex_converter(self):
        return {
            'math': Math,
            'mi': MI,
            'mo': MO,
            'mn': MN,
            # 'msqrt': ToLatexConverters.MSqrt,
            # 'mfenced': ToLatexConverters.MFenced,
            # 'mfrac': ToLatexConverters.MFrac,
            # 'mroot': ToLatexConverters.MRoot,
            # 'maction': ToLatexConverters.MAction,
            # 'menclose': ToLatexConverters.MEnclose,
            # 'merror': ToLatexConverters.MError,
            # 'mphantom': ToLatexConverters.MPhantom,
            # 'msup': ToLatexConverters.MSup,
            # 'msub': ToLatexConverters.MSub,
            # 'msubsup': ToLatexConverters.MSubsup,
            # 'mmultiscripts': ToLatexConverters.MMultiscripts,
            # 'mtext': ToLatexConverters.MText,
            # 'munderover': ToLatexConverters.MUnderover,
            # 'mtable': ToLatexConverters.MTable,
            # 'mtr': ToLatexConverters.MTr,
            # 'mover': ToLatexConverters.GenericUnderOver,
            # 'munder': ToLatexConverters.GenericUnderOver,
            # 'mrow': ToLatexConverters.GenericSpacingWrapper,
            # 'mpadded': ToLatexConverters.GenericSpacingWrapper,
            # 'void': ToLatexConverters.Void,
        }

class Math(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement):
        self.white_space_normalizer = WhiteSpaceNormalizer()
        self.adapter = MathMLElementToLatexConverterAdapter()
        self._math_element = math_element

    def convert(self) -> str:
        raw_tex = ' '.join([self.adapter.to_latex_converter(child).convert() for child in self._math_element.children])
        return self.white_space_normalizer.normalize(raw_tex)
