import unittest

from src.main import MathMLToLaTeX
from src.mathml_to_tex.protocols import InvalidNumberOfChildrenError
from tests.mathml import (
    mi,
    mi_with_space,
    mi_with_double_struck,
    math_with_mi,
    math_with_mi_and_space,
    mi_with_especial_char,
    mo_with_simple_operator,
    mo_divider_operator,
    mo_with_glyph_operator,
    mo_with_char_operator,
    mo_with_char_operator_and_mi,
    mrow_with_mn_and_mo,
    msqrt,
    msqrt_with_wrapped_content,
    msqrt_with_mrow,
    empty_msqrt,
    mfenced_without_attribute,
    mfenced_with_open,
    mfenced_with_open_and_close,
    mfenced_with_broken_close,
    mfenced_with_wrapped_content,
    mfenced_with_empty_separator,
    mfenced_with_separator,
    mfenced_with_diff_separators,
    mfenced_as_bmatrix,
    mfenced_as_pmatrix,
    mfenced_as_vmatrix,
    mfenced_as_big_bmatrix,
    mfenced_as_big_vmatrix,
    mfenced_as_matrix,
    mfenced_as_partial_function,
    mfenced_with_nested_mtables,
    mfrac_with_three_children,
    short_m_frac,
    mfrac_with_mrow,
    mfrac,
    mroot,
    mroot_with_three_children,
    mpadded,
    maction,
    maction_with_mrow,
    maction_type_toggle,
    maction_type_statusline,
    maction_type_tooltip,
    menclose,
    menclose_notation_longdiv,
    menclose_notation_actuarial,
    menclose_notation_radical,
    menclose_notation_box,
    menclose_notation_rounded_box,
    menclose_notation_circle,
    menclose_notation_left,
    menclose_notation_right,
    menclose_notation_top,
    menclose_notation_bottom,
    menclose_notation_updiagnonalstrike,
    menclose_notation_horizontalstrike,
    menclose_notation_verticalstrike,
    menclose_notation_downdiagnonalstrike,
    menclose_notation_updiagnonalarrow,
    menclose_notation_madruwb,
    menclose_notation_phasorangle,
    merror,
    mglyph,
    mphantom,
    msup_with_mrow_on_top,
    msup_with_mrow_on_bottom,
    msup_with_mrow_on_top_bottom,
    msup_with_three_children,
    msup,
    msub,
    msub_with_mrow_on_bottom,
    msub_with_mrow_on_top,
    msub_with_mrow_on_top_bottom,
    msub_with_three_children,
    msubsup,
    msubsup_with_mrow,
    msubsup_with_four_children,
    mtext_normal,
    mtext_bold,
    mtext_italic,
    mtext_bold_italic,
    mtext_double_struck,
    mtext_fraktur,
    mtext_bold_fraktur,
    mtext_monospace,
    mtext_script,
    mtext_bold_script,
    mover_mrow,
    mover_encoded_mo,
    mover_double_mrow,
    mover_three_children,
    munder,
    munder_double_mrow,
    munder_encoded_mrow,
    munderover,
    munderover_encoded,
    munderover_with_three_children,
    mmultiscript,
    mmultiscript_no_super,
    mmultiscript_no_sub,
    mmultiscript_preset,
    mmultiscript_preset_with_none,
    mmultiscript_preset_only,
    mmultiscript_with_two_children,
)


