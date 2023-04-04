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

# Adapta o nome do token, usando prefixos e sufixos pré-definidos.
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

palavras_chave = [ ['BREAK', 'NLSEMI'], 'DEFAULT', 'FUNC', 'INTERFACE', 'SELECT', 'CASE',
                   'DEFER', 'GO', 'MAP', 'STRUCT', 'CHAN', 'ELSE', 'GOTO',
                   'PACKAGE', 'SWITCH', 'CONST', ['FALLTHROUGH', 'NLSEMI'], 'IF', 'RANGE',
                   'TYPE', ['CONTINUE', 'NLSEMI'], 'FOR', 'IMPORT', ['RETURN', 'NLSEMI'], 'VAR' ]

# Vai pra NLSEMI porque funciona como um literal.
valor_zero = [ ['NIL', 'NLSEMI'] ]

# Tokens especiais: seus nomes e valores são distintos.
comentarios = \
{
  'LINE_COMMENT': f'''"//" (~["\\n", "\\r"])*''',
  'GENERAL_COMMENT': '"/*" (~[])* "*/"' 
}

espacos_brancos = \
{
  'SPACE': '" "',
  'HORIZONTAL_TAB': '"\\t"',
  'CARRIAGE_RETURN': '"\\r"',
  'NEWLINE': '"\\n"'
}

# Esses tokens (não finais) são referenciados em outros tokens.
unicode = \
{
  '#UNICODE_CHAR': '~["\\n"]',

  # Tecnicamente, teria que aceitar todas as letras do Unicode.
  # Neste momento, por simplicidade, aceita apenas as letras latinas sem acento.
  '#UNICODE_LETTER': '["A"-"Z", "a"-"z"]',

  # Tecnicamente, teria que aceitar todos os digitos do Unicode.
  # Neste momento, por simplicidade, aceita apenas digitos de 0 a 9.
  '#UNICODE_DIGIT': '["0"-"9"]'
}

# Esses tokens (não finais) são referenciados em outros tokens.
letras_e_digitos = \
{
  '#LETTER': f'''"_" | < {adaptar('UNICODE_LETTER')} >''',

  # Digitos Unitários
  '#BINARY_DIGIT': '"0" | "1"',

  '#OCTAL_DIGIT': '["0"-"7"]',

  '#DECIMAL_DIGIT': '["0"-"9"]',

  '#HEX_DIGIT': '["0"-"9", "A"-"F", "a"-"f"]',
}

