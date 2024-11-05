from src.mathml_to_tex.protocols import MathMLElement, VoidMathMLElement
from .usecases import Void, MI, MO, MN, Math, MSup, GenericSpacingWrapper, MSqrt, MFenced, MTable, MTr


class MathMLElementToLatexConverterAdapter:
    def to_latex_converter(self, mathml_element: MathMLElement):
        name = mathml_element.name or VoidMathMLElement().name
        converter = self._from_mathml_element_to_latex_converter().get(name, self._make_generic_spacing_wrapper)

        return converter(mathml_element)

    def _from_mathml_element_to_latex_converter(self):
        return {
            'math': self._make_math_tag_converter,
            'mi': MI,
            'mo': MO,
            'mn': MN,
            'msqrt': self._make_msqrt_tag_converter,
            'mfenced': self._make_mfenced_tag_converter,
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
            'mtable': self._make_mtable_tag_converter,
            'mtr': self._make_mtr_tag_converter,
            # 'mover': ToLatexConverters.GenericUnderOver,
            # 'munder': ToLatexConverters.GenericUnderOver,
            'mrow': self._make_generic_spacing_wrapper,
            # 'mpadded': ToLatexConverters.GenericSpacingWrapper,
        }

    def _make_math_tag_converter(self, math_element: MathMLElement) -> Math:
        return Math(math_element, self)

    def _make_msup_tag_converter(self, math_element: MathMLElement) -> MSup:
        return MSup(math_element, self)

    def _make_msqrt_tag_converter(self, math_element: MathMLElement) -> MSqrt:
        return MSqrt(math_element, self)

    def _make_mfenced_tag_converter(self, math_element: MathMLElement) -> MFenced:
        return MFenced(math_element, self)

    def _make_mtable_tag_converter(self, math_element: MathMLElement) -> MTable:
        return MTable(math_element, self)

    def _make_mtr_tag_converter(self, math_element: MathMLElement) -> MTr:
        return MTr(math_element, self)

    def _make_generic_spacing_wrapper(self, math_element: MathMLElement) -> GenericSpacingWrapper:
        return GenericSpacingWrapper(math_element, self)