from typing import Optional, List

from src.syntax import HashUTF8ToLtXConverter, all_math_symbols_by_char, all_math_symbols_by_glyph, math_number_by_glyph, \
    all_math_operators_by_char, all_math_operators_by_glyph
from .protocols import ToLaTeXConverter, MathMLElement, InvalidNumberOfChildrenError
from .services.normalizer import WhiteSpaceNormalizer
from .services.wrapper import ParenthesisWrapper, BracketWrapper, GenericWrapper, JoinWithManySeparators


class Math(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement, adapter):
        self._white_space_normalizer = WhiteSpaceNormalizer()
        self._adapter = adapter
        self._math_element = math_element

    def convert(self) -> str:
        raw_tex = ' '.join([self._adapter.to_latex_converter(child).convert() for child in self._math_element.children])
        return self._white_space_normalizer.normalize(raw_tex)

class Void(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement):
        self._math_element = math_element

    def convert(self) -> str:
        return ''

class MI(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement):
        self._utf8_converter = HashUTF8ToLtXConverter()
        self._normalizer = WhiteSpaceNormalizer()
        self._math_element = math_element

    def convert(self) -> str:
        normalized_value = self._normalizer.normalize(self._math_element.value)
        if normalized_value == ' ':
            return Character.apply(normalized_value)

        trimmed_value = normalized_value.strip()
        converted_char = Character.apply(trimmed_value)

        parsed_char = self._utf8_converter.convert(converted_char)
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
        self._normalizer = WhiteSpaceNormalizer()
        self._math_element = math_element

    def convert(self) -> str:
        normalized_value = self._normalizer.normalize(self._math_element.value).strip()
        converted_value = math_number_by_glyph.get(normalized_value, '')

        return converted_value or normalized_value

# export class MSup implements ToLaTeXConverter {
#   private readonly _mathmlElement: MathMLElement;
#
#   constructor(mathElement: MathMLElement) {
#     this._mathmlElement = mathElement;
#   }
#
#   convert(): string {
#     const { name, children } = this._mathmlElement;
#     const childrenLength = children.length;
#
#     if (childrenLength !== 2) throw new InvalidNumberOfChildrenError(name, 2, childrenLength);
#
#     const baseChild = children[0];
#     const exponentChild = children[1];
#
#     return `${this._handleBaseChild(baseChild)}^${this._handleExponentChild(exponentChild)}`;
#   }
#
#   private _handleBaseChild(base: MathMLElement): string {
#     const baseChildren = base.children;
#     const baseStr = mathMLElementToLaTeXConverter(base).convert();
#
#     if (baseChildren.length <= 1) {
#       return baseStr;
#     }
#
#     return new ParenthesisWrapper().wrapIfMoreThanOneChar(baseStr);
#   }
#
#   private _handleExponentChild(exponent: MathMLElement): string {
#     const exponentStr = mathMLElementToLaTeXConverter(exponent).convert();
#
#     return new BracketWrapper().wrap(exponentStr);
#   }
# }

class MSup(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement, adapter):
        self._math_element = math_element
        self._adapter = adapter
        self._parenthesis_wrapper = ParenthesisWrapper()
        self._bracket_wrapper = BracketWrapper()

    def convert(self) -> str:
        name = self._math_element.name
        children = self._math_element.children
        children_length = len(children)

        if children_length != 2:
            raise InvalidNumberOfChildrenError(name, 2, children_length)

        base_child = children[0]
        exponent_child = children[1]

        return f'{self._handle_base_child(base_child)}^{self._handle_exponent_child(exponent_child)}'

    def _handle_base_child(self, base: MathMLElement) -> str:
        base_children = base.children
        base_str = self._adapter.to_latex_converter(base).convert()

        if len(base_children) <= 1:
            return base_str

        return self._parenthesis_wrapper.wrap_if_more_than_one_char(base_str)

    def _handle_exponent_child(self, exponent: MathMLElement) -> str:
        exponent_str = self._adapter.to_latex_converter(exponent).convert()

        return self._bracket_wrapper.wrap(exponent_str)


# export class GenericSpacingWrapper implements ToLaTeXConverter {
#   private readonly _mathmlElement: MathMLElement;
#
#   constructor(mathElement: MathMLElement) {
#     this._mathmlElement = mathElement;
#   }
#
#   convert(): string {
#     return this._mathmlElement.children
#       .map((child) => mathMLElementToLaTeXConverter(child))
#       .map((converter) => converter.convert())
#       .join(' ');
#   }
# }

