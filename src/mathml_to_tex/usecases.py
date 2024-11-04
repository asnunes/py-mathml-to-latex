from typing import Optional

from src.syntax import HashUTF8ToLtXConverter, all_math_symbols_by_char, all_math_symbols_by_glyph, math_number_by_glyph, \
    all_math_operators_by_char, all_math_operators_by_glyph
from .protocols import ToLaTeXConverter, MathMLElement
from .services.normalizer import WhiteSpaceNormalizer

class Void(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement):
        self._math_element = math_element

    def convert(self) -> str:
        return ''

class MI(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement):
        self.utf8_converter = HashUTF8ToLtXConverter()
        self.normalizer = WhiteSpaceNormalizer()
        self._math_element = math_element

    def convert(self) -> str:
        normalized_value = self.normalizer.normalize(self._math_element.value)
        if normalized_value == ' ':
            return Character.apply(normalized_value)

        trimmed_value = normalized_value.strip()
        converted_char = Character.apply(trimmed_value)

        parsed_char = self.utf8_converter.convert(converted_char)
        if parsed_char != converted_char:
            return parsed_char

        return self._wrap_in_math_variant(converted_char, self._get_math_variant(self._math_element.attributes))

    def _get_math_variant(self, attributes: dict) -> str:
        if not attributes or 'mathvariant' not in attributes:
            return ''
        return attributes['mathvariant']

    def _wrap_in_math_variant(self, value: str, math_variant: str) -> str:
        if math_variant == 'bold':
            return f'\\mathbf{{{value}}}'
        if math_variant == 'italic':
            return f'\\mathit{{{value}}}'
        if math_variant == 'bold-italic':
            return f'\\mathbf{{\\mathit{{{value}}}}}'
        if math_variant == 'double-struck':
            return f'\\mathbb{{{value}}}'
        if math_variant == 'bold-fraktur':
            return f'\\mathbf{{\\mathfrak{{{value}}}}}'
        if math_variant == 'script':
            return f'\\mathcal{{{value}}}'
        if math_variant == 'bold-script':
            return f'\\mathbf{{\\mathcal{{{value}}}}}'
        if math_variant == 'fraktur':
            return f'\\mathfrak{{{value}}}'
        if math_variant == 'sans-serif':
            return f'\\mathsf{{{value}}}'
        if math_variant == 'bold-sans-serif':
            return f'\\mathbf{{\\mathsf{{{value}}}}}'
        if math_variant == 'sans-serif-italic':
            return f'\\mathsf{{\\mathit{{{value}}}}}'
        if math_variant == 'sans-serif-bold-italic':
            return f'\\mathbf{{\\mathsf{{\\mathit{{{value}}}}}}}'
        if math_variant == 'monospace':
            return f'\\mathtt{{{value}}}'
        return value

class Character:
    def __init__(self, value: str):
        self.value = value

    @staticmethod
    def apply(value: str) -> str:
        return Character(value)._apply()

    def _apply(self) -> str:
        return self._find_by_character() or self._find_by_glyph() or self._find_by_number() or HashUTF8ToLtXConverter().convert(self.value)

    def _find_by_character(self) -> str:
        return all_math_symbols_by_char.get(self.value, '')

    def _find_by_glyph(self) -> str:
        return all_math_symbols_by_glyph.get(self.value, '')

    def _find_by_number(self) -> str:
        return math_number_by_glyph.get(self.value, '')

class MO(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement):
        self.normalizer = WhiteSpaceNormalizer()
        self._math_element = math_element

    def convert(self) -> str:
        normalized_value = self.normalizer.normalize(self._math_element.value)
        trimmed_value = normalized_value.strip()

        return Operator.operate(trimmed_value)


class Operator:
    def __init__(self, value: str):
        self._value = value

    @staticmethod
    def operate(value: str) -> str:
        return Operator(value)._operate()

    def _operate(self) -> str:
        # Attempt to find the LaTeX command by character
        latex_command = self._find_by_character()
        if latex_command:
            return latex_command

        # Attempt to find the LaTeX command by glyph
        latex_command = self._find_by_glyph()
        if latex_command:
            return latex_command

        # Attempt to find the LaTeX command by number
        latex_command = self._find_by_number()
        if latex_command:
            return latex_command

        # Fallback to converting using HashUTF8ToLtXConverter
        return HashUTF8ToLtXConverter().convert(self._value)

    def _find_by_character(self) -> Optional[str]:
        return all_math_operators_by_char.get(self._value)

    def _find_by_glyph(self) -> Optional[str]:
        return all_math_operators_by_glyph.get(self._value)

    def _find_by_number(self) -> Optional[str]:
        return math_number_by_glyph.get(self._value)


class MN(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement):
        self.normalizer = WhiteSpaceNormalizer()
        self._math_element = math_element

    def convert(self) -> str:
        normalized_value = self.normalizer.normalize(self._math_element.value).strip()
        converted_value = math_number_by_glyph.get(normalized_value, '')

        return converted_value or normalized_value