mi = """
<root><math><mi>a</mi></math></root>
"""

mi_with_space = """
<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi mathvariant="normal">Δ</mi>
  <mi>x</mi>
</math>
"""

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

mi_with_double_struck = """
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
"""

math_with_mi = """
<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>b</mi>
</math>
"""

# export const mathWithMiAndSpace = '<root><math><mi> a </mi></math></root>';

math_with_mi_and_space = """
<root>
  <math>
    <mi> a </mi>
  </math>
</root>
"""

# export const miWithEspecialChar = '<root><math><mi> &#x221E; </mi></math></root>';
mi_with_especial_char = """
<root>
  <math>
    <mi> &#x221E; </mi>
  </math>
</root>
"""

mo_with_simple_operator = """
<root>
  <math>
    <mo>+</mo>
  </math>
</root>
"""

mo_divider_operator = """
<math>
  <mi>x</mi>
  <mo>=</mo>
  <mn>4</mn>
  <mrow>
    <mo>/</mo>
  </mrow>
  <mn>5</mn>
</math>
"""

mo_with_glyph_operator = """
<root>
  <math>
    <mo>*</mo>
  </math>
</root>
"""

mo_with_char_operator = """
<root>
  <math>
    <mo>b</mo>
  </math>
</root>
"""

mo_with_char_operator_and_mi = """
<root>
  <math xmlns="http://www.w3.org/1998/Math/MathML">
    <mstyle displaystyle="true">
      <mi>a</mi>
      <mo>&#x21D2;</mo>
      <mi>b</mi>
    </mstyle>
  </math>
</root>
"""

mrow_with_mn_and_mo = """
<root>
  <math>
    <mrow>
      <mn>2</mn>
      <mo>+</mo>
      <mn>2</mn>
    </mrow>
  </math>
</root>
"""

msqrt = """
<root>
  <math>
    <msqrt>
      <mn>2</mn>
    </msqrt>
  </math>
</root>
"""

msqrt_with_wrapped_content = """
<root>
  <math>
    <msqrt>
      <mn>2</mn>
      <mo>+</mo>
      <mn>2</mn>
    </msqrt>
  </math>
</root>
"""

msqrt_with_mrow = """
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
"""

empty_msqrt = """
<root>
  <math>
    <msqrt>
    </msqrt>
  </math>
</root>
"""

mfenced_without_attribute = """
<root>
  <math>
  <mfenced>
    <mn>3</mn>
  </mfenced>
  </math>
</root>
"""

mfenced_with_open = """
<root>
  <math>
  <mfenced open="{">
    <mn>3</mn>
  </mfenced>
  </math>
</root>
"""

mfenced_with_open_and_close = """
<root>
  <math>
  <mfenced open="(" close=")">
    <mn>3</mn>
  </mfenced>
  </math>
</root>
"""

mfenced_with_broken_close = """
<root>
  <math>
  <mfenced open="{" close>
    <mn>3</mn>
  </mfenced>
  </math>
</root>
"""

mfenced_with_wrapped_content = """
<root>
  <math>
  <mfenced>
    <mn>3</mn>
    <mn>2</mn>
    <mn>1</mn>
  </mfenced>
  </math>
</root>
"""

mfenced_with_empty_separator = """
<root>
  <math>
  <mfenced separators=''>
    <mn>3</mn>
    <mn>2</mn>
    <mn>1</mn>
    <mn>7</mn>
  </mfenced>
  </math>
</root>
"""

mfenced_with_separator = """
<root>
  <math>
  <mfenced separators=';;;'>
    <mn>3</mn>
    <mn>2</mn>
    <mn>1</mn>
  </mfenced>
  </math>
</root>
"""

mfenced_with_diff_separators = """
<root>
  <math>
  <mfenced separators=';.'>
    <mn>3</mn>
    <mn>2</mn>
    <mn>1</mn>
    <mn>7</mn>
  </mfenced>
  </math>
</root>
"""

mfenced_as_bmatrix = """
<root>
  <math xmlns = "http://www.w3.org/1998/Math/MathML">
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
</root>
"""

mfenced_as_pmatrix = """
<root>
  <math xmlns = "http://www.w3.org/1998/Math/MathML">
    <mrow>
      <mi>A</mi>
      <mo>=</mo>
      <mfenced open = "(" close=")">
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
</root>
"""

