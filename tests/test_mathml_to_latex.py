import unittest

from src.main import MathMLToLaTeX
from tests.mathml import mi, mi_with_space, mi_with_double_struck


class TestMathMLToLaTeX(unittest.TestCase):
    def setUp(self):
        self.converter = MathMLToLaTeX()

    def tearDown(self):
        del self.converter

    def test_convert_mi_to_simple_text(self):
        expected_latex = 'a'

        result = self.converter.convert(mi)

        self.assertEqual(result, expected_latex)

    def test_add_space_between_mi_tags(self):
        expected_latex = '\\Delta x'

        result = self.converter.convert(mi_with_space)

        self.assertEqual(result, expected_latex)

    def test_convert_mi_with_double_struck_attribute(self):
        expected_latex = '\\mathbb{R}^{n}'

        result = self.converter.convert(mi_with_double_struck)

        self.assertEqual(result, expected_latex)