class GenericSpacingWrapper(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement, adapter):
        self._math_element = math_element
        self._adapter = adapter

    def convert(self) -> str:
        return ' '.join([self._adapter.to_latex_converter(child).convert() for child in self._math_element.children])

# export class MSqrt implements ToLaTeXConverter {
#   private readonly _mathmlElement: MathMLElement;
#
#   constructor(mathElement: MathMLElement) {
#     this._mathmlElement = mathElement;
#   }
#
#   convert(): string {
#     const latexJoinedChildren = this._mathmlElement.children
#       .map((child) => mathMLElementToLaTeXConverter(child))
#       .map((converter) => converter.convert())
#       .join(' ');
#
#     return `\\sqrt{${latexJoinedChildren}}`;
#   }
# }

class MSqrt(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement, adapter):
        self._math_element = math_element
        self._adapter = adapter

    def convert(self) -> str:
        latex_joined_children = ' '.join([self._adapter.to_latex_converter(child).convert() for child in self._math_element.children])

        return f'\\sqrt{{{latex_joined_children}}}'

class Separators:
    def __init__(self, op: str, close: str):
        self._open = op
        self._close = close

    def wrap(self, string: str) -> str:
        return GenericWrapper(self._open, self._close).wrap(string)

    def are_parentheses(self) -> bool:
        return self._compare('(', ')')

    def are_square_brackets(self) -> bool:
        return self._compare('[', ']')

    def are_brackets(self) -> bool:
        return self._compare('{', '}')

    def are_divides(self) -> bool:
        return self._compare('|', '|')

    def are_parallels(self) -> bool:
        return self._compare('||', '||')

    def are_not_equal(self) -> bool:
        return self._open != self._close

    def _compare(self, open_to_compare: str, close_to_compare: str) -> bool:
        return self._open == open_to_compare and self._close == close_to_compare


class Vector:
    def __init__(self, op: str, close: str, separators: List[str]):
        self._open = op if op != '' else '('
        self._close = close if close != '' else ')'
        self._separators = separators

    def apply(self, latex_contents):
        content_without_wrapper = JoinWithManySeparators(self._separators).join(latex_contents)
        return GenericWrapper(self._open, self._close).wrap(content_without_wrapper)

class Matrix:
    def __init__(self, op: str, close: str):
        self._separators = Separators(op, close)
        self._generic_command = 'matrix'

    def apply(self, latex_contents):
        command = self._command
        matrix = f'\\begin{{{command}}}\n{"".join(latex_contents)}\n\\end{{{command}}}'

        return self._separators.wrap(matrix) if command == self._generic_command else matrix

    @property
    def _command(self):
        if self._separators.are_parentheses():
            return 'pmatrix'
        if self._separators.are_square_brackets():
            return 'bmatrix'
        if self._separators.are_brackets():
            return 'Bmatrix'
        if self._separators.are_divides():
            return 'vmatrix'
        if self._separators.are_parallels():
            return 'Vmatrix'
        if self._separators.are_not_equal():
            return self._generic_command
        return 'bmatrix'

class MFenced(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement, adapter):
        self._math_element = math_element
        self._adapter = adapter
        self._open = self._math_element.attributes.get('open', '')
        self._close = self._math_element.attributes.get('close', '')
        self._separators = list(self._math_element.attributes.get('separators', ''))

    def convert(self) -> str:
        latex_children = [self._adapter.to_latex_converter(child).convert() for child in self._math_element.children]

        if self._is_there_relative_of_name(self._math_element.children, 'mtable'):
            return Matrix(self._open, self._close).apply(latex_children)

        return Vector(self._open, self._close, self._separators).apply(latex_children)

    def _is_there_relative_of_name(self, mathml_elements, element_name):
        return any([child.name == element_name or self._is_there_relative_of_name(child.children, element_name) for child in mathml_elements])

# export class MTable implements ToLaTeXConverter {
#   private readonly _mathmlElement: MathMLElement;
#
#   constructor(mathElement: MathMLElement) {
#     this._mathmlElement = mathElement;
#     this._addFlagRecursiveIfName(this._mathmlElement.children, 'mtable', 'innerTable');
#   }
#
#   convert(): string {
#     const tableContent = this._mathmlElement.children
#       .map((child) => mathMLElementToLaTeXConverter(child))
#       .map((converter) => converter.convert())
#       .join(' \\\\\n');
#
#     return this._hasFlag('innerTable') ? this._wrap(tableContent) : tableContent;
#   }
#
#   private _wrap(latex: string): string {
#     return `\\begin{matrix}${latex}\\end{matrix}`;
#   }
#
#   private _addFlagRecursiveIfName(mathmlElements: MathMLElement[], name: string, flag: string): void {
#     mathmlElements.forEach((mathmlElement) => {
#       if (mathmlElement.name === name) mathmlElement.attributes[flag] = flag;
#       this._addFlagRecursiveIfName(mathmlElement.children, name, flag);
#     });
#   }
#
#   private _hasFlag(flag: string): boolean {
#     return !!this._mathmlElement.attributes[flag];
#   }
# }

