# Programa para gerar código em JavaCC de reconhecimento léxico da linguagem Go.

nome_da_classe = 'Compilador'
prefixo_token = 'TOKEN_'
posfixo_token = ''

# Responde se o token é ou não final. 
# Por ex.: digitos que comporão números não são tokens finais.
def eh_token_final(nome_do_token):
  if nome_do_token[0] == '#':
    return False

  return True


# Adapta o nome do token para a regra usada.
def adaptar(nome_do_token):
  nome_final = None

  # Para tokens que não sejam finais, como digitos que comporão números.
  if eh_token_final(nome_do_token) == False:
    nome_final = '#' + prefixo_token + nome_do_token[1:] + posfixo_token

  else:
    nome_final = prefixo_token + nome_do_token + posfixo_token

  return nome_final

# Tokens normais: seus nomes e valores são iguais.
tipos = [ 'ANY', 'BOOL', 'BYTE', 'COMPARABLE', 'COMPLEX64', 'COMPLEX128', 'ERROR',
          'FLOAT32', 'FLOAT64', 'INT', 'INT8', 'INT16', 'INT32', 'INT64', 'RUNE',
          'STRING', 'UINT', 'UINT8', 'UINT16', 'UINT32', 'UINT64', 'UINTPTR' ]

constantes = [ 'TRUE', 'FALSE', 'IOTA' ]

funcoes = [ 'APPEND', 'CAP', 'CLOSE', 'COMPLEX', 'COPY', 'DELETE', 'IMAG', 'LEN',
            'MAKE', 'NEW', 'PANIC', 'PRINTLN', 'PRINT', 'REAL', 'RECOVER' ]

palavras_chave = [ 'BREAK', 'DEFAULT', 'FUNC', 'INTERFACE', 'SELECT', 'CASE',
                   'DEFER', 'GO', 'MAP', 'STRUCT', 'CHAN', 'ELSE', 'GOTO',
                   'PACKAGE', 'SWITCH', 'CONST', 'FALLTHROUGH', 'IF', 'RANGE',
                   'TYPE', 'CONTINUE', 'FOR', 'IMPORT', 'RETURN', 'VAR' ]

valor_zero = [ 'NIL' ]

# Tokens especiais: seus nomes e valores são distintos.
comentarios = \
{
  'LINE_COMMENT': '"//"',
  'OPEN_GENERAL_COMMENT': '"/*"',
  'CLOSE_GENERAL_COMMENT': '"*/"'
}

operadores = \
{
  'DIFFERENT': '"!="',

  'LESS_EQUAL': '"<="',

  'GREATER_EQUAL': '">="',

  'SHORT_DECLARATION': '":="',

  'ELLIPSIS': '"..."',

  'OPEN_PARENTHESIS': '"("',

  'CLOSE_PARENTHESIS': '")"',

  'OPEN_BRACKET': '"["',

  'CLOSE_BRACKET': '"]"',

  'OPEN_BRACE': '"{"',

  'CLOSE_BRACE': '"}"',

  'COMMA': '","',

  'SEMICOLON': '";"',

  'DOT': '"."',

  'COLON': '":"',

  'AND': '"&&"',

  'OR': '"||"',

  'CHANNEL_DIRECTION': '"<-"',

  'PLUS_PLUS': '"++"',

  'MINUS_MINUS': '"--"',

  'BIT_AND_NOT_ASSIGN': '"&^="',

  'BIT_AND_ASSIGN': '"&="',

  'BIT_OR_ASSIGN': '"|="',

  'BIT_XOR_ASSIGN': '"^="',

  'LEFT_SHIFT_ASSIGN': '"<<="',

  'RIGHT_SHIFT_ASSIGN': '">>="',

  'PLUS_ASSIGN': '"+="',

  'MINUS_ASSIGN': '"-="',

  'MULTIPLY_ASSIGN': '"*="',

  'DIVIDE_ASSIGN': '"/="',

  'REMAINDER_ASSIGN': '"%="',

  'BIT_AND_NOT': '"&^"',

  'BIT_AND': '"&"',

  'BIT_OR': '"|"',

  'BIT_XOR': '"^"',

  'LEFT_SHIFT': '"<<"',

  'RIGHT_SHIFT': '">>"',

  'PLUS': '"+"',

  'MINUS': '"-"',

  'MULTIPLY': '"*"',

  'DIVIDE': '"/"',

  'REMAINDER': '"%"',

  'EQUAL': '"=="',

  'LESS': '"<"',

  'GREATER': '">"',

  'ASSIGN': '"="',

  'NOT': '"!"',

  'TILDE': '"~"'
}

