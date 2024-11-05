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

mfenced_without_attribute = '''
<root>
  <math>
  <mfenced>
    <mn>3</mn>
  </mfenced>
  </math>
</root>
'''

mfenced_with_open = '''
<root>
  <math>
  <mfenced open="{">
    <mn>3</mn>
  </mfenced>
  </math>
</root>
'''

mfenced_with_open_and_close = '''
<root>
  <math>
  <mfenced open="(" close=")">
    <mn>3</mn>
  </mfenced>
  </math>
</root>
'''

mfenced_with_broken_close = '''
<root>
  <math>
  <mfenced open="{" close>
    <mn>3</mn>
  </mfenced>
  </math>
</root>
'''

mfenced_with_wrapped_content = '''
<root>
  <math>
  <mfenced>
    <mn>3</mn>
    <mn>2</mn>
    <mn>1</mn>
  </mfenced>
  </math>
</root>
'''

mfenced_with_empty_separator = '''
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
'''

mfenced_with_separator = '''
<root>
  <math>
  <mfenced separators=';;;'>
    <mn>3</mn>
    <mn>2</mn>
    <mn>1</mn>
  </mfenced>
  </math>
</root>
'''

mfenced_with_diff_separators = '''
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
'''

mfenced_as_bmatrix = '''
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
'''

mfenced_as_pmatrix = '''
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
'''

mfenced_as_vmatrix = '''
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
'''

mfenced_as_big_bmatrix = '''
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
'''

mfenced_as_big_vmatrix = '''
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
'''

mfenced_as_matrix = '''
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
'''

mfenced_as_partial_function = '''
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
'''

mfenced_with_nested_mtables = '''
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
'''










































