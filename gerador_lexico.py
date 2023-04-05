# Programa para gerar código em JavaCC de reconhecimento léxico da linguagem Go.

nome_da_classe = 'Compilador'
prefixo_token = 'TOKEN_'
posfixo_token = ''

# Modo: 0 para Site, 1 para Programa de Alberto
modo = 0

# Responde se o token é ou não final. 
# Por ex.: digitos que comporão números não são tokens finais.
def eh_token_final(nome_do_token):
  if nome_do_token[0] == '#':
    return False

  return True

# Adapta o nome do token, usando prefixos e sufixos pré-definidos.
def tokenizar(nome_do_token):
  nome_final = None

  # Para tokens que não sejam finais, como digitos que comporão números.
  if eh_token_final(nome_do_token) == False:
    nome_final = '#' + prefixo_token + nome_do_token[1:] + posfixo_token

  else:
    nome_final = prefixo_token + nome_do_token + posfixo_token

  return nome_final.upper()

def tk(x):
    if len(x) == 1:
        return "PROVAVEL_ERRO" * 1000
    return tokenizar(x)

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
  '#LETTER': f'''"_" | < {tk('UNICODE_LETTER')} >''',

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
  '#BINARY_DIGITS': f'''< {tk('BINARY_DIGIT')} > ( ("_")? < {tk('BINARY_DIGIT')} > )*''',
  
  '#OCTAL_DIGITS': f'''< {tk('OCTAL_DIGIT')} > ( ("_")? < {tk('OCTAL_DIGIT')} > )*''',

  '#DECIMAL_DIGITS': f'''< {tk('DECIMAL_DIGIT')} > ( ("_")? < {tk('DECIMAL_DIGIT')} > )*''',

  '#HEX_DIGITS': f'''< {tk('HEX_DIGIT')} > ( ("_")? < {tk('HEX_DIGIT')} > )*''',


  # Números Inteiros
  'BINARY_LITERAL': [f'''"0" ("b" | "B") ("_")? < {tk('BINARY_DIGITS')}  >''', 'NLSEMI'],

  'OCTAL_LITERAL': [f'''"0" ("o" | "O")? ("_")? < {tk('OCTAL_DIGITS')} >''', 'NLSEMI'],

  'DECIMAL_LITERAL': [f'''"0" | ( ["1"-"9"] ( ("_")? < {tk('DECIMAL_DIGITS')} > )? )''', 'NLSEMI'],

  'HEX_LITERAL': [f'''"0" ("x" | "X") ("_")? < {tk('HEX_DIGITS')} >''', 'NLSEMI'],

  '#INT_LITERAL': 
    f'''< {tk('BINARY_LITERAL')} > | < {tk('OCTAL_LITERAL')} > | ''' +
    f'''< {tk('DECIMAL_LITERAL')} > | < {tk('HEX_LITERAL')} >''',


  # Mantissas e Expoentes
  '#DECIMAL_EXPONENT': f'''("e" | "E") ("+" | "-")? < {tk('DECIMAL_DIGITS')} >''',

  '#HEX_MANTISSA': 
    f'''( ("_")? < {tk('HEX_DIGITS')} > "." (< {tk('HEX_DIGITS')} >)? ) | ''' +
    f'''( ("_")? < {tk('HEX_DIGITS')} > ) | ''' +
    f'''( "." < {tk('HEX_DIGITS')} > )''',

  '#HEX_EXPONENT': f'''("p" | "P") ("+" | "-")? < {tk('DECIMAL_DIGITS')} >''',


  # Pontos Flutuantes
  'DECIMAL_FLOAT_LITERAL': 
    [f'''( < {tk('DECIMAL_DIGITS')} > "." ( < {tk('DECIMAL_DIGITS')} > )? ( < {tk('DECIMAL_EXPONENT')} > )? ) | ''' +
    f'''( < {tk('DECIMAL_DIGITS')} > < {tk('DECIMAL_EXPONENT')} > ) | ''' +
    f'''( "." < {tk('DECIMAL_DIGITS')} > ( < {tk('DECIMAL_EXPONENT')} > )? )''', 'NLSEMI'],

  'HEX_FLOAT_LITERAL': [f'''"0" ("x" | "X") < {tk('HEX_MANTISSA')} > < {tk('HEX_EXPONENT')} >''', 'NLSEMI'],

  '#FLOAT_LITERAL':
    f'''< {tk('DECIMAL_FLOAT_LITERAL')} > | < {tk('HEX_FLOAT_LITERAL')} >''',


  # Números Imaginários
  'IMAGINARY_LITERAL': 
    [f'''(< {tk('DECIMAL_DIGITS')} > | ''' +
    f'''< {tk('INT_LITERAL')} > | < {tk('FLOAT_LITERAL')} >) ''' +
    f'''"i"''', 'NLSEMI']
}