class TestMathMLToLaTeX(unittest.TestCase):
    def setUp(self):
        self.converter = MathMLToLaTeX()

    def tearDown(self):
        del self.converter

    def test_convert_mi_to_simple_text_with_root(self):
        expected_latex = "a"

        result = self.converter.convert(mi)

        self.assertEqual(result, expected_latex)

    def test_convert_mi_to_simple_text_without_root(self):
        expected_latex = "b"

        result = self.converter.convert(math_with_mi)

        self.assertEqual(result, expected_latex)

    def test_add_space_between_mi_tags(self):
        expected_latex = "\\Delta x"

        result = self.converter.convert(mi_with_space)

        self.assertEqual(result, expected_latex)

    def test_convert_mi_with_double_struck_attribute(self):
        expected_latex = "\\mathbb{R}^{n}"

        result = self.converter.convert(mi_with_double_struck)

        self.assertEqual(result, expected_latex)

    def test_convert_mi_with_space(self):
        expected_latex = "a"

        result = self.converter.convert(math_with_mi_and_space)

        self.assertEqual(result, expected_latex)

    def test_convert_mi_with_special_char_to_tex(self):
        expected_latex = "\\infty"

        result = self.converter.convert(mi_with_especial_char)

        self.assertEqual(result, expected_latex)

    def test_add_space_between_mis(self):
        expected_latex = "\\Delta x"
        result = self.converter.convert(mi_with_space)
        self.assertEqual(result, expected_latex)

    def test_convert_mo_to_simple_operator(self):
        expected_latex = "+"
        result = self.converter.convert(mo_with_simple_operator)
        self.assertEqual(result, expected_latex)

    def test_convert_mo_divider_operator(self):
        expected_latex = "x = 4 / 5"
        result = self.converter.convert(mo_divider_operator)
        self.assertEqual(result, expected_latex)

    def test_convert_mo_with_glyph_operator(self):
        expected_latex = "\\star"
        result = self.converter.convert(mo_with_glyph_operator)
        self.assertEqual(result, expected_latex)

    def test_convert_mo_with_char_operator(self):
        expected_latex = "b"
        result = self.converter.convert(mo_with_char_operator)
        self.assertEqual(result, expected_latex)

    def test_convert_mo_with_char_operator_and_mi(self):
        expected_latex = "a \\Rightarrow b"
        result = self.converter.convert(mo_with_char_operator_and_mi)
        self.assertEqual(result, expected_latex)

    def test_convert_mrow_wrapping_content(self):
        expected_latex = "2 + 2"
        result = self.converter.convert(mrow_with_mn_and_mo)
        self.assertEqual(result, expected_latex)

    def test_convert_msqrt_single_child(self):
        expected_latex = "\\sqrt{2}"
        result = self.converter.convert(msqrt)
        self.assertEqual(result, expected_latex)

    def test_convert_msqrt_with_wrapped_content(self):
        expected_latex = "\\sqrt{2 + 2}"
        result = self.converter.convert(msqrt_with_wrapped_content)
        self.assertEqual(result, expected_latex)

    def test_convert_msqrt_with_mrow(self):
        expected_latex = "\\sqrt{2 + 2}"
        result = self.converter.convert(msqrt_with_mrow)
        self.assertEqual(result, expected_latex)

    def test_convert_empty_msqrt(self):
        expected_latex = "\\sqrt{}"
        result = self.converter.convert(empty_msqrt)
        self.assertEqual(result, expected_latex)

    def test_convert_mfenced_without_attribute(self):
        expected_latex = "\\left(3\\right)"
        result = self.converter.convert(mfenced_without_attribute)
        self.assertEqual(result, expected_latex)

    def test_convert_mfenced_with_open(self):
        expected_latex = "\\left{3\\right)"
        result = self.converter.convert(mfenced_with_open)
        self.assertEqual(result, expected_latex)

    def test_convert_mfenced_with_open_and_close(self):
        expected_latex = "\\left(3\\right)"
        result = self.converter.convert(mfenced_with_open_and_close)
        self.assertEqual(result, expected_latex)

    def test_convert_mfenced_with_broken_close(self):
        expected_latex = "\\left{3\\right)"
        result = self.converter.convert(mfenced_with_broken_close)
        self.assertEqual(result, expected_latex)

    def test_convert_mfenced_with_wrapped_content(self):
        expected_latex = "\\left(3,2,1\\right)"
        result = self.converter.convert(mfenced_with_wrapped_content)
        self.assertEqual(result, expected_latex)

    def test_convert_mfenced_with_empty_separator(self):
        expected_latex = "\\left(3,2,1,7\\right)"
        result = self.converter.convert(mfenced_with_empty_separator)
        self.assertEqual(result, expected_latex)

    def test_convert_mfenced_with_separator(self):
        expected_latex = "\\left(3;2;1\\right)"
        result = self.converter.convert(mfenced_with_separator)
        self.assertEqual(result, expected_latex)

    def test_convert_mfenced_with_diff_separators(self):
        expected_latex = "\\left(3;2.1.7\\right)"
        result = self.converter.convert(mfenced_with_diff_separators)
        self.assertEqual(result, expected_latex)

    def test_convert_mfenced_as_bmatrix(self):
        expected_latex = "A = \\begin{bmatrix} x & y \\\\ z & w \\end{bmatrix}"
        result = self.converter.convert(mfenced_as_bmatrix)
        self.assertEqual(result, expected_latex)

    def test_convert_mfenced_as_pmatrix(self):
        expected_latex = "A = \\begin{pmatrix} x & y \\\\ z & w \\end{pmatrix}"
        result = self.converter.convert(mfenced_as_pmatrix)
        self.assertEqual(result, expected_latex)

    def test_convert_mfenced_as_vmatrix(self):
        expected_latex = "A = \\begin{vmatrix} x & y \\\\ z & w \\end{vmatrix}"
        result = self.converter.convert(mfenced_as_vmatrix)
        self.assertEqual(result, expected_latex)

    def test_convert_mfenced_as_big_bmatrix(self):
        expected_latex = "A = \\begin{Bmatrix} x & y \\\\ z & w \\end{Bmatrix}"
        result = self.converter.convert(mfenced_as_big_bmatrix)
        self.assertEqual(result, expected_latex)

    def test_convert_mfenced_as_big_vmatrix(self):
        expected_latex = "A = \\begin{Vmatrix} x & y \\\\ z & w \\end{Vmatrix}"
        result = self.converter.convert(mfenced_as_big_vmatrix)
        self.assertEqual(result, expected_latex)

    def test_convert_mfenced_as_matrix(self):
        expected_latex = "A = \\begin{bmatrix} x & y \\\\ z & w \\end{bmatrix}"
        result = self.converter.convert(mfenced_as_matrix)
        self.assertEqual(result, expected_latex)

    def test_convert_mfenced_as_partial_function(self):
        expected_latex = "f \\left(x\\right) = \\left{\\begin{matrix} x^{2} , x < 0 \\\\ e^{x} , x \\geq 0 \\end{matrix}\\right"
        result = self.converter.convert(mfenced_as_partial_function)
        self.assertEqual(result, expected_latex)

    def test_convert_mfenced_with_nested_mtables(self):
        expected_latex = (
            "\\begin{bmatrix} \\begin{matrix}a_{11} & a_{12}\\end{matrix} & "
            "\\begin{matrix}\\ldots & \\ldots\\end{matrix} & a_{1 n} \\\\ "
            "\\begin{matrix}a_{21} & a_{22}\\end{matrix} & "
            "\\begin{matrix}\\ddots & \\end{matrix} & a_{2 n} \\\\ "
            "\\begin{matrix}\\begin{matrix}\\vdots & \\vdots\\end{matrix} \\\\ "
            "\\begin{matrix}a_{m 1} & a_{m 2}\\end{matrix}\\end{matrix} & "
            "\\begin{matrix}\\begin{matrix} & \\ddots\\end{matrix} \\\\ "
            "\\begin{matrix}\\ldots & \\ldots\\end{matrix}\\end{matrix} & "
            "\\begin{matrix}\\vdots \\\\ a_{m n}\\end{matrix} \\end{bmatrix}"
        )
        result = self.converter.convert(mfenced_with_nested_mtables)
        self.assertEqual(result, expected_latex)

    def test_convert_mfrac_simple(self):
        expected_latex = "\\frac{x}{3}"
        result = self.converter.convert(mfrac)
        self.assertEqual(result, expected_latex)

    def test_convert_mfrac_with_mrow(self):
        expected_latex = "\\frac{a + 2}{b - 3}"
        result = self.converter.convert(mfrac_with_mrow)
        self.assertEqual(result, expected_latex)

    def test_convert_short_m_frac(self):
        expected_latex = "1/\\left(x^{3} + 3\\right)"
        result = self.converter.convert(short_m_frac)
        self.assertEqual(result, expected_latex)

    def test_convert_mfrac_with_three_children(self):
        with self.assertRaises(InvalidNumberOfChildrenError):
            self.converter.convert(mfrac_with_three_children)

    def test_convert_mroot(self):
        expected_latex = "\\sqrt[3]{x + 2}"
        result = self.converter.convert(mroot)
        self.assertEqual(result, expected_latex)

    def test_convert_mroot_with_three_children(self):
        with self.assertRaises(InvalidNumberOfChildrenError):
            self.converter.convert(mroot_with_three_children)

    def test_convert_mpadded(self):
        expected_latex = "2 + 2"
        result = self.converter.convert(mpadded)
        self.assertEqual(result, expected_latex)

    def test_convert_maction_toggle(self):
        expected_latex = "a + 2 \\Longrightarrow b - 3"
        result = self.converter.convert(maction)
        self.assertEqual(result, expected_latex)

    def test_convert_maction_with_mrow(self):
        expected_latex = "a + 2 \\Longrightarrow b - 3 \\Longrightarrow a + b"
        result = self.converter.convert(maction_with_mrow)
        self.assertEqual(result, expected_latex)

    def test_convert_maction_type_toggle(self):
        expected_latex = "a + 2 \\Longrightarrow b - 3 \\Longrightarrow a + b"
        result = self.converter.convert(maction_type_toggle)
        self.assertEqual(result, expected_latex)

    def test_convert_maction_type_statusline(self):
        expected_latex = "a + 2"
        result = self.converter.convert(maction_type_statusline)
        self.assertEqual(result, expected_latex)

    def test_convert_maction_type_tooltip(self):
        expected_latex = "a + 2"
        result = self.converter.convert(maction_type_tooltip)
        self.assertEqual(result, expected_latex)

    def test_convert_menclose_default(self):
        expected_latex = "\\overline{\\left.\\right)a + 2}"
        result = self.converter.convert(menclose)
        self.assertEqual(result, expected_latex)

    def test_convert_menclose_longdiv(self):
        expected_latex = "\\overline{\\left.\\right)a + 2}"
        result = self.converter.convert(menclose_notation_longdiv)
        self.assertEqual(result, expected_latex)

    def test_convert_menclose_actuarial(self):
        expected_latex = "\\overline{\\left.a + 2\\right|}"
        result = self.converter.convert(menclose_notation_actuarial)
        self.assertEqual(result, expected_latex)

    def test_convert_menclose_radical(self):
        expected_latex = "\\sqrt{a + 2}"
        result = self.converter.convert(menclose_notation_radical)
        self.assertEqual(result, expected_latex)

    def test_convert_menclose_box(self):
        expected_latex = "\\boxed{E = m c^{2}}"
        result = self.converter.convert(menclose_notation_box)
        self.assertEqual(result, expected_latex)

    def test_convert_menclose_rounded_box(self):
        expected_latex = "\\boxed{E = m c^{2}}"
        result = self.converter.convert(menclose_notation_rounded_box)
        self.assertEqual(result, expected_latex)

    def test_convert_menclose_circle(self):
        expected_latex = "\\boxed{E = m c^{2}}"
        result = self.converter.convert(menclose_notation_circle)
        self.assertEqual(result, expected_latex)

    def test_convert_menclose_left(self):
        expected_latex = "\\left|E = m c^{2}"
        result = self.converter.convert(menclose_notation_left)
        self.assertEqual(result, expected_latex)

    def test_convert_menclose_right(self):
        expected_latex = "E = m c^{2}\\right|"
        result = self.converter.convert(menclose_notation_right)
        self.assertEqual(result, expected_latex)

    def test_convert_menclose_top(self):
        expected_latex = "\\overline{E = m c^{2}}"
        result = self.converter.convert(menclose_notation_top)
        self.assertEqual(result, expected_latex)

    def test_convert_menclose_bottom(self):
        expected_latex = "\\underline{a + 2}"
        result = self.converter.convert(menclose_notation_bottom)
        self.assertEqual(result, expected_latex)

    def test_convert_menclose_updiagnonalstrike(self):
        expected_latex = "\\cancel{a + 2}"
        result = self.converter.convert(menclose_notation_updiagnonalstrike)
        self.assertEqual(result, expected_latex)

    def test_convert_menclose_downdiagonalstrike(self):
        expected_latex = "\\bcancel{a + 2}"
        result = self.converter.convert(menclose_notation_downdiagnonalstrike)
        self.assertEqual(result, expected_latex)

    def test_convert_menclose_horizontalstrike(self):
        expected_latex = "\\hcancel{a + 2}"
        result = self.converter.convert(menclose_notation_horizontalstrike)
        self.assertEqual(result, expected_latex)

    def test_convert_menclose_verticalstrike(self):
        expected_latex = "\\hcancel{a + 2}"
        result = self.converter.convert(menclose_notation_verticalstrike)
        self.assertEqual(result, expected_latex)

    def test_convert_menclose_updiagnonalarrow(self):
        expected_latex = "\\cancelto{}{a + 2}"
        result = self.converter.convert(menclose_notation_updiagnonalarrow)
        self.assertEqual(result, expected_latex)

    def test_convert_menclose_madruwb(self):
        expected_latex = "\\underline{a + 2\\right|}"
        result = self.converter.convert(menclose_notation_madruwb)
        self.assertEqual(result, expected_latex)

    def test_convert_menclose_phasorangle(self):
        expected_latex = "{\\angle \\underline{a + 2}}"
        result = self.converter.convert(menclose_notation_phasorangle)
        self.assertEqual(result, expected_latex)

    def test_convert_merror(self):
        expected_latex = "\\color{red}{2 + 2}"
        result = self.converter.convert(merror)
        self.assertEqual(result, expected_latex)

    def test_convert_mglyph(self):
        expected_latex = ""
        result = self.converter.convert(mglyph)
        self.assertEqual(result, expected_latex)

    def test_convert_mphantom(self):
        expected_latex = "x + z"
        result = self.converter.convert(mphantom)
        self.assertEqual(result, expected_latex)

    def test_convert_msup_single(self):
        expected_latex = "x^{2}"
        result = self.converter.convert(msup)
        self.assertEqual(result, expected_latex)

    def test_convert_msup_with_mrow_on_top(self):
        expected_latex = "x^{a + b}"
        result = self.converter.convert(msup_with_mrow_on_top)
        self.assertEqual(result, expected_latex)

    def test_convert_msup_with_mrow_on_bottom(self):
        expected_latex = "\\left(x + y\\right)^{2}"
        result = self.converter.convert(msup_with_mrow_on_bottom)
        self.assertEqual(result, expected_latex)

    def test_convert_msup_with_mrow_on_top_bottom(self):
        expected_latex = "\\left(x + y\\right)^{2 + 2}"
        result = self.converter.convert(msup_with_mrow_on_top_bottom)
        self.assertEqual(result, expected_latex)

    def test_convert_msup_with_three_children(self):
        with self.assertRaises(InvalidNumberOfChildrenError):
            self.converter.convert(msup_with_three_children)

    def test_convert_msub_single(self):
        expected_latex = "x_{2}"
        result = self.converter.convert(msub)
        self.assertEqual(result, expected_latex)

    def test_convert_msub_with_mrow_on_bottom(self):
        expected_latex = "x_{a + b}"
        result = self.converter.convert(msub_with_mrow_on_bottom)
        self.assertEqual(result, expected_latex)

    def test_convert_msub_with_mrow_on_top(self):
        expected_latex = "\\left(x + y\\right)_{2}"
        result = self.converter.convert(msub_with_mrow_on_top)
        self.assertEqual(result, expected_latex)

    def test_convert_msub_with_mrow_on_top_bottom(self):
        expected_latex = "\\left(x + y\\right)_{2 + 2}"
        result = self.converter.convert(msub_with_mrow_on_top_bottom)
        self.assertEqual(result, expected_latex)

    def test_convert_msub_with_three_children(self):
        with self.assertRaises(InvalidNumberOfChildrenError):
            self.converter.convert(msub_with_three_children)

    def test_convert_msubsup(self):
        expected_latex = "\\int_{0}^{1}"
        result = self.converter.convert(msubsup)
        self.assertEqual(result, expected_latex)

    def test_convert_msubsup_with_mrow(self):
        expected_latex = "\\left(x + y\\right)_{0}^{1}"
        result = self.converter.convert(msubsup_with_mrow)
        self.assertEqual(result, expected_latex)

    def test_convert_msubsup_with_four_children(self):
        with self.assertRaises(InvalidNumberOfChildrenError):
            self.converter.convert(msubsup_with_four_children)

    def test_convert_mtext_normal(self):
        expected_latex = "\\text{Theorem of Pythagoras}"
        result = self.converter.convert(mtext_normal)
        self.assertEqual(result, expected_latex)

    def test_convert_mtext_bold(self):
        expected_latex = "\\textbf{Theorem of Pythagoras}"
        result = self.converter.convert(mtext_bold)
        self.assertEqual(result, expected_latex)

    def test_convert_mtext_italic(self):
        expected_latex = "\\textit{Theorem of Pythagoras}"
        result = self.converter.convert(mtext_italic)
        self.assertEqual(result, expected_latex)

    def test_convert_mtext_bold_italic(self):
        expected_latex = "\\textbf{\\textit{Theorem of Pythagoras}}"
        result = self.converter.convert(mtext_bold_italic)
        self.assertEqual(result, expected_latex)

    def test_convert_mtext_double_struck(self):
        expected_latex = "\\mathbb{R}"
        result = self.converter.convert(mtext_double_struck)
        self.assertEqual(result, expected_latex)

    def test_convert_mtext_fraktur(self):
        expected_latex = "\\mathfrak{Creepy}"
        result = self.converter.convert(mtext_fraktur)
        self.assertEqual(result, expected_latex)

    def test_convert_mtext_bold_fraktur(self):
        expected_latex = "\\mathfrak{Creepy}"
        result = self.converter.convert(mtext_bold_fraktur)
        self.assertEqual(result, expected_latex)

    def test_convert_mtext_monospace(self):
        expected_latex = "\\mathtt{simple text}"
        result = self.converter.convert(mtext_monospace)
        self.assertEqual(result, expected_latex)

    def test_convert_mtext_script(self):
        expected_latex = "\\text{Creepy}"
        result = self.converter.convert(mtext_script)
        self.assertEqual(result, expected_latex)

    def test_convert_mtext_bold_script(self):
        expected_latex = "\\text{Creepy}"
        result = self.converter.convert(mtext_bold_script)
        self.assertEqual(result, expected_latex)

    def test_convert_mover_overbrace(self):
        expected_latex = "\\hat{x + y + z}"
        result = self.converter.convert(mover_mrow)
        self.assertEqual(result, expected_latex)

    def test_convert_mover_encoded_mo(self):
        expected_latex = "\\hat{x + y + z}"
        result = self.converter.convert(mover_encoded_mo)
        self.assertEqual(result, expected_latex)

    def test_convert_mover_double_mrow(self):
        expected_latex = "\\overset{a + b}{x + y + z}"
        result = self.converter.convert(mover_double_mrow)
        self.assertEqual(result, expected_latex)

    def test_convert_mover_with_three_children(self):
        with self.assertRaises(InvalidNumberOfChildrenError):
            self.converter.convert(mover_three_children)

    def test_convert_munder_underbrace(self):
        expected_latex = "\\underbrace{x + y + z}"
        result = self.converter.convert(munder)
        self.assertEqual(result, expected_latex)

    def test_convert_munder_double_mrow(self):
        expected_latex = "\\underset{a + b}{x + y + z}"
        result = self.converter.convert(munder_double_mrow)
        self.assertEqual(result, expected_latex)

    def test_convert_munder_encoded_mrow(self):
        expected_latex = "\\underbrace{x + y + z}"
        result = self.converter.convert(munder_encoded_mrow)
        self.assertEqual(result, expected_latex)

    def test_convert_munderover(self):
        expected_latex = "\\int_{0}^{1}"
        result = self.converter.convert(munderover)
        self.assertEqual(result, expected_latex)

    def test_convert_munderover_encoded(self):
        expected_latex = "\\int_{0}^{\\infty}"
        result = self.converter.convert(munderover_encoded)
        self.assertEqual(result, expected_latex)

    def test_convert_munderover_with_three_children(self):
        with self.assertRaises(InvalidNumberOfChildrenError):
            self.converter.convert(munderover_with_three_children)

    def test_convert_mmultiscript(self):
        expected_latex = "\\left(N a\\right)_{11}^{+}"
        result = self.converter.convert(mmultiscript)
        self.assertEqual(result, expected_latex)

    def test_convert_mmultiscript_no_super(self):
        expected_latex = "\\left(N a\\right)_{11}^{}"
        result = self.converter.convert(mmultiscript_no_super)
        self.assertEqual(result, expected_latex)

    def test_convert_mmultiscript_no_sub(self):
        expected_latex = "\\left(N a\\right)_{}^{+}"
        result = self.converter.convert(mmultiscript_no_sub)
        self.assertEqual(result, expected_latex)

    def test_convert_mmultiscript_preset(self):
        expected_latex = "\\_{b}^{a}X_{d}^{c}"
        result = self.converter.convert(mmultiscript_preset)
        self.assertEqual(result, expected_latex)

    def test_convert_mmultiscript_preset_with_none(self):
        expected_latex = "\\_{b}^{}X_{}^{c}"
        result = self.converter.convert(mmultiscript_preset_with_none)
        self.assertEqual(result, expected_latex)

    def test_convert_mmultiscript_preset_only(self):
        expected_latex = "\\_{b}^{}X"
        result = self.converter.convert(mmultiscript_preset_only)
        self.assertEqual(result, expected_latex)

    def test_convert_mmultiscript_with_two_children(self):
        with self.assertRaises(InvalidNumberOfChildrenError):
            self.converter.convert(mmultiscript_with_two_children)

    # def test_convert_mmultiscript_trim_spaces(self):
    #     expected_latex = "x"
    #     result = self.converter.convert(
    #         math_with_epsilon_glyph
    #     )  # Adjusted to the correct variable
    #     self.assertEqual(result, expected_latex)

    # def test_convert_special_epsilon(self):
    #     expected_latex = 'd = \\left(\\frac{q^{2} L}{2 \\pi \\epsilon_{0} m g}\\right)^{1 / 3}'
    #     result = self.converter.convert(math_with_epsilon_glyph)
    #     self.assertEqual(result, expected_latex)
    #
    # def test_convert_mu(self):
    #     expected_latex = '2 \\mu s'
    #     result = self.converter.convert(math_with_mu_glyph)
    #     self.assertEqual(result, expected_latex)
    #
    # def test_convert_cdot_in_text(self):
    #     expected_latex = '\\text{kg}\\cdot\\text{m}^{2}'
    #     result = self.converter.convert(math_with_cdot_glyph)
    #     self.assertEqual(result, expected_latex)
    #
    # def test_convert_alternative_imath(self):
    #     expected_latex = 'E \\left(W_{\\imath}\\right) = \\mu'
    #     result = self.converter.convert(math_with_alternative1)
    #     self.assertEqual(result, expected_latex)
    #
    # def test_convert_alternative_square(self):
    #     expected_latex = '2 \\blacksquare s'
    #     result = self.converter.convert(math_with_alternative_square)
    #     self.assertEqual(result, expected_latex)
    #
    # def test_convert_input_expected_pairs(self):
    #     for pair in input_expected_pairs:
    #         input_val = pair['input']
    #         expected = pair['expected']
    #         op = pair['op']
    #         mathml = f'<math xmlns="http://www.w3.org/1998/Math/MathML"><{op}>{input_val}</{op}></math>'
    #         result = self.converter.convert(mathml)
    #         self.assertEqual(result, expected)
    #
    # def test_convert_ms_word_input(self):
    #     expected_latex = (
    #         'V_{i} \\frac{\\Delta C_{A , i}^{t}}{\\Delta t} = '
    #         '\\sum_{j = k}^{N} G_{i , j}^{D} \\left(C_{A , j} - C_{A , i}\\right)'
    #     )
    #     result = self.converter.convert(ms_word_input)
    #     self.assertEqual(result, expected_latex)
    #
    # def test_convert_complex_mathml(self):
    #     expected_latex = (
    #         '\\text{Required Value}_{\\text{other}} \\geq '
    #         '\\frac{21 f t^{3}}{A C H} \\cdot '
    #         '\\left(\\frac{I_{o}}{1000 B_{\\text{Btu}/\\text{h}}}\\right)'
    #     )
    #     result = self.converter.convert(complex_mathml)
    #     self.assertEqual(result, expected_latex)
    #
    # def test_convert_mmultiscripts_empty_preset(self):
    #     expected_latex = '\\_{b}^{}X_{}^{c}'
    #     result = self.converter.convert(mmultiscript_preset_with_none)
    #     self.assertEqual(result, expected_latex)