mfenced_as_vmatrix = """
<root>
  <math xmlns = "http://www.w3.org/1998/Math/MathML">
    <mrow>
      <mi>A</mi>
      <mo>=</mo>
      <mfenced open = "|" close="|">
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
</root>
"""

mfenced_as_big_bmatrix = """
<root>
  <math xmlns = "http://www.w3.org/1998/Math/MathML">
    <mrow>
      <mi>A</mi>
      <mo>=</mo>
      <mfenced open = "{" close="}">
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
</root>
"""

mfenced_as_big_vmatrix = """
<root>
  <math xmlns = "http://www.w3.org/1998/Math/MathML">
    <mrow>
      <mi>A</mi>
      <mo>=</mo>
      <mfenced open = "||" close="||">
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
</root>
"""

mfenced_as_matrix = """
<root>
  <math xmlns = "http://www.w3.org/1998/Math/MathML">
    <mrow>
      <mi>A</mi>
      <mo>=</mo>
      <mfenced>
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
</root>
"""

mfenced_as_partial_function = """
<root>
  <math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
    <mi>f</mi>
    <mfenced separators="|">
      <mrow>
        <mi>x</mi>
      </mrow>
    </mfenced>
    <mo>=</mo>
    <mfenced open="{" close="" separators="|">
      <mrow>
        <mtable>
          <mtr>
            <mtd>
              <mrow>
                <maligngroup></maligngroup>
                <msup>
                  <mrow>
                    <mi>x</mi>
                  </mrow>
                  <mrow>
                    <mn>2</mn>
                  </mrow>
                </msup>
                <mo>,</mo>
                <mi>x</mi>
                <mo>&lt;</mo>
                <mn>0</mn>
              </mrow>
            </mtd>
          </mtr>
          <mtr>
            <mtd>
              <mrow>
                <maligngroup></maligngroup>
                <msup>
                  <mrow>
                    <mi>e</mi>
                  </mrow>
                  <mrow>
                    <mi>x</mi>
                  </mrow>
                </msup>
                <mo>,</mo>
                <mi>x</mi>
                <mo>≥</mo>
                <mn>0</mn>
              </mrow>
            </mtd>
          </mtr>
        </mtable>
      </mrow>
    </mfenced>
  </math>
</root>
"""

