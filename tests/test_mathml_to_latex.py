import unittest

from src.main import MathMLToLaTeX


class TestMathMLToLaTeX(unittest.TestCase):
    def setUp(self):
        self.converter = MathMLToLaTeX()

    def tearDown(self):
        del self.converter

    def test_convert_mi_to_simple_text(self):
        mathml = '<root><math><mi>a</mi></math></root>'
        expected_latex = 'a'

        result = self.converter.convert(mathml)

        self.assertEqual(result, expected_latex)