class MTable(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement, adapter):
        self._math_element = math_element
        self._adapter = adapter
        self._add_flag_recursive_if_name(self._math_element.children, 'mtable', 'innerTable')

    def convert(self) -> str:
        table_content = ' \\\\\n'.join([self._adapter.to_latex_converter(child).convert() for child in self._math_element.children])

        return self._wrap(table_content) if self._has_flag('innerTable') else table_content

    def _wrap(self, latex: str) -> str:
        return f'\\begin{{matrix}}{latex}\\end{{matrix}}'

    def _add_flag_recursive_if_name(self, mathml_elements, name, flag):
        for mathml_element in mathml_elements:
            if mathml_element.name == name:
                mathml_element.attributes[flag] = flag
            self._add_flag_recursive_if_name(mathml_element.children, name, flag)

    def _has_flag(self, flag: str) -> bool:
        return bool(self._math_element.attributes.get(flag))

# export class MTr implements ToLaTeXConverter {
#   private readonly _mathmlElement: MathMLElement;
#
#   constructor(mathElement: MathMLElement) {
#     this._mathmlElement = mathElement;
#   }
#
#   convert(): string {
#     return this._mathmlElement.children
#       .map((child) => mathMLElementToLaTeXConverter(child))
#       .map((converter) => converter.convert())
#       .join(' & ');
#   }
# }

class MTr(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement, adapter):
        self._math_element = math_element
        self._adapter = adapter

    def convert(self) -> str:
        return ' & '.join([self._adapter.to_latex_converter(child).convert() for child in self._math_element.children])

# export class MSub implements ToLaTeXConverter {
#   private readonly _mathmlElement: MathMLElement;
#
#   constructor(mathElement: MathMLElement) {
#     this._mathmlElement = mathElement;
#   }
#
#   convert(): string {
#     const { name, children } = this._mathmlElement;
#     const childrenLength = children.length;
#
#     if (childrenLength !== 2) throw new InvalidNumberOfChildrenError(name, 2, childrenLength);
#
#     const baseChild = children[0];
#     const subscriptChild = children[1];
#
#     return `${this._handleBaseChild(baseChild)}_${this._handleSubscriptChild(subscriptChild)}`;
#   }
#
#   private _handleBaseChild(base: MathMLElement): string {
#     const baseChildren = base.children;
#     const baseStr = mathMLElementToLaTeXConverter(base).convert();
#
#     if (baseChildren.length <= 1) {
#       return baseStr;
#     }
#
#     return new ParenthesisWrapper().wrapIfMoreThanOneChar(baseStr);
#   }
#
#   private _handleSubscriptChild(subscript: MathMLElement): string {
#     const subscriptStr = mathMLElementToLaTeXConverter(subscript).convert();
#
#     return new BracketWrapper().wrap(subscriptStr);
#   }
# }

class MSub(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement, adapter):
        self._math_element = math_element
        self._adapter = adapter
        self._parenthesis_wrapper = ParenthesisWrapper()
        self._bracket_wrapper = BracketWrapper()

    def convert(self) -> str:
        name = self._math_element.name
        children = self._math_element.children
        children_length = len(children)

        if children_length != 2:
            raise InvalidNumberOfChildrenError(name, 2, children_length)

        base_child = children[0]
        subscript_child = children[1]

        return f'{self._handle_base_child(base_child)}_{self._handle_subscript_child(subscript_child)}'

    def _handle_base_child(self, base: MathMLElement) -> str:
        base_children = base.children
        base_str = self._adapter.to_latex_converter(base).convert()

        if len(base_children) <= 1:
            return base_str

        return self._parenthesis_wrapper.wrap_if_more_than_one_char(base_str)

    def _handle_subscript_child(self, subscript: MathMLElement) -> str:
        subscript_str = self._adapter.to_latex_converter(subscript).convert()

        return self._bracket_wrapper.wrap(subscript_str)