mfenced_with_nested_mtables = """
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mfenced separators="|">
    <mrow>
      <mtable>
        <mtr>
          <mtd>
            <mtable>
              <mtr>
                <mtd>
                  <msub>
                    <mrow>
                      <mi>a</mi>
                    </mrow>
                    <mrow>
                      <mn>11</mn>
                    </mrow>
                  </msub>
                </mtd>
                <mtd>
                  <msub>
                    <mrow>
                      <mi>a</mi>
                    </mrow>
                    <mrow>
                      <mn>12</mn>
                    </mrow>
                  </msub>
                </mtd>
              </mtr>
            </mtable>
          </mtd>
          <mtd>
            <mtable>
              <mtr>
                <mtd>
                  <mo>…</mo>
                </mtd>
                <mtd>
                  <mo>…</mo>
                </mtd>
              </mtr>
            </mtable>
          </mtd>
          <mtd>
            <msub>
              <mrow>
                <mi>a</mi>
              </mrow>
              <mrow>
                <mn>1</mn>
                <mi>n</mi>
              </mrow>
            </msub>
          </mtd>
        </mtr>
        <mtr>
          <mtd>
            <mtable>
              <mtr>
                <mtd>
                  <msub>
                    <mrow>
                      <mi>a</mi>
                    </mrow>
                    <mrow>
                      <mn>21</mn>
                    </mrow>
                  </msub>
                </mtd>
                <mtd>
                  <msub>
                    <mrow>
                      <mi>a</mi>
                    </mrow>
                    <mrow>
                      <mn>22</mn>
                    </mrow>
                  </msub>
                </mtd>
              </mtr>
            </mtable>
          </mtd>
          <mtd>
            <mtable>
              <mtr>
                <mtd>
                  <mo>⋱</mo>
                </mtd>
                <mtd>
                  <mi></mi>
                </mtd>
              </mtr>
            </mtable>
          </mtd>
          <mtd>
            <msub>
              <mrow>
                <mi>a</mi>
              </mrow>
              <mrow>
                <mn>2</mn>
                <mi>n</mi>
              </mrow>
            </msub>
          </mtd>
        </mtr>
        <mtr>
          <mtd>
            <mtable>
              <mtr>
                <mtd>
                  <mtable>
                    <mtr>
                      <mtd>
                        <mo>⋮</mo>
                        <mi></mi>
                        <mi></mi>
                        <mi></mi>
                        <mi></mi>
                      </mtd>
                      <mtd>
                        <mo>⋮</mo>
                      </mtd>
                    </mtr>
                  </mtable>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mtable>
                    <mtr>
                      <mtd>
                        <msub>
                          <mrow>
                            <mi>a</mi>
                          </mrow>
                          <mrow>
                            <mi>m</mi>
                            <mn>1</mn>
                          </mrow>
                        </msub>
                      </mtd>
                      <mtd>
                        <msub>
                          <mrow>
                            <mi>a</mi>
                          </mrow>
                          <mrow>
                            <mi>m</mi>
                            <mn>2</mn>
                          </mrow>
                        </msub>
                      </mtd>
                    </mtr>
                  </mtable>
                </mtd>
              </mtr>
            </mtable>
          </mtd>
          <mtd>
            <mtable>
              <mtr>
                <mtd>
                  <mtable>
                    <mtr>
                      <mtd>
                        <mi></mi>
                      </mtd>
                      <mtd>
                        <mo>⋱</mo>
                      </mtd>
                    </mtr>
                  </mtable>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <mtable>
                    <mtr>
                      <mtd>
                        <mo>…</mo>
                      </mtd>
                      <mtd>
                        <mo>…</mo>
                      </mtd>
                    </mtr>
                  </mtable>
                </mtd>
              </mtr>
            </mtable>
          </mtd>
          <mtd>
            <mtable>
              <mtr>
                <mtd>
                  <mo>⋮</mo>
                </mtd>
              </mtr>
              <mtr>
                <mtd>
                  <msub>
                    <mrow>
                      <mi>a</mi>
                    </mrow>
                    <mrow>
                      <mi>m</mi>
                      <mi>n</mi>
                    </mrow>
                  </msub>
                </mtd>
              </mtr>
            </mtable>
          </mtd>
        </mtr>
      </mtable>
    </mrow>
  </mfenced>
  <mi></mi>
</math>
"""

mfrac = """
<root>
  <math>
    <mfrac>
      <mi>x</mi>
      <mn>3</mn>
    </mfrac>
  </math>
</root>
"""

mfrac_with_mrow = """
<root>
  <math>
    <mfrac>
      <mrow>
        <mi>a</mi>
        <mo>+</mo>
        <mi>2</mi>
      </mrow>
      <mrow>
        <mi>b</mi>
        <mo>-</mo>
        <mi>3</mi>
      </mrow>
    </mfrac>
  </math>
</root>
"""

short_m_frac = """
<root>
  <math>
    <mfrac bevelled="true">
      <mn>1</mn>
      <mrow>
        <msup>
          <mi>x</mi>
          <mn>3</mn>
        </msup>
        <mo>+</mo>
        <mn>3</mn>
      </mrow>
    </mfrac>
  </math>
</root>
"""

mfrac_with_three_children = """
<root>
  <math>
    <mfrac>
      <mi>x</mi>
      <mn>3</mn>
      <mi>2</mi>
    </mfrac>
  </math>
</root>
"""

mroot = """
<root>
  <math>
    <mroot>
      <mrow>
        <mi>x</mi>
        <mo>+</mo>
        <mi>2</mi>
      </mrow>
      <mn>3</mn>
    </mroot> 
  </math>
</root>
"""

mroot_with_three_children = """
<root>
  <math>
    <mroot>
      <mrow>
        <mi>x</mi>
        <mo>+</mo>
        <mi>2</mi>
      </mrow>
      <mn>3</mn>
      <mn>2</mn>
    </mroot> 
  </math>
</root>
"""

