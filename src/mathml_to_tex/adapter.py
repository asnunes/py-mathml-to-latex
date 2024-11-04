from src.mathml_to_tex.protocols import MathMLElement
from .usecases import Void, MI, MO, MN, Math, MSup, GenericSpacingWrapper


class MathMLElementToLatexConverterAdapter:
    def to_latex_converter(self, mathml_element: MathMLElement):
        name = mathml_element.name
        converter = self._from_mathml_element_to_latex_converter().get(name, Void)

        return converter(mathml_element)

    def _from_mathml_element_to_latex_converter(self):
        return {
            'math': self._make_math_tag_converter,
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
            'msup': self._make_msup_tag_converter,
            # 'msub': ToLatexConverters.MSub,
            # 'msubsup': ToLatexConverters.MSubsup,
            # 'mmultiscripts': ToLatexConverters.MMultiscripts,
            # 'mtext': ToLatexConverters.MText,
            # 'munderover': ToLatexConverters.MUnderover,
            # 'mtable': ToLatexConverters.MTable,
            # 'mtr': ToLatexConverters.MTr,
            # 'mover': ToLatexConverters.GenericUnderOver,
            # 'munder': ToLatexConverters.GenericUnderOver,
            'mrow': self._make_generic_spacing_wrapper,
            # 'mpadded': ToLatexConverters.GenericSpacingWrapper,
        }

    def _make_math_tag_converter(self, math_element: MathMLElement) -> Math:
        return Math(math_element, self)

    def _make_msup_tag_converter(self, math_element: MathMLElement) -> MSup:
        return MSup(math_element, self)

    def _make_generic_spacing_wrapper(self, math_element: MathMLElement) -> GenericSpacingWrapper:
        return GenericSpacingWrapper(math_element, self)