# Em Go, apesar de '_42' ser um identificador, '0x_42' é válido.
numeros = \
{
  # Digitos Unitários
  '#BINARY_DIGIT': '"0" | "1"',

  '#OCTAL_DIGIT': '["0"-"7"]',

  '#DECIMAL_DIGIT': '["0"-"9"]',

  '#HEX_DIGIT': '["0"-"9", "A"-"F", "a"-"f"]',


  # Digitos Combinados
  '#BINARY_DIGITS': f'''< {adaptar('BINARY_DIGIT')} > ( ("_")? < {adaptar('BINARY_DIGIT')} > )*''',
  
  '#OCTAL_DIGITS': f'''< {adaptar('OCTAL_DIGIT')} > ( ("_")? < {adaptar('OCTAL_DIGIT')} > )*''',

  '#DECIMAL_DIGITS': f'''< {adaptar('DECIMAL_DIGIT')} > ( ("_")? < {adaptar('DECIMAL_DIGIT')} > )*''',

  '#HEX_DIGITS': f'''< {adaptar('HEX_DIGIT')} > ( ("_")? < {adaptar('HEX_DIGIT')} > )*''',


  # Números Inteiros
  'BINARY_LITERAL': f'''"0" ("b" | "B") ("_")? < {adaptar('BINARY_DIGITS')}  >''',

  'OCTAL_LITERAL': f'''"0" ("o" | "O")? ("_")? < {adaptar('OCTAL_DIGITS')} >''',

  'DECIMAL_LITERAL': f'''"0" | ( ["1"-"9"] ( ("_")? < {adaptar('DECIMAL_DIGITS')} > )? )''',

  'HEX_LITERAL': f'''"0" ("x" | "X") ("_")? < {adaptar('HEX_DIGITS')} >''',

  '#INT_LITERAL': 
    f'''< {adaptar('BINARY_LITERAL')} > | < {adaptar('OCTAL_LITERAL')} > | ''' +
    f'''< {adaptar('DECIMAL_LITERAL')} > | < {adaptar('HEX_LITERAL')} >''',


  # Mantissas e Expoentes
  '#DECIMAL_EXPONENT': f'''("e" | "E") ("+" | "-")? < {adaptar('DECIMAL_DIGITS')} >''',

  '#HEX_MANTISSA': 
    f'''( ("_")? < {adaptar('HEX_DIGITS')} > "." (< {adaptar('HEX_DIGITS')} >)? ) | ''' +
    f'''( ("_")? < {adaptar('HEX_DIGITS')} > ) | ''' +
    f'''( "." < {adaptar('HEX_DIGITS')} > )''',

  '#HEX_EXPONENT': f'''("p" | "P") ("+" | "-")? < {adaptar('DECIMAL_DIGITS')} >''',


  # Pontos Flutuantes
  'DECIMAL_FLOAT_LITERAL': 
    f'''( < {adaptar('DECIMAL_DIGITS')} > "." ( < {adaptar('DECIMAL_DIGITS')} > )? ( < {adaptar('DECIMAL_EXPONENT')} > )? ) | ''' +
    f'''( < {adaptar('DECIMAL_DIGITS')} > < {adaptar('DECIMAL_EXPONENT')} > ) | ''' +
    f'''( "." < {adaptar('DECIMAL_DIGITS')} > ( < {adaptar('DECIMAL_EXPONENT')} > )? )''',

  'HEX_FLOAT_LITERAL': f'''"0" ("x" | "X") < {adaptar('HEX_MANTISSA')} > < {adaptar('HEX_EXPONENT')} >''',

  '#FLOAT_LITERAL':
    f'''< {adaptar('DECIMAL_FLOAT_LITERAL')} > | < {adaptar('HEX_FLOAT_LITERAL')} >''',


  # Números Imaginários
  'IMAGINARY_LITERAL': 
    f'''(< {adaptar('DECIMAL_DIGITS')} > | ''' +
    f'''< {adaptar('INT_LITERAL')} > | < {adaptar('FLOAT_LITERAL')} >) ''' +
    f'''"i"'''
}

# Go usa caracteres unicode para identificadores.
# Traduzi `unicode_letter` para `["A"-"Z", "a"-"z"]`.
# Traduzi `unicode_digit` para `["0"-"9"]`.
identificadores = \
{
  '#LETTER': '"_" | ["A"-"Z", "a"-"z"]',

  'IDENTIFIER': 
    f'''< {adaptar('LETTER')} > ( < {adaptar('LETTER')} > | < {adaptar('DECIMAL_DIGIT')} > )*'''
}