# export class MFrac implements ToLaTeXConverter {
#   private readonly _mathmlElement: MathMLElement;
#
#   constructor(mathElement: MathMLElement) {
#     this._mathmlElement = mathElement;
#   }
#
#   convert(): string {
#     const { children, name } = this._mathmlElement;
#     const childrenLength = children.length;
#
#     if (childrenLength !== 2) throw new InvalidNumberOfChildrenError(name, 2, childrenLength);
#
#     const num = mathMLElementToLaTeXConverter(children[0]).convert();
#     const den = mathMLElementToLaTeXConverter(children[1]).convert();
#
#     if (this._isBevelled()) return `${this._wrapIfMoreThanOneChar(num)}/${this._wrapIfMoreThanOneChar(den)}`;
#
#     return `\\frac{${num}}{${den}}`;
#   }
#
#   private _wrapIfMoreThanOneChar(str: string): string {
#     return new ParenthesisWrapper().wrapIfMoreThanOneChar(str);
#   }
#
#   private _isBevelled(): boolean {
#     return !!this._mathmlElement.attributes.bevelled;
#   }
# }

class MFrac(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement, adapter):
        self._math_element = math_element
        self._adapter = adapter
        self._parenthesis_wrapper = ParenthesisWrapper()

    def convert(self) -> str:
        children = self._math_element.children
        name = self._math_element.name
        children_length = len(children)

        if children_length != 2:
            raise InvalidNumberOfChildrenError(name, 2, children_length)

        num = self._adapter.to_latex_converter(children[0]).convert()
        den = self._adapter.to_latex_converter(children[1]).convert()

        if self._is_bevelled():
            return f'{self._wrap_if_more_than_one_char(num)}/{self._wrap_if_more_than_one_char(den)}'

        return f'\\frac{{{num}}}{{{den}}}'

    def _wrap_if_more_than_one_char(self, val: str) -> str:
        return self._parenthesis_wrapper.wrap_if_more_than_one_char(val)

    def _is_bevelled(self) -> bool:
        return bool(self._math_element.attributes.get('bevelled'))

# export class MRoot implements ToLaTeXConverter {
#   private readonly _mathmlElement: MathMLElement;
#
#   constructor(mathElement: MathMLElement) {
#     this._mathmlElement = mathElement;
#   }
#
#   convert(): string {
#     const { name, children } = this._mathmlElement;
#     const childrenLength = children.length;
#
#     if (childrenLength !== 2) throw new InvalidNumberOfChildrenError(name, 2, childrenLength);
#
#     const content = mathMLElementToLaTeXConverter(children[0]).convert();
#     const rootIndex = mathMLElementToLaTeXConverter(children[1]).convert();
#
#     return `\\sqrt[${rootIndex}]{${content}}`;
#   }
# }

class MRoot(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement, adapter):
        self._math_element = math_element
        self._adapter = adapter

    def convert(self) -> str:
        name = self._math_element.name
        children = self._math_element.children
        children_length = len(children)

        if children_length != 2:
            raise InvalidNumberOfChildrenError(name, 2, children_length)

        content = self._adapter.to_latex_converter(children[0]).convert()
        root_index = self._adapter.to_latex_converter(children[1]).convert()

        return f'\\sqrt[{root_index}]{{{content}}}'

# export class MAction implements ToLaTeXConverter {
#   private readonly _mathmlElement: MathMLElement;
#
#   constructor(mathElement: MathMLElement) {
#     this._mathmlElement = mathElement;
#   }
#
#   convert(): string {
#     const { children } = this._mathmlElement;
#
#     if (this._isToggle())
#       return children
#         .map((child) => mathMLElementToLaTeXConverter(child))
#         .map((converter) => converter.convert())
#         .join(' \\Longrightarrow ');
#
#     return mathMLElementToLaTeXConverter(children[0]).convert();
#   }
#
#   private _isToggle(): boolean {
#     const { actiontype } = this._mathmlElement.attributes;
#     return actiontype === 'toggle' || !actiontype;
#   }
# }

class MAction(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement, adapter):
        self._math_element = math_element
        self._adapter = adapter

    def convert(self) -> str:
        children = self._math_element.children

        if self._is_toggle():
            return ' \\Longrightarrow '.join([self._adapter.to_latex_converter(child).convert() for child in children])

        return self._adapter.to_latex_converter(children[0]).convert()

    def _is_toggle(self) -> bool:
        action_type = self._math_element.attributes.get('actiontype')
        return action_type == 'toggle' or not action_type