operadores = \
{
  'DIFFERENT': '"!="',

  'LESS_EQUAL': '"<="',

  'GREATER_EQUAL': '">="',

  'SHORT_DECLARATION': '":="',

  'ELLIPSIS': '"..."',

  'OPEN_PARENTHESIS': '"("',

  'CLOSE_PARENTHESIS': ['")"', 'NLSEMI'],

  'OPEN_BRACKET': '"["',

  'CLOSE_BRACKET': ['"]"', 'NLSEMI'],

  'OPEN_BRACE': '"{"',

  'CLOSE_BRACE': ['"}"', 'NLSEMI'],

  'COMMA': '","',

  'SEMICOLON': '";"',

  'DOT': '"."',

  'COLON': '":"',

  'AND': '"&&"',

  'OR': '"||"',

  'CHANNEL_DIRECTION': '"<-"',

  'PLUS_PLUS': ['"++"', 'NLSEMI'],

  'MINUS_MINUS': ['"--"', 'NLSEMI'],

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

# Em Go, apesar de '_42' ser um identificador, '0x_42' é um número literal válido.
numeros = \
{
  # Digitos Combinados
  '#BINARY_DIGITS': f'''< {adaptar('BINARY_DIGIT')} > ( ("_")? < {adaptar('BINARY_DIGIT')} > )*''',
  
  '#OCTAL_DIGITS': f'''< {adaptar('OCTAL_DIGIT')} > ( ("_")? < {adaptar('OCTAL_DIGIT')} > )*''',

  '#DECIMAL_DIGITS': f'''< {adaptar('DECIMAL_DIGIT')} > ( ("_")? < {adaptar('DECIMAL_DIGIT')} > )*''',

  '#HEX_DIGITS': f'''< {adaptar('HEX_DIGIT')} > ( ("_")? < {adaptar('HEX_DIGIT')} > )*''',


  # Números Inteiros
  'BINARY_LITERAL': [f'''"0" ("b" | "B") ("_")? < {adaptar('BINARY_DIGITS')}  >''', 'NLSEMI'],

  'OCTAL_LITERAL': [f'''"0" ("o" | "O")? ("_")? < {adaptar('OCTAL_DIGITS')} >''', 'NLSEMI'],

  'DECIMAL_LITERAL': [f'''"0" | ( ["1"-"9"] ( ("_")? < {adaptar('DECIMAL_DIGITS')} > )? )''', 'NLSEMI'],

  'HEX_LITERAL': [f'''"0" ("x" | "X") ("_")? < {adaptar('HEX_DIGITS')} >''', 'NLSEMI'],

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
    [f'''( < {adaptar('DECIMAL_DIGITS')} > "." ( < {adaptar('DECIMAL_DIGITS')} > )? ( < {adaptar('DECIMAL_EXPONENT')} > )? ) | ''' +
    f'''( < {adaptar('DECIMAL_DIGITS')} > < {adaptar('DECIMAL_EXPONENT')} > ) | ''' +
    f'''( "." < {adaptar('DECIMAL_DIGITS')} > ( < {adaptar('DECIMAL_EXPONENT')} > )? )''', 'NLSEMI'],

  ['HEX_FLOAT_LITERAL': f'''"0" ("x" | "X") < {adaptar('HEX_MANTISSA')} > < {adaptar('HEX_EXPONENT')} >''', 'NLSEMI'],

  '#FLOAT_LITERAL':
    f'''< {adaptar('DECIMAL_FLOAT_LITERAL')} > | < {adaptar('HEX_FLOAT_LITERAL')} >''',


  # Números Imaginários
  'IMAGINARY_LITERAL': 
    [f'''(< {adaptar('DECIMAL_DIGITS')} > | ''' +
    f'''< {adaptar('INT_LITERAL')} > | < {adaptar('FLOAT_LITERAL')} >) ''' +
    f'''"i"''', 'NLSEMI']
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

  '#UNICODE_VALUE': 
    f'''< {adaptar('UNICODE_CHAR')} > | ''' +
    f'''< {adaptar('LITTLE_U_VALUE')} > | ''' +
    f'''< {adaptar('BIG_U_VALUE')} > | ''' +
    f'''< {adaptar('ESCAPED_CHAR')} >''',

  'RUNE_LITERAL': [f'''"'" ( < {adaptar('UNICODE_VALUE')} > | < {adaptar('BYTE_VALUE')} > ) "'"''', 'NLSEMI']
}

strings = \
{
  '#STRING_LITERAL': 
    f'''< {adaptar('RAW_STRING_LITERAL')} > | < {adaptar('INTERPRETED_STRING_LITERAL')} >'''
}

identificadores = \
{
  'IDENTIFIER': 
    [f'''< {adaptar('LETTER')} > ( < {adaptar('LETTER')} > | < {adaptar('UNICODE_DIGIT')} > )*''', 'NLSEMI']
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
  'Unicode': unicode,

  'Letras & Digitos': letras_e_digitos,

  'Comentários': comentarios,

  'Operadores': operadores,

  'Números': numeros,

  'Runas': runas,

  'Strings': strings,

  'Identificadores': identificadores
}

'''
  Por padrão, JavaCC analisa o código no estado DEFAULT.
  As regras de TOKEN, SKIP e MORE são definidas somente para este estado.
  Quando dentro de `MORE: `, temos uma regra, como `"/*": IN_GENERAL_COMMENT`, isso significa que,
quando o JAVACC ler `/*` do código, ele irá para o estado `IN_GENERAL_COMMENT`.
  Dessa forma, precisamos definir as regras que serão válidas neste estado. Para este exemplo, as
regras são definidas dentro de: `< IN_GENERAL_COMMENT > TOKEN:` e `< IN_GENERAL_COMMENT > MORE:`.
  `< IN_GENERAL_COMMENT > TOKEN:` nos diz que quando um caractere lido casar com alguma regra
definida lá dentro, haverá uma criação de um token, e a transição de volta ao estado DEFAULT.
  `< IN_GENERAL_COMMENT > MORE:` nos diz que quando um caractere lido casar com alguma regra
definida lá dentro, ele será pulado, mas fará parte do próximo token a ser criado.
'''
estados_lexicos = \
{
  'IN_RAW_STRING_LITERAL':
  {
    # 'TOKEN' será printado dentro de `< IN_RAW_STRING_LITERAL > TOKEN:`
    # É uma tupla de dois elementos: 
    #   Elemento 1: nome do token a ser gerado
    #   Elemento 2: caractere que ao ser lido neste estado gerará o token
    'TOKEN': ('RAW_STRING_LITERAL', '"`"'),

    # 'MORE' será printado dentro de `< IN_RAW_STRING_LITERAL > MORE:`
    # É uma lista dos caracteres que serão ignorados ao ser lidos neste estado, mas que comporão o token final
    'MORE': [f'''< {adaptar('IN_RAW_STRING_LITERAL_UNICODE_CHAR')}: < {adaptar('UNICODE_CHAR')} > >''', 
             f'''< {adaptar('IN_RAW_STRING_LITERAL_NEWLINE')}: < {adaptar('NEWLINE')} > >'''],

    # 'IN_DEFAULT_MORE' será printado em `MORE:`
    # É o caractere que ao ser lido, mudará do estado DEFAULT para IN_RAW_STRING_LITERAL
    'IN_DEFAULT_MORE': '"`"'
  },

  'IN_INTERPRETED_STRING_LITERAL':
  {
    'TOKEN': ('INTERPRETED_STRING_LITERAL', '"\\""'),
    'MORE': ['"\\\\\\""',
             f'''< {adaptar('IN_INTERPRETED_STRING_LITERAL_UNICODE_VALUE')}: < {adaptar('UNICODE_VALUE')} > >''',
             f'''< {adaptar('IN_INTERPRETED_STRING_LITERAL_BYTE_VALUE')}: < {adaptar('BYTE_VALUE')} > >'''],
    'IN_DEFAULT_MORE': '"\\""'
  }
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

# Comentário descrevendo como funcionam os estados léxicos.
print('''\
/*
  Por padrão, JavaCC analisa o código no estado DEFAULT.
  As regras de TOKEN, SKIP e MORE são definidas somente para este estado.
  Quando dentro de `MORE: `, temos uma regra, como `"/*": IN_GENERAL_COMMENT`, isso significa que,
quando o JAVACC ler `/*` do código, ele irá para o estado `IN_GENERAL_COMMENT`.
  Dessa forma, precisamos definir as regras que serão válidas neste estado. Para este exemplo, as
regras são definidas dentro de: `< IN_GENERAL_COMMENT > TOKEN:` e `< IN_GENERAL_COMMENT > MORE:`.
  `< IN_GENERAL_COMMENT > TOKEN:` nos diz que quando um caractere lido casar com alguma regra
definida lá dentro, haverá uma criação de um token, e a transição de volta ao estado DEFAULT.
  `< IN_GENERAL_COMMENT > MORE:` nos diz que quando um caractere lido casar com alguma regra
definida lá dentro, ele será pulado, mas fará parte do próximo token a ser criado.
*/\
''')

for nome_estado, dados_estado in estados_lexicos.items():
  # Printando '< ESTADO > TOKEN:'
  print(f'''< {nome_estado} > TOKEN:''',
        f'''{{''',
        f'''  < {adaptar(dados_estado['TOKEN'][0])}: {dados_estado['TOKEN'][1]} > : DEFAULT''',
        f'''}}''',
        f'''''',
        sep = '\n')

  # Printando '< ESTADO > MORE:'
  print(f'''< {nome_estado} > MORE:''',
        f'''{{''',
        f'''  {dados_estado['MORE'][0]}''',
        sep = '\n')

  for regra in dados_estado['MORE'][1:]:
    print(f'|',
          f'  {regra}',
          sep = '\n')

  print('}\n')

# MORE
print ('MORE:',
       '{',
       sep = '\n')

for nome_estado, dados_estado in estados_lexicos.items():
  print(f'''  {dados_estado['IN_DEFAULT_MORE']}: {nome_estado}''',
        '|' if nome_estado != list(estados_lexicos.keys())[-1] else '}\n\n',
        sep = '\n')

# SKIP
print('SKIP:',
      '{',
      '  /** Espaços em Branco */',
      sep = '\n')

for nome_token, valor_token in espacos_brancos.items():
  print(f'  < {adaptar(nome_token)}: {valor_token} >',
        f'|' if nome_token != list(espacos_brancos.keys())[-1] else '}\n\n',
        sep = '\n')

# TOKEN
print('TOKEN:',
      '{',
      sep = '\n')

## Tokens Normais
for nome_lista, lista in listas_de_tokens_normais.items():
  print(f'  /** {nome_lista} */')

  for token in lista:
    if isinstance(token, str):
      print(f'  < {adaptar(token)}: "{token.lower()}" >',
            f'|',
            sep = '\n')
    else:
      valor_token = token[0]
      prox_estado = token[1]
      print(f'  < {adaptar(valor_token)}: "{valor_token.lower()}" > : {prox_estado}',
            f'|',
            sep = '\n')

## Tokens Especiais
for nome_lista, lista in listas_de_tokens_especiais.items():
  print(f'  /** {nome_lista} */')

  for nome_token, valor_token in lista.items():
    if isinstance(valor_token, str):
      print(f'  < {adaptar(nome_token)}: {valor_token} >',
            f'|' if nome_token != ultimo_token_da_ultima_lista else '}\n\n',
            sep = '\n')
    else:
      prox_estado = valor_token[1]
      valor_token = valor_token[0]
      print(f'  < {adaptar(nome_token)}: {valor_token} > : {prox_estado}',
            f'|' if nome_token != ultimo_token_da_ultima_lista else '}\n\n',
            sep = '\n')


# Implementação da função de início.

# Modo: 0 para Site, 1 para Programa de Alberto
modo = 1

imagem = ''
if modo == 1:
  imagem = ' + " " + t.image'

print(f'''\
void Inicio():
{{
  Token t;
}}
{{
  (\
''')

for lista in listas_de_tokens_normais.values():
  for token in lista:
    print(f'    t = < {adaptar(token)} >',
          f'    {{',
          f'      System.out.println("{adaptar(token)}"{imagem});',
          f'    }}',
          f'',
          f'    |',
          f'',
          sep = '\n')

for dados_estado in estados_lexicos.values():
  print(f'''    t = < {adaptar(dados_estado['TOKEN'][0])} >''',
        f'''    {{''',
        f'''      System.out.println("{adaptar(dados_estado['TOKEN'][0])}"{imagem});''',
        f'''    }}''',
        f'''''',
        f'''    |''',
        f'''''',
        sep = '\n')

for lista in listas_de_tokens_especiais.values():
  for nome_token, valor_token in lista.items():
    if eh_token_final(nome_token) == False:
      continue

    print(f'    t = < {adaptar(nome_token)} >',
          f'    {{',
          f'      System.out.println("{adaptar(nome_token)}"{imagem});',
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
