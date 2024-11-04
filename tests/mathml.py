mi = '''
<root><math><mi>a</mi></math></root>
'''

mi_with_space = '''
<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi mathvariant="normal">Δ</mi>
  <mi>x</mi>
</math>
'''

# export const miWithDoubleStruck = `
# <math>
#   <msup>
#     <mrow>
#       <mi mathvariant="double-struck">R</mi>
#     </mrow>
#     <mrow>
#       <mi>n</mi>
#     </mrow>
#   </msup>
# </math>
# `;

mi_with_double_struck = '''
<math xmlns="http://www.w3.org/1998/Math/MathML">
  <msup>
    <mrow>
      <mi mathvariant="double-struck">R</mi>
    </mrow>
    <mrow>
      <mi>n</mi>
    </mrow>
  </msup>
</math>
'''

math_with_mi = '''
<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>b</mi>
</math>
'''

# export const mathWithMiAndSpace = '<root><math><mi> a </mi></math></root>';

math_with_mi_and_space = '''
<root>
  <math>
    <mi> a </mi>
  </math>
</root>
'''

# export const miWithEspecialChar = '<root><math><mi> &#x221E; </mi></math></root>';
mi_with_especial_char = '''
<root>
  <math>
    <mi> &#x221E; </mi>
  </math>
</root>
'''

mo_with_simple_operator = '''
<root>
  <math>
    <mo>+</mo>
  </math>
</root>
'''

mo_divider_operator = '''
<math>
  <mi>x</mi>
  <mo>=</mo>
  <mn>4</mn>
  <mrow>
    <mo>/</mo>
  </mrow>
  <mn>5</mn>
</math>
'''

mo_with_glyph_operator = '''
<root>
  <math>
    <mo>*</mo>
  </math>
</root>
'''

mo_with_char_operator = '''
<root>
  <math>
    <mo>b</mo>
  </math>
</root>
'''

mo_with_char_operator_and_mi = '''
<root>
  <math xmlns="http://www.w3.org/1998/Math/MathML">
    <mstyle displaystyle="true">
      <mi>a</mi>
      <mo>&#x21D2;</mo>
      <mi>b</mi>
    </mstyle>
  </math>
</root>
'''

mrow_with_mn_and_mo = '''
<root>
  <math>
    <mrow>
      <mn>2</mn>
      <mo>+</mo>
      <mn>2</mn>
    </mrow>
  </math>
</root>
'''

msqrt = '''
<root>
  <math>
    <msqrt>
      <mn>2</mn>
    </msqrt>
  </math>
</root>
'''

msqrt_with_wrapped_content = '''
<root>
  <math>
    <msqrt>
      <mn>2</mn>
      <mo>+</mo>
      <mn>2</mn>
    </msqrt>
  </math>
</root>
'''

msqrt_with_mrow = '''
<root>
  <math>
    <msqrt>
      <mrow>
        <mn>2</mn>
        <mo>+</mo>
        <mn>2</mn>
      </mrow>
    </msqrt>
  </math>
</root>
'''

empty_msqrt = '''
<root>
  <math>
    <msqrt>
    </msqrt>
  </math>
</root>
'''