runas = \
{
  # {3} significa 3 digitos octais.
  '#OCTAL_BYTE_VALUE': f'''"\\\\" (< {tk('OCTAL_DIGIT')} >){{3}}''',
  
  '#HEX_BYTE_VALUE': f'''"\\\\" "x" (< {tk('HEX_DIGIT')} >){{2}}''',

  '#LITTLE_U_VALUE': f'''"\\\\" "u" (< {tk('HEX_DIGIT')} >){{4}}''',

  '#BIG_U_VALUE': f'''"\\\\" "U" (< {tk('HEX_DIGIT')} >){{8}}''',

  '#ESCAPED_CHAR': f'''"\\\\" ( "a" | "b" | "f" | "n" | "r" | "t" | "v" | "\\\\" | "'" | "\\"" )''',

  '#BYTE_VALUE': f'''< {tk('OCTAL_BYTE_VALUE')} > | < {tk('HEX_BYTE_VALUE')} >''',

  '#UNICODE_VALUE': 
    f'''< {tk('UNICODE_CHAR')} > | ''' +
    f'''< {tk('LITTLE_U_VALUE')} > | ''' +
    f'''< {tk('BIG_U_VALUE')} > | ''' +
    f'''< {tk('ESCAPED_CHAR')} >''',

  'RUNE_LITERAL': [f'''"'" ( < {tk('UNICODE_VALUE')} > | < {tk('BYTE_VALUE')} > ) "'"''', 'NLSEMI']
}

strings = \
{
  '#STRING_LITERAL': 
    f'''< {tk('RAW_STRING_LITERAL')} > | < {tk('INTERPRETED_STRING_LITERAL')} >'''
}

