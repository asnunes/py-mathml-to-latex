# mathml-to-latex

It converts [MathML](https://en.wikipedia.org/wiki/MathML) to [LaTeX](https://pt.wikipedia.org/wiki/LaTeX). 
Based on the Node.js version of the [mathml-to-latex](https://github.com/asnunes/mathml-to-latex) library.

## Installation

```bash
pip install mathml-to-latex
```

## Usage

```python
from mathml_to_latex.converter import MathMLToLaTeX

mathml = """
<math>
    <mrow>
        <mi>A</mi>
        <mo>=</mo>
        <mfenced open = "[" close="]">
        <mtable>
            <mtr>
            <mtd><mi>x</mi></mtd>
            <mtd><mi>y</mi></mtd>
            </mtr>
            <mtr>
            <mtd><mi>z</mi></mtd>
            <mtd><mi>w</mi></mtd>
            </mtr>
        </mtable>
        </mfenced>
    </mrow>
</math>
"""

result = MathMLToLaTeX().convert(mathml)
# A = \begin{bmatrix} x & y \\ z & w \end{bmatrix}
```

## Running Tests

```bash
python -m unittest discover tests
```

### Using Docker
```bash
docker build -t mathml-to-latex-test .
docker run mathml-to-latex-test
```