# export class MEnclose implements ToLaTeXConverter {
#   private readonly _mathmlElement: MathMLElement;
#
#   constructor(mathElement: MathMLElement) {
#     this._mathmlElement = mathElement;
#   }
#
#   convert(): string {
#     const latexJoinedChildren = this._mathmlElement.children
#       .map((child) => mathMLElementToLaTeXConverter(child))
#       .map((converter) => converter.convert())
#       .join(' ');
#
#     if (this._notation === 'actuarial') return `\\overline{\\left.${latexJoinedChildren}\\right|}`;
#     if (this._notation === 'radical') return `\\sqrt{${latexJoinedChildren}}`;
#     if (['box', 'roundedbox', 'circle'].includes(this._notation)) return `\\boxed{${latexJoinedChildren}}`;
#     if (this._notation === 'left') return `\\left|${latexJoinedChildren}`;
#     if (this._notation === 'right') return `${latexJoinedChildren}\\right|`;
#     if (this._notation === 'top') return `\\overline{${latexJoinedChildren}}`;
#     if (this._notation === 'bottom') return `\\underline{${latexJoinedChildren}}`;
#     if (this._notation === 'updiagonalstrike') return `\\cancel{${latexJoinedChildren}}`;
#     if (this._notation === 'downdiagonalstrike') return `\\bcancel{${latexJoinedChildren}}`;
#     if (this._notation === 'updiagonalarrow') return `\\cancelto{}{${latexJoinedChildren}}`;
#     if (['verticalstrike', 'horizontalstrike'].includes(this._notation)) return `\\hcancel{${latexJoinedChildren}}`;
#     if (this._notation === 'madruwb') return `\\underline{${latexJoinedChildren}\\right|}`;
#     if (this._notation === 'phasorangle') return `{\\angle \\underline{${latexJoinedChildren}}}`;
#
#     return `\\overline{\\left.\\right)${latexJoinedChildren}}`;
#   }
#
#   private get _notation(): string {
#     return this._mathmlElement.attributes.notation || 'longdiv';
#   }
# }

class MEnclose(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement, adapter):
        self._math_element = math_element
        self._adapter = adapter
        self._notation = self._math_element.attributes.get('notation', 'longdiv')

    def convert(self) -> str:
        latex_joined_children = ' '.join([self._adapter.to_latex_converter(child).convert() for child in self._math_element.children])

        if self._notation == 'actuarial':
            return f'\\overline{{\\left.{latex_joined_children}\\right|}}'
        if self._notation == 'radical':
            return f'\\sqrt{{{latex_joined_children}}}'
        if self._notation in ['box', 'roundedbox', 'circle']:
            return f'\\boxed{{{latex_joined_children}}}'
        if self._notation == 'left':
            return f'\\left|{latex_joined_children}'
        if self._notation == 'right':
            return f'{latex_joined_children}\\right|'
        if self._notation == 'top':
            return f'\\overline{{{latex_joined_children}}}'
        if self._notation == 'bottom':
            return f'\\underline{{{latex_joined_children}}}'
        if self._notation == 'updiagonalstrike':
            return f'\\cancel{{{latex_joined_children}}}'
        if self._notation == 'downdiagonalstrike':
            return f'\\bcancel{{{latex_joined_children}}}'
        if self._notation == 'updiagonalarrow':
            return f'\\cancelto{{}}{{{latex_joined_children}}}'
        if self._notation in ['verticalstrike', 'horizontalstrike']:
            return f'\\hcancel{{{latex_joined_children}}}'
        if self._notation == 'madruwb':
            return f'\\underline{{{latex_joined_children}\\right|}}'
        if self._notation == 'phasorangle':
            return f'{{\\angle \\underline{{{latex_joined_children}}}}}'
        return f'\\overline{{\\left.\\right){latex_joined_children}}}'

# export class MError implements ToLaTeXConverter {
#   private readonly _mathmlElement: MathMLElement;
#
#   constructor(mathElement: MathMLElement) {
#     this._mathmlElement = mathElement;
#   }
#
#   convert(): string {
#     const latexJoinedChildren = this._mathmlElement.children
#       .map((child) => mathMLElementToLaTeXConverter(child))
#       .map((converter) => converter.convert())
#       .join(' ');
#
#     return `\\color{red}{${latexJoinedChildren}}`;
#   }
# }

class MError(ToLaTeXConverter):
    def __init__(self, math_element: MathMLElement, adapter):
        self._math_element = math_element
        self._adapter = adapter

    def convert(self) -> str:
        latex_joined_children = ' '.join([self._adapter.to_latex_converter(child).convert() for child in self._math_element.children])

        return f'\\color{{red}}{{{latex_joined_children}}}'