mpadded = """
<root>
  <math>
    <mpadded>
      <mn>2</mn>
      <mo>+</mo>
      <mn>2</mn>
    </mpadded>
  </math>
</root>
"""

maction = """
<root>
  <math>
    <maction>
      <mrow>
        <mi>a</mi>
        <mo>+</mo>
        <mi>2</mi>
      </mrow>
      <mrow>
        <mi>b</mi>
        <mo>-</mo>
        <mi>3</mi>
      </mrow>
    </maction>
  </math>
</root>
"""

maction_with_mrow = """
<root>
  <math>
    <maction>
      <mrow>
        <mi>a</mi>
        <mo>+</mo>
        <mi>2</mi>
      </mrow>
      <mrow>
        <mi>b</mi>
        <mo>-</mo>
        <mi>3</mi>
      </mrow>
      <mrow>
        <mi>a</mi>
        <mo>+</mo>
        <mi>b</mi>
      </mrow>
    </maction>
  </math>
</root>
"""

maction_type_toggle = """
<root>
  <math>
    <maction actiontype="toggle">
      <mrow>
        <mi>a</mi>
        <mo>+</mo>
        <mi>2</mi>
      </mrow>
      <mrow>
        <mi>b</mi>
        <mo>-</mo>
        <mi>3</mi>
      </mrow>
      <mrow>
        <mi>a</mi>
        <mo>+</mo>
        <mi>b</mi>
      </mrow>
    </maction>
  </math>
</root>
"""

maction_type_statusline = """
<root>
  <math>
    <maction actiontype="statusline">
      <mrow>
        <mi>a</mi>
        <mo>+</mo>
        <mi>2</mi>
      </mrow>
      <mrow>
        <mi>b</mi>
        <mo>-</mo>
        <mi>3</mi>
      </mrow>
      <mrow>
        <mi>a</mi>
        <mo>+</mo>
        <mi>b</mi>
      </mrow>
    </maction>
  </math>
</root>
"""

maction_type_tooltip = """
<root>
  <math>
    <maction actiontype="tooltip">
      <mrow>
        <mi>a</mi>
        <mo>+</mo>
        <mi>2</mi>
      </mrow>
      <mrow>
        <mi>b</mi>
        <mo>-</mo>
        <mi>3</mi>
      </mrow>
      <mrow>
        <mi>a</mi>
        <mo>+</mo>
        <mi>b</mi>
      </mrow>
    </maction>
  </math>
</root>
"""

menclose = """
<root>
  <math>
    <menclose>
      <mi>a</mi>
      <mo>+</mo>
      <mi>2</mi>
    </menclose>
  </math>
</root>
"""

menclose_notation_longdiv = """
<root>
  <math>
    <menclose notation="longdiv">
      <mi>a</mi>
      <mo>+</mo>
      <mi>2</mi>
    </menclose>
  </math>
</root>
"""

menclose_notation_actuarial = """
<root>
  <math>
    <menclose notation="actuarial">
      <mi>a</mi>
      <mo>+</mo>
      <mi>2</mi>
    </menclose>
  </math>
</root>
"""

menclose_notation_radical = """
<root>
  <math>
    <menclose notation="radical">
      <mi>a</mi>
      <mo>+</mo>
      <mi>2</mi>
    </menclose>
  </math>
</root>
"""

menclose_notation_box = """
<root>
  <math>
    <menclose notation="box">
      <mrow>
        <mi>E</mi>
        <mo>=</mo>
        <mi>m</mi>
        <msup>
          <mi>c</mi>
          <mn>2</mn>
        </msup>
      </mrow>
    </menclose>
  </math>
</root>
"""

menclose_notation_rounded_box = """
<root>
  <math>
    <menclose notation="roundedbox">
      <mrow>
        <mi>E</mi>
        <mo>=</mo>
        <mi>m</mi>
        <msup>
          <mi>c</mi>
          <mn>2</mn>
        </msup>
      </mrow>
    </menclose>
  </math>
</root>
"""

menclose_notation_circle = """
<root>
  <math>
    <menclose notation="circle">
      <mrow>
        <mi>E</mi>
        <mo>=</mo>
        <mi>m</mi>
        <msup>
          <mi>c</mi>
          <mn>2</mn>
        </msup>
      </mrow>
    </menclose>
  </math>
</root>
"""