identificadores = \
{
  'IDENTIFIER': 
    [f'''< {tk('LETTER')} > ( < {tk('LETTER')} > | < {tk('UNICODE_DIGIT')} > )*''', 'NLSEMI']
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
  # Nome do Estado Léxico
  'IN_RAW_STRING_LITERAL':
  {
    # Tokens que são gerados neste estado léxico.
    # Eles são gerados ao ler da entrada um dos 'Tokens de Evento'.
    # Assim que são gerados, vão para o 'Próximo Estado'.
    'TOKEN':
    {
      f'{tk("RAW_STRING_LITERAL")}':
      {
        'Tokens de Evento': ['"`"'],

        'Próximo Estado': 'NLSEMI'
      }
    },

    # More é a lista dos caracteres e tokens que serão ignorados ao ser lidos,
    # mas que futuramente comporão o token final. 
    'MORE':
    {
      f'{tk("IN_RAW_STRING_LITERAL_UNICODE_CHAR")}':
      {
        'Tokens de Evento': [f'{tk("UNICODE_CHAR")}']
      },

      f'{tk("IN_RAW_STRING_LITERAL_NEWLINE")}':
      {
        'Tokens de Evento': [f'{tk("NEWLINE")}']
      }
    },

    # É o caractere / token que ao ser lido, mudará do estado DEFAULT para este.
    'IN_DEFAULT_MORE': '"`"'
  },

  'IN_INTERPRETED_STRING_LITERAL':
  {
    'TOKEN':
    {
      f'{tk("INTERPRETED_STRING_LITERAL")}':
      {
        'Tokens de Evento': '"\\""',
        
        'Próximo Estado': 'NLSEMI'
      }
    },

    'MORE':
    {
      '"\\\\\\""': {},

      f'{tk("IN_INTERPRETED_STRING_LITERAL_UNICODE_VALUE")}':
      {
        'Tokens de Evento': [f'{tk("UNICODE_VALUE")}']
      },

      f'{tk("IN_INTERPRETED_STRING_LITERAL_BYTE_VALUE")}':
      {
        'Tokens de Evento': [f'{tk("BYTE_VALUE")}']
      }
    },

    'IN_DEFAULT_MORE': '"\\""'
  },

  'NLSEMI':
  {
    'TOKEN': 
    {
      f'{tk("EOS")}': 
      {
        'Tokens de Evento': [f'{tk("NEWLINE")}', f'{tk("CARRIAGE_RETURN")}', f'{tk("GENERAL_COMMENT")}'],

        'Próximo Estado': 'DEFAULT'
      }
    },

    # Os caracteres que serão simplesmente ignorados ao ser lidos.
    'SKIP':
    {
      f'{tk("NLSEMI_SKIP_SPACE")}':
      {
        'Tokens de Evento': [f'{tk("SPACE")}']
      },

      f'{tk("NLSEMI_SKIP_HORIZONTAL_TAB")}':
      {
        'Tokens de Evento': [f'{tk("HORIZONTAL_TAB")}']
      }
    },

    'MORE':
    {
      '""':
      {
        'Próximo Estado': 'DEFAULT'
      }
    }
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

for nome_estado, acoes_lexicas in estados_lexicos.items():
  #print("Ações Léxicas:", acoes_lexicas)
  
  for nome_acao, itens_acao in acoes_lexicas.items():
    print(f'< {nome_estado} > {nome_acao}:',
          f'{{',
          sep = '\n')

    for nome_item, valor_item in itens_acao.items():
      print(f'  < {nome_item} : ', end='')

      if 'Tokens de Evento' in valor_item:
        tokens_de_evento = valor_item['Tokens de Evento']

        if len(tokens_de_evento) == 1:
          print(f'< {tokens_de_evento[0]} >')
        
        else:
          print(f'',
                f'    ')


# # Melhorar semântica
# for nome_estado, dados_estado in estados_lexicos.items():
#   # Printando '< ESTADO > TOKEN:'
#   print(f'''< {nome_estado} > TOKEN:''',
#         f'''{{''',
#         f'''  < {tk(dados_estado['TOKEN'][0][0])}: {dados_estado['TOKEN'][0][1]} > : {dados_estado['TOKEN'][1]}''',
#         f'''}}''',
#         f'''''',
#         sep = '\n')

#   # Printando '< ESTADO > MORE:'
#   print(f'''< {nome_estado} > MORE:''',
#         f'''{{''',
#         f'''  {dados_estado['MORE'][0]}''',
#         sep = '\n')

#   for regra in dados_estado['MORE'][1:]:
#     print(f'|',
#           f'  {regra}',
#           sep = '\n')

#   print('}\n')

# # MORE
# print ('MORE:',
#        '{',
#        sep = '\n')

# for nome_estado, dados_estado in estados_lexicos.items():
#   print(f'''  {dados_estado['IN_DEFAULT_MORE']}: {nome_estado}''',
#         '|' if nome_estado != list(estados_lexicos.keys())[-1] else '}\n\n',
#         sep = '\n')

# # SKIP
# print('SKIP:',
#       '{',
#       '  /** Espaços em Branco */',
#       sep = '\n')

# for nome_token, valor_token in espacos_brancos.items():
#   print(f'  < {tk(nome_token)}: {valor_token} >',
#         f'|' if nome_token != list(espacos_brancos.keys())[-1] else '}\n\n',
#         sep = '\n')

# TOKEN
print('TOKEN:',
      '{',
      sep = '\n')

## Tokens Normais
for nome_lista, lista in listas_de_tokens_normais.items():
  print(f'  /** {nome_lista} */')

  for token in lista:
    if isinstance(token, str):
      print(f'  < {tk(token)}: "{token.lower()}" >',
            f'|',
            sep = '\n')
    else:
      valor_token = token[0]
      prox_estado = token[1]
      print(f'  < {tk(valor_token)}: "{valor_token.lower()}" > : {prox_estado}',
            f'|',
            sep = '\n')

## Tokens Especiais
for nome_lista, lista in listas_de_tokens_especiais.items():
  print(f'  /** {nome_lista} */')

  for nome_token, valor_token in lista.items():
    if isinstance(valor_token, str):
      print(f'  < {tk(nome_token)}: {valor_token} >',
            f'|' if nome_token != ultimo_token_da_ultima_lista else '}\n\n',
            sep = '\n')
    else:
      prox_estado = valor_token[1]
      valor_token = valor_token[0]
      print(f'  < {tk(nome_token)}: {valor_token} > : {prox_estado}',
            f'|' if nome_token != ultimo_token_da_ultima_lista else '}\n\n',
            sep = '\n')


# Implementação da função de início.

# Printa imagem para o programa de Alberto e não printa para o uso no Site.
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
    if isinstance(token, str) == False:
      token = token[0]
    print(f'    t = < {tk(token)} >',
          f'    {{',
          f'      System.out.println("{tk(token)}"{imagem});',
          f'    }}',
          f'',
          f'    |',
          f'',
          sep = '\n')

# # Melhorar semântica
# for dados_estado in estados_lexicos.values():
#   print(f'''    t = < {tk(dados_estado['TOKEN'][0][0])} >''',
#         f'''    {{''',
#         f'''      System.out.println("{tk(dados_estado['TOKEN'][0][0])}"{imagem});''',
#         f'''    }}''',
#         f'''''',
#         f'''    |''',
#         f'''''',
#         sep = '\n')

for lista in listas_de_tokens_especiais.values():
  for nome_token, valor_token in lista.items():
    if eh_token_final(nome_token) == False:
      continue

    if isinstance(valor_token, str) == False:
      valor_token = valor_token[0]

    print(f'    t = < {tk(nome_token)} >',
          f'    {{',
          f'      System.out.println("{tk(nome_token)}"{imagem});',
          f'    }}',
          sep = '\n')

    if nome_token != ultimo_token_da_ultima_lista:
      print(f'',
            f'    |',
            f'',
            sep = '\n')

print(f'''\
  )*

  t = < EOF >
  {{
    System.out.println("{tk("EOF")}"{imagem});'
  }}
}}\
''')