runas = \
{
  # {3} significa 3 digitos octais.
  '#OCTAL_BYTE_VALUE': f'''"\\\\" (< {adaptar('OCTAL_DIGIT')} >){{3}}''',
  
  '#HEX_BYTE_VALUE': f'''"\\\\" "x" (< {adaptar('HEX_DIGIT')} >){{2}}''',

  '#LITTLE_U_VALUE': f'''"\\\\" "u" (< {adaptar('HEX_DIGIT')} >){{4}}''',

  '#BIG_U_VALUE': f'''"\\\\" "U" (< {adaptar('HEX_DIGIT')} >){{8}}''',

  '#ESCAPED_CHAR': f'''"\\\\" ( "a" | "b" | "f" | "n" | "r" | "t" | "v" | "\\\\" | "'" | "\\"" )''',

  '#BYTE_VALUE': f'''< {adaptar('OCTAL_BYTE_VALUE')} > | < {adaptar('HEX_BYTE_VALUE')} >''',

  # Deveria ser #UNICODE_VALUE, mas como usa #LETTER, tornei #LETTER_VALUE.
  '#LETTER_VALUE': 
    f'''< {adaptar('LETTER')} > | ''' +
    f'''< {adaptar('LITTLE_U_VALUE')} > | ''' +
    f'''< {adaptar('BIG_U_VALUE')} > | ''' +
    f'''< {adaptar('ESCAPED_CHAR')} >''',

  'RUNE_LITERAL': f'''"'" ( < {adaptar('LETTER_VALUE')} > | < {adaptar('BYTE_VALUE')} > ) "'"'''
}

# Listando todas as listas de tokens
listas_de_tokens_normais = \
{
  'Tipos': tipos,

  'Constantes': constantes,

  'Funções': funcoes,

  'Palavras-Chave': palavras_chave,

  'Valor Zero': valor_zero
}

listas_de_tokens_especiais = \
{
  'Comentários': comentarios,

  'Operadores': operadores,

  'Números': numeros,

  'Identificadores': identificadores,

  'Runas': runas
}

# Início dos prints.

ultimo_token_da_ultima_lista = \
  list( (list(listas_de_tokens_especiais.values())[-1]).keys() )[-1]

# Implementa a classe base.
print(f'''\
PARSER_BEGIN({nome_da_classe})

public class {nome_da_classe}
{{
  public static void main(String args[]) throws ParseException, TokenMgrError
  {{
    {nome_da_classe} parser = new {nome_da_classe}(System.in);

    parser.Inicio();
  }}
}}

PARSER_END({nome_da_classe})

''')

# SKIP
print(f'''\
SKIP:
{{
  /** Espaços em Branco */
  " "
| "\\t"
| "\\n"
| "\\r"
}}
''')

# TOKEN
print('TOKEN:',
      '{',
      sep = '\n')

## Tokens Normais
for nome_lista, lista in listas_de_tokens_normais.items():
  print(f'  /** {nome_lista} */')

  for token in lista:
    print(f'  < {adaptar(token)}: "{token.lower()}" >',
          f'|',
          sep = '\n')

## Tokens Especiais
for nome_lista, lista in listas_de_tokens_especiais.items():
  print(f'  /** {nome_lista} */')

  for nome_token, valor_token in lista.items():
      print(f'  < {adaptar(nome_token)}: {valor_token} >',
            f'|' if nome_token != ultimo_token_da_ultima_lista else '}\n\n',
            sep = '\n')


# Implementação da função de início.
print(f'''\
void Inicio():
{{
  Token t;
}}
{{
  (\
''')

for nome_lista, lista in listas_de_tokens_normais.items():
  for token in lista:
    print(f'    t = < {adaptar(token)} >',
          f'    {{',
          f'      System.out.println("{adaptar(token)} " + t.image);',
          f'    }}',
          f'',
          f'    |',
          f'',
          sep = '\n')

for nome_lista, lista in listas_de_tokens_especiais.items():
  for nome_token, valor_token in lista.items():
    if eh_token_final(nome_token) == False:
      continue

    print(f'    t = < {adaptar(nome_token)} >',
          f'    {{',
          f'      System.out.println("{adaptar(nome_token)} " + t.image);',
          f'    }}',
          sep = '\n')

    if nome_token != ultimo_token_da_ultima_lista:
      print(f'',
            f'    |',
            f'',
            sep = '\n')

print(f'''\
  )*

  < EOF >
}}\
''')