menclose_notation_left = """
<root>
  <math>
    <menclose notation="left">
      <mrow>
        <mi>E</mi>
        <mo>=</mo>
        <mi>m</mi>
        <msup>
          <mi>c</mi>
          <mn>2</mn>
        </msup>
      </mrow>
    </menclose>
  </math>
</root>
"""

menclose_notation_right = """
<root>
  <math>
    <menclose notation="right">
      <mrow>
        <mi>E</mi>
        <mo>=</mo>
        <mi>m</mi>
        <msup>
          <mi>c</mi>
          <mn>2</mn>
        </msup>
      </mrow>
    </menclose>
  </math>
</root>
"""

menclose_notation_top = """
<root>
  <math>
    <menclose notation="top">
      <mrow>
        <mi>E</mi>
        <mo>=</mo>
        <mi>m</mi>
        <msup>
          <mi>c</mi>
          <mn>2</mn>
        </msup>
      </mrow>
    </menclose>
  </math>
</root>
"""

menclose_notation_bottom = """
<root>
  <math>
    <menclose notation="bottom">
      <mi>a</mi>
      <mo>+</mo>
      <mi>2</mi>
    </menclose>
  </math>
</root>
"""

menclose_notation_updiagnonalstrike = """
<root>
  <math>
    <menclose notation="updiagonalstrike">
      <mi>a</mi>
      <mo>+</mo>
      <mi>2</mi>
    </menclose>
  </math>
</root>
"""

menclose_notation_downdiagnonalstrike = """
<root>
  <math>
    <menclose notation="downdiagonalstrike">
      <mi>a</mi>
      <mo>+</mo>
      <mi>2</mi>
    </menclose>
  </math>
</root>
"""

menclose_notation_horizontalstrike = """
<root>
  <math>
    <menclose notation="horizontalstrike">
      <mi>a</mi>
      <mo>+</mo>
      <mi>2</mi>
    </menclose>
  </math>
</root>
"""

menclose_notation_verticalstrike = """
<root>
  <math>
    <menclose notation="verticalstrike">
      <mi>a</mi>
      <mo>+</mo>
      <mi>2</mi>
    </menclose>
  </math>
</root>
"""

menclose_notation_updiagnonalarrow = """
<root>
  <math>
    <menclose notation="updiagonalarrow">
      <mi>a</mi>
      <mo>+</mo>
      <mi>2</mi>
    </menclose>
  </math>
</root>
"""

menclose_notation_madruwb = """
<root>
  <math>
    <menclose notation="madruwb">
      <mi>a</mi>
      <mo>+</mo>
      <mi>2</mi>
    </menclose>
  </math>
</root>
"""

menclose_notation_phasorangle = """
<root>
  <math>
    <menclose notation="phasorangle">
      <mi>a</mi>
      <mo>+</mo>
      <mi>2</mi>
    </menclose>
  </math>
</root>
"""

merror = """
<root>
  <math>
    <merror>
      <mi>2</mi>
      <mo>+</mo>
      <mi>2</mi>
    </merror>
  </math>
</root>
"""

mglyph = """
<root>
  <math>
    <mi><mglyph src="my-glyph.png" alt="my glyph"/></mi>
  </math>
</root>
"""

mphantom = """
<root>
  <math>
    <mrow>
      <mi> x </mi>
      <mo> + </mo>
      <mphantom>
        <mi> y </mi>
        <mo> + </mo>
      </mphantom>
      <mi> z </mi>
    </mrow>
  </math>
</root>
"""

msup = """
<root>
  <math>
    <msup>
      <mi>x</mi>
      <mn>2</mn>
    </msup>
  </math>
</root>
"""

msup_with_mrow_on_top = """
<root>
  <math>
    <msup>
      <mi>x</mi>
      <mrow>
        <mn>a</mn>
        <mo>+</mo>
        <mn>b</mn>
      </mrow>
    </msup>
  </math>
</root>
"""

msup_with_mrow_on_bottom = """
<root>
  <math>
    <msup>
      <mrow>
        <mn>x</mn>
        <mo>+</mo>
        <mn>y</mn>
      </mrow>
      <mi>2</mi>
    </msup>
  </math>
</root>
"""

