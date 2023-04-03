# Gramática Reduzida

prefixo_token = 'TOKEN_'
posfixo_token = ''

# Adapta o nome do token para a regra usada.
def tokenizar(nome_do_token):  
  nome_final = prefixo_token + nome_do_token + posfixo_token

  return nome_final.upper()

def tk(x):
    if len(x) == 1:
        return "PROVAVEL_ERRO" * 1000
    return tokenizar(x)

def op(x):
  if (x == '!='):
    return tk('DIFFERENT')

  if (x == '<='):
    return tk('LESS_EQUAL')

  if (x == '>='):
    return tk('GREATER_EQUAL')

  if (x == ':='):
    return tk('SHORT_DECLARATION')

  if (x == '...'):
    return tk('ELLIPSIS')

  if (x == '('):
    return tk('OPEN_PARENTHESIS')

  if (x == ')'):
    return tk('CLOSE_PARENTHESIS')

  if (x == '['):
    return tk('OPEN_BRACKET')

  if (x == ']'):
    return tk('CLOSE_BRACKET')

  if (x == '{'):
    return tk('OPEN_BRACE')

  if (x == '}'):
    return tk('CLOSE_BRACE')

  if (x == ','):
    return tk('COMMA')

  if (x == ';'):
    return tk('SEMICOLON')

  if (x == '.'):
    return tk('DOT')

  if (x == ':'):
    return tk('COLON')

  if (x == '&&'):
    return tk('AND')

  if (x == '||'):
    return tk('OR')

  if (x == '<-'):
    return tk('CHANNEL_DIRECTION')

  if (x == '++'):
    return tk('PLUS_PLUS')

  if (x == '--'):
    return tk('MINUS_MINUS')

  if (x == '&^='):
    return tk('BIT_AND_NOT_ASSIGN')

  if (x == '&='):
    return tk('BIT_AND_ASSIGN')

  if (x == '|='):
    return tk('BIT_OR_ASSIGN')

  if (x == '^='):
    return tk('BIT_XOR_ASSIGN')

  if (x == '<<='):
    return tk('LEFT_SHIFT_ASSIGN')

  if (x == '>>='):
    return tk('RIGHT_SHIFT_ASSIGN')

  if (x == '+='):
    return tk('PLUS_ASSIGN')

  if (x == '-='):
    return tk('MINUS_ASSIGN')

  if (x == '*='):
    return tk('MULTIPLY_ASSIGN')

  if (x == '/='):
    return tk('DIVIDE_ASSIGN')

  if (x == '%='):
    return tk('REMAINDER_ASSIGN')

  if (x == '&^'):
    return tk('BIT_AND_NOT')

  if (x == '&'):
    return tk('BIT_AND')

  if (x == '|'):
    return tk('BIT_OR')

  if (x == '^'):
    return tk('BIT_XOR')

  if (x == '<<'):
    return tk('LEFT_SHIFT')

  if (x == '>>'):
    return tk('RIGHT_SHIFT')

  if (x == '+'):
    return tk('PLUS')

  if (x == '-'):
    return tk('MINUS')

  if (x == '*'):
    return tk('MULTIPLY')

  if (x == '/'):
    return tk('DIVIDE')

  if (x == '%'):
    return tk('REMAINDER')

  if (x == '=='):
    return tk('EQUAL')

  if (x == '<'):
    return tk('LESS')

  if (x == '>'):
    return tk('GREATER')

  if (x == '='):
    return tk('ASSIGN')

  if (x == '!'):
    return tk('NOT')

  if (x == '~'):
    return tk('TILDE')
  return "ERRO" * 1000

arquivo_fonte = \
{
    'ArquivoFonte':
    [
        'PackageClause ImportDecl?'
    ],

    'ImportDecl?':
    [
        '',
        'ImportDecl'
    ]
}

clausula_pacote = \
{
    'PackageClause': 
    [
        f'{tk("package")} PackageName'
    ],

    'PackageName':
    [
        # Não deve aceitar o identificador 'blank': "_"
        f'{tk("identifier")}'
    ]
}

declaracao_import = \
{
    'ImportDecl':
    [
        f'{tk("import")} ImportSpec',
        f'{tk("import")} {op("(")} ImportDeclSp* {op(")")}'
    ],

    'ImportDeclSp*':
    [
        '',
        f'ImportSpec {op(";")}? ImportDeclSp*'
    ],

    'ImportSpec':
    [
        'ImportSpecSp? ImportPath'
    ],

    'ImportSpecSp?':
    [
        '',
        f'{op(".")}',
        'PackageName'
    ],

    'ImportPath':
    [
        'stringLiteral'
    ]
}

declaracao_funcao = \
{
    'FunctionDecl':
    [
        f'{tk("func")} FunctionName'
    ],

    'FunctionName':
    [
        f'{tk("identifier")}'
    ],

    # 'FunctionBody':
    # [
    #     'Block'
    # ]
}

string = \
{
    'stringLiteral':
    [
        f'{tk("RAW_STRING_LITERAL")}',
        f'{tk("INTERPRETED_STRING_LITERAL")}'
    ]
}

tokens_finais_condicionais = \
{
    f'{op(";")}?':
    [
        '',
        f'{op(";")}'
    ]
}

listas = \
{
    'Go': go,

    'Cláusula de Pacote': clausula_pacote,
    'Declaração de Import': declaracao_import,
    'Declaração de Função': declaracao_funcao,

    'String': string,
    'Tokens Finais Condicionais': tokens_finais_condicionais
}

# Modo: 0 para Site, 1 para Programa de Alberto
#modo = int(input())
modo = 0

for nome_lista, lista in listas.items():
    for nome_regra, valores_regra in lista.items():
        for valor in valores_regra:
            print(nome_regra, ' -> ', "''" if valor == '' and modo == 0 else valor, sep='')
#        print()
#    print()