msup_with_mrow_on_top_bottom = """
<root>
  <math>
    <msup>
      <mrow>
        <mn>x</mn>
        <mo>+</mo>
        <mn>y</mn>
      </mrow>
      <mrow>
        <mn>2</mn>
        <mo>+</mo>
        <mn>2</mn>
      </mrow>
    </msup>
  </math>
</root>
"""

msup_with_three_children = """
<root>
  <math>
    <msup>
      <mi>x</mi>
      <mn>2</mn>
      <mn>3</mn>
    </msup>
  </math>
</root>
"""

msub = """
<root>
  <math>
    <msub>
      <mi>x</mi>
      <mn>2</mn>
    </msub>
  </math>
</root>
"""

msub_with_mrow_on_bottom = """
<root>
  <math>
    <msub>
      <mi>x</mi>
      <mrow>
        <mn>a</mn>
        <mo>+</mo>
        <mn>b</mn>
      </mrow>
    </msub>
  </math>
</root>
"""

msub_with_mrow_on_top = """
<root>
  <math>
    <msub>
      <mrow>
        <mn>x</mn>
        <mo>+</mo>
        <mn>y</mn>
      </mrow>
      <mi>2</mi>
    </msub>
  </math>
</root>
"""

msub_with_mrow_on_top_bottom = """
<root>
  <math>
    <msub>
      <mrow>
        <mn>x</mn>
        <mo>+</mo>
        <mn>y</mn>
      </mrow>
      <mrow>
        <mn>2</mn>
        <mo>+</mo>
        <mn>2</mn>
      </mrow>
    </msub>
  </math>
</root>
"""

msub_with_three_children = """
<root>
  <math>
    <msub>
      <mi>x</mi>
      <mn>2</mn>
      <mn>3</mn>
    </msub>
  </math>
</root>
"""

msubsup = """
<root>
  <math>
    <msubsup>
      <mo> &#x222B; </mo>
      <mn> 0 </mn>
      <mn> 1 </mn>
    </msubsup>
  </math>
</root>
"""

msubsup_with_mrow = """
<root>
  <math>
    <msubsup>
      <mrow>
        <mn>x</mn>
        <mo>+</mo>
        <mn>y</mn>
      </mrow>
      <mn> 0 </mn>
      <mn> 1 </mn>
    </msubsup>
  </math>
</root>
"""

msubsup_with_four_children = """
<root>
  <math>
    <msubsup>
      <mo> &#x222B; </mo>
      <mn> 0 </mn>
      <mn> 1 </mn>
      <mn> 5 </mn>
    </msubsup>
  </math>
</root>
"""

mtext = """
<root>
  <math xmlns="http://www.w3.org/1998/Math/MathML">
    <mtext> Theorem of Pythagoras </mtext>
  </math>
</root>
"""

mtext_normal = """
<root>
  <math xmlns="http://www.w3.org/1998/Math/MathML">
    <mtext mathvariant="normal"> Theorem of Pythagoras </mtext>
  </math>
</root>
"""

mtext_bold = """
<root>
  <math xmlns="http://www.w3.org/1998/Math/MathML">
    <mtext mathvariant="bold"> Theorem of Pythagoras </mtext>
  </math>
</root>
"""

mtext_italic = """
<root>
  <math xmlns="http://www.w3.org/1998/Math/MathML">
    <mtext mathvariant="italic"> Theorem of Pythagoras </mtext>
  </math>
</root>
"""

mtext_bold_italic = """
<root>
  <math xmlns="http://www.w3.org/1998/Math/MathML">
    <mtext mathvariant="bold-italic"> Theorem of Pythagoras </mtext>
  </math>
</root>
"""

mtext_double_struck = """
<root>
  <math xmlns="http://www.w3.org/1998/Math/MathML">
    <mtext mathvariant="double-struck">R</mtext>
  </math>
</root>
"""

mtext_fraktur = """
<root>
  <math xmlns="http://www.w3.org/1998/Math/MathML">
    <mtext mathvariant="fraktur">Creepy</mtext>
  </math>
</root>
"""

mtext_bold_fraktur = """
<root>
  <math xmlns="http://www.w3.org/1998/Math/MathML">
    <mtext mathvariant="bold-fraktur">Creepy</mtext>
  </math>
</root>
"""

mtext_monospace = """
<root>
  <math xmlns="http://www.w3.org/1998/Math/MathML">
    <mtext mathvariant="monospace">simple text</mtext>
  </math>
</root>
"""

mtext_script = """
<root>
  <math xmlns="http://www.w3.org/1998/Math/MathML">
    <mtext mathvariant="script">Creepy</mtext>
  </math>
</root>
"""

mtext_bold_script = """
<root>
  <math xmlns="http://www.w3.org/1998/Math/MathML">
    <mtext mathvariant="bold-script">Creepy</mtext>
  </math>
</root>
"""

mtext_mover = """
<root>
  <math>
    <mover accent="true">
      <mrow>
        <mi> x </mi>
        <mo> + </mo>
        <mi> y </mi>
        <mo> + </mo>
        <mi> z </mi>
      </mrow>
      <mo>⏞</mo>
    </mover>
  </math>
</root>
"""

mover_mrow = """
<root>
  <math>
    <mover accent="true">
      <mrow>
        <mi> x </mi>
        <mo> + </mo>
        <mi> y </mi>
        <mo> + </mo>
        <mi> z </mi>
      </mrow>
      <mo>^</mo>
    </mover>
  </math>
</root>
"""

mover_encoded_mo = """
<root>
  <math>
    <mover accent="true">
      <mrow>
        <mi> x </mi>
        <mo> + </mo>
        <mi> y </mi>
        <mo> + </mo>
        <mi> z </mi>
      </mrow>
      <mo>&#x2C6;</mo>
    </mover>
  </math>
</root>
"""

mover_double_mrow = """
<root>
  <math>
    <mover accent="true">
      <mrow>
        <mi> x </mi>
        <mo> + </mo>
        <mi> y </mi>
        <mo> + </mo>
        <mi> z </mi>
      </mrow>
      <mrow>
        <mi> a </mi>
        <mo> + </mo>
        <mi> b </mi>
      </mrow>
    </mover>
  </math>
</root>
"""

mover_three_children = """
<root>
  <math>
    <mover accent="true">
      <mrow>
        <mi> x </mi>
        <mo> + </mo>
        <mi> y </mi>
        <mo> + </mo>
        <mi> z </mi>
      </mrow>
      <mo> + </mo>
      <mi> z </mi>
    </mover>
  </math>
</root>
"""

munder = """
<root>
  <math>
    <munder accent="true">
      <mrow>
        <mi> x </mi>
        <mo> + </mo>
        <mi> y </mi>
        <mo> + </mo>
        <mi> z </mi>
      </mrow>
      <mo>⏟</mo>
    </munder>
  </math>
</root>
"""

munder_double_mrow = """
<root>
  <math>
    <munder accent="true">
      <mrow>
        <mi> x </mi>
        <mo> + </mo>
        <mi> y </mi>
        <mo> + </mo>
        <mi> z </mi>
      </mrow>
      <mrow>
        <mi> a </mi>
        <mo> + </mo>
        <mi> b </mi>
      </mrow>
    </munder>
  </math>
</root>
"""

munder_encoded_mrow = """
<root>
  <math>
    <munder accent="true">
      <mrow>
        <mi> x </mi>
        <mo> + </mo>
        <mi> y </mi>
        <mo> + </mo>
        <mi> z </mi>
      </mrow>
      <mo>&#x23DF;</mo>
    </munder>
  </math>
</root>
"""

munderover = """
<root>
  <math>
    <munderover>
      <mo> &#x222B;</mo>
      <mn> 0 </mn>
      <mn> 1 </mn>
    </munderover>
  </math>
</root>
"""

munderover_encoded = """
<root>
  <math>
    <munderover>
      <mo> &#x222B;</mo>
      <mn> 0 </mn>
      <mi> &#x221E; </mi>
    </munderover>
  </math>
</root>
"""

munderover_with_three_children = """
<root>
  <math>
    <munderover>
      <mo> &#x222B;</mo>
      <mn> 0 </mn>
      <mi> &#x221E; </mi>
      <mi> 1 </mi>
    </munderover>
  </math>
</root>
"""
