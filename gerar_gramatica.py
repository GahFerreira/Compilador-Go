# Algoritmo para gerar gramatica para Go

''' 
Nota sobre ponto e vírgula (;):
  Na especificação, é citado que:
"
The formal syntax uses semicolons ";" as terminators in a number of productions. Go programs may omit most of these semicolons using the following two rules:

    1. When the input is broken into tokens, a semicolon is automatically inserted into the token stream immediately after a line's final token if that token is
        - an identifier
        - an integer, floating-point, imaginary, rune, or string literal
        - one of the keywords break, continue, fallthrough, or return
        - one of the operators and punctuation ++, --, ), ], or }

    2. To allow complex statements to occupy a single line, a semicolon may be omitted before a closing ")" or "}".
"
No momento, a implementação não segue esse padrão.
Cada ";" obrigatório antes de fecha parenteses ( ")" ) ou chaves ( "}" ), foi substituído por um ";" opcional no lugar.
Isso acontece por exemplo na declaração de elementos de Struct & Interface.
'''


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

# Todas as regras do caso '[ regra ]' caem aqui.
condicional_1 = \
{
    # Regras para tokens léxicos (terminais)
    # Comma
    f'{op(",")}?':
    [
        '',
        f'{op(",")}'
    ],

    # Ellipsis
    f'{op("...")}?': #
    [
        '',
        f'{op("...")}'
    ],

    # Multiply
    f'{op("*")}?':
    [
        '',
        f'{op("*")}'
    ],

    # Semicolon
    f'{op(";")}?':
    [
        '',
        f'{op(";")}'
    ],

    # Regras para não-terminais
    'ArgumentsSp1?':
    [
        '',
        f'ExpressionList {op("...")} {op(",")}',
        f'Type ArgumentsSp2? {op("...")} {op(",")}'
    ],

    'ArgumentsSp2?':
    [
        '',
        f'{op(",")} ExpressionList'
    ],

    'Expression?':
    [
        '',
        'Expression'
    ],
    
    'FunctionBody?':
    [
        '',
        'FunctionBody'
    ],
    
    'IdentifierList?':
    [
        '',
        'IdentifierList'
    ],
    
    'Result?':
    [
        '',
        'Result'
    ], 

    'Tag?':
    [
        '',
        'Tag'
    ],

    'Type?':
    [
        '',
        'Type'
    ],

    'TypeArgs?':
    [
        '',
        'TypeArgs'
    ],

    'TypeParameters?':
    [
        '',
        'TypeParameters'
    ],

    # Regras especiais
    'ConstSpecSp1?':
    [
        '',
        f'Type? {op("=")} ExpressionList'
    ],

    'KeyedElementSp1?':
    [
        f'Key {op(":")}'
    ],

    'LiteralValueSp1?':
    [
        '',
        f'ElementList {op(",")}?'
    ],

    'ParametersSp1?':
    [
        '',
        f'ParameterList {op(",")}?'
    ],

    'VarSpecSp1?':
    [
        '',
        f'{op("=")} ExpressionList'
    ]
}

# Todas as regras do caso '{ regra }' caem aqui.
condicional_n = \
{
    # Regras para tokens léxicos (terminais)

    # Regras para não-terminais

    # Regras especiais
    'ConstDeclSp1*':
    [
        '',
        f'ConstSpec {op(";")}? ConstDeclSp1*'
    ],

    'ElementListSp1*':
    [
        '',
        f'{op(",")} KeyedElement ElementListSp1*'
    ],

    'ExpressionListSp1*':
    [
        '',
        f'{op(",")} Expression ExpressionListSp1*'
    ],

    'IdentifierListSp1*':
    [
        '',
        f'{op(",")} {tk("identifier")} IdentifierListSp1*'
    ],

    'InterfaceTypeSp1*':
    [
        '',
        f'InterfaceElem {op(";")}? InterfaceTypeSp1*' # ; OPCIONAL
    ],

    'ParameterListSp1*':
    [
      '',
      f'{op(",")} ParameterDecl ParameterListSp1*'
    ],
    
    'StatementListSp1*':
    [
        '',
        f'Statement {op(";")}?' # ; OPCIONAL
    ],

    'StructTypeSp1*':
    [
        '',
        f'FieldDecl {op(";")}? StructTypeSp1*' # ; OPCIONAL
    ],

    'TypeDeclSp1*':
    [
        '',
        f'TypeSpec {op(";")}? TypeDeclSp1*' # ; OPCIONAL
    ],

    'TypeElemSp1*':
    [
        '',
        f'{op("|")} TypeTerm TypeElemSp1*'
    ],

    'TypeListSp1*':
    [
        '',
        f'{op(",")} Type TypeListSp1*'
    ],

    'TypeParamListSp1*':
    [
        '',
        f'{op(",")} TypeParamDecl TypeParamListSp1*'
    ],

    'VarDeclSp1*':
    [
        '',
        f'VarSpec {op(";")} VarDeclSp1*' # ; OPCIONAL
    ]
}

tipos = \
{
    'Type':
    [
        'TypeName TypeArgs?',
        'TypeLit',
        f'{op("(")} Type {op(")")}'
    ],

    'TypeName':
    [
        f'{tk("identifier")}',
        'QualifiedIdent'
    ],

    'TypeArgs':
    [
        f'{op("[")} TypeList {op(",")}? {op("]")}',
    ],

    'TypeList':
    [
        'Type TypeListSp1*'
    ],

    'TypeLit':
    [
        'ArrayType',
        'StructType',
        'PointerType',
        'FunctionType',
        'InterfaceType',
        'SliceType',
        'MapType',
        'ChannelType'
    ]
}

tipos_array = \
{
    'ArrayType':
    [
        f'{op("[")} ArrayLength {op("]")} ElementType'
    ],

    'ArrayLength':
    [
        'Expression'
    ],

    'ElementType':
    [
        'Type'
    ]
}

tipos_slice = \
{
    'SliceType':
    [
        f'{op("[")} {op("]")} ElementType'
    ]
}

#???
tipos_struct = \
{
    'StructType':
    [
        f'{tk("struct")} {op("{")} StructTypeSp1* {op("}")}'
    ],

    'FieldDecl':
    [
        'IdentifierList Type Tag?',
        'EmbeddedField Tag?'
    ],

    'EmbeddedField':
    [
        f'{op("*")}? TypeName TypeArgs?'
    ],

    'Tag':
    [
        f'{tk("string_lit")}'
    ]
}

tipos_ponteiro = \
{
    'PointerType':
    [
        f'{op("*")} BaseType'
    ],

    'BaseType':
    [
        'Type'
    ]
}

tipos_funcao = \
{
    'FunctionType':
    [
        f'{tk("func")} Signature'
    ],

    'Signature':
    [
        'Parameters Result?'
    ],

    'Result':
    [
        'Parameters',
        'Type'
    ],

    'Parameters':
    [
        f'{op("(")} ParametersSp1? {op(")")}'
    ],

    'ParameterList':
    [
        'ParameterDecl ParameterListSp1*'
    ],

    'ParameterDecl':
    [
        f'IdentifierList? {op("...")}? Type'
    ]
}

tipos_interface = \
{
    'InterfaceType':
    [
        f'{tk("interface")} {op("{")} InterfaceTypeSp1* {op("}")}'
    ],

    'InterfaceElem':
    [
        'MethodElem',
        'TypeElem'
    ],

    'MethodElem':
    [
        'MethodName Signature'
    ],

    'MethodName':
    [
        f'{tk("identifier")}'
    ],

    'TypeElem':
    [
        f'TypeTerm TypeElemSp1*'
    ],

    'TypeTerm':
    [
        'Type',
        'UnderlyingType'
    ],

    'UnderlyingType':
    [
        f'{op("~")} Type'
    ]
}

tipos_mapa = \
{
    'MapType':
    [
        f'{tk("map")} {op("[")} KeyType {op("]")} ElementType'
    ],

    'KeyType':
    [
        'Type'
    ]
}

tipos_canal = \
{
    'ChannelType':
    [
        f'{tk("chan")} ElementType',
        f'{tk("chan")} {op("<-")} ElementType',
        f'{op("<-")} {tk("chan")} ElementType'
    ]
}

# Blocos explícitos. A especificação ainda trata de blocos implícitos: https://go.dev/ref/spec#Blocks.
blocos = \
{
    'Block':
    [
        f'{op("{")} StatementList {op("}")}'
    ],

    'StatementList':
    [
        'StatementListSp1*'
    ]
}

declaracoes = \
{
    'Declaration':
    [
        'ConstDecl',
        'TypeDecl',
        'VarDecl'
    ],

    'TopLevelDecl':
    [
        'Declaration',
        'FunctionDecl',
        'MethodDecl'
    ]
}

declaracao_constantes = \
{
    'ConstDecl':
    [
        f'{tk("const")} ConstSpec',
        f'{tk("const")} {op("(")} ConstDeclSp1* {op(")")}'
    ],

    'ConstSpec':
    [
        'IdentifierList ConstSpecSp1?'
    ],

    'IdentifierList':
    [
        f'{tk("identifier")} IdentifierListSp1*'
    ],

    'ExpressionList':
    [
        'Expression ExpressionListSp1*'
    ]
}

declaracao_tipos = \
{
    'TypeDecl':
    [
        f'{tk("type")} TypeSpec',
        f'{tk("type")} {op("(")} TypeDeclSp1* {op(")")}',
    ],

    'TypeSpec':
    [
        'AliasDecl',
        'TypeDef'
    ]
}

declaracao_alias = \
{
    'AliasDecl':
    [
        f'{tk("identifier")} {op("=")} Type'
    ]
}

definicao_tipo = \
{
    'TypeDef':
    [
        f'{tk("identifier")} TypeParameters? Type'
    ]
}

declaracao_parametros_tipo = \
{
    'TypeParameters':
    [
        f'{op("[")} TypeParamList {op(",")}? {op("]")}'
    ],

    'TypeParamList':
    [
        'TypeParamDecl TypeParamListSp1*'
    ],

    'TypeParamDecl':
    [
        'IdentifierList TypeConstraint'
    ]
}

restricoes_tipo = \
{
    'TypeConstraint':
    [
        'TypeElem'
    ]
}

declaracao_variaveis = \
{
    'VarDecl':
    [
        f'{tk("var")} VarSpec',
        f'{tk("var")} {op("(")} VarDeclSp1* {op(")")}'
    ],

    'VarSpec':
    [
        'IdentifierList Type VarSpecSp1?',
        f'IdentifierList {op("=")} ExpressionList'
    ]
}

declaracao_curta_variaveis = \
{
    'ShortVarDecl':
    [
        f'IdentifierList {op(":=")} ExpressionList'
    ]
}

declaracao_funcoes = \
{
    'FunctionDecl':
    [
        f'{tk("func")} FunctionName TypeParameters? Signature FunctionBody?'
    ],

    'FunctionName':
    [
        f'{tk("identifier")}'
    ],

    'FunctionBody':
    [
        'Block'
    ]
}

declaracao_metodos = \
{
    'MethodDecl':
    [
        f'{tk("func")} Receiver MethodName Signature FunctionBody?'
    ],

    'Receiver':
    [
        'Parameters'
    ]
}

operandos = \
{
    'Operand':
    [
        'Literal',
        'OperandName TypeArgs?',
        f'{op("(")} Expression {op(")")}'
    ],

    'Literal':
    [
        'BasicLit',
        'CompositeLit',
        'FunctionLit'
    ],

    'BasicLit':
    [
        f'{tk("int_lit")}',
        f'{tk("float_lit")}',
        f'{tk("imaginary_lit")}',
        f'{tk("rune_lit")}',
        f'{tk("string_lit")}'
    ],

    'OperandName':
    [
        f'{tk("identifier")}',
        'QualifiedIdent'
    ]
}

identificadores_qualificados = \
{
    'QualifiedIdent':
    [
        f'PackageName {op(".")} {tk("identifier")}'
    ]
}

literais_compostos = \
{
    'CompositeLit':
    [
        'LiteralType LiteralValue'
    ],

    'LiteralType':
    [
        'StructType',
        'ArrayType',
        f'{op("[")} {op("...")} {op("]")} ElementType'
        'SliceType',
        'MapType',
        'TypeName TypeArgs?'
    ],

    'LiteralValue':
    [
        f'{op("{")} LiteralValueSp1? {op("}")}'
    ],

    'ElementList':
    [
        'KeyedElement ElementListSp1*'
    ],

    'KeyedElement':
    [
        'KeyedElementSp1? Element'
    ],

    'Key':
    [
        'FieldName',
        'Expression',
        'LiteralValue'
    ],

    'FieldName':
    [
        f'{tk("identifier")}'
    ],

    'Element':
    [
        'Expression',
        'LiteralValue'
    ]
}

funcao_literal = \
{
    'FunctionLit':
    [
        f'{tk("func")} Signature FunctionBody'
    ]
}

expressoes_primarias = \
{
    'PrimaryExpr':
    [
        'Operand',
        'Conversion',
        'MethodExpr',
        'PrimaryExpr Selector',
        'PrimaryExpr Index',
        'PrimaryExpr Slice',
        'PrimaryExpr TypeAssertion',
        'PrimaryExpr Arguments'
    ],

    'Selector':
    [
        f'{op(".")} {tk("identifier")}'
    ],

    'Index':
    [
        f'{op("[")} Expression {op(",")}? {op("]")}'
    ],

    'Slice':
    [
        f'{op("[")} Expression? {op(":")} Expression? {op("]")}',
        f'{op("[")} Expression? {op(":")} Expression {op(":")} Expression {op("]")}'
    ],

    'TypeAssertion':
    [
        f'{op(".")} {op("(")} Type {op(")")}'
    ],

    'Arguments':
    [
        f'{op("(")} ArgumentsSp1? {op(")")}'
    ]
}

expressoes_metodos = \
{
    'MethodExpr':
    [
        f'ReceiverType {op(".")} MethodName'
    ],

    'ReceiverType':
    [
        'Type'
    ]
}

listas = \
{
    'Condicional 1': condicional_1,
    'Condicional n': condicional_n,

    'Tipos': tipos,
    'Tipos de Array': tipos_array,
    'Tipos de Slice': tipos_slice,
    'Tipos de Struct': tipos_struct,
    'Tipos de Ponteiro': tipos_ponteiro,
    'Tipos de Função': tipos_funcao,
    'Tipos de Interface': tipos_interface,
    'Tipos de Mapa': tipos_mapa,
    'Tipos de Canal': tipos_canal,

    'Blocos': blocos,

    'Declarações': declaracoes,

    'Declaração de Constantes': declaracao_constantes,
    'Declaração de Alias': declaracao_alias,
    'Definição de Tipo': definicao_tipo,
    'Declaração de Parâmetros de Tipo': declaracao_parametros_tipo,
    'Restrições de Tipo': restricoes_tipo,
    'Declaração de Variáveis': declaracao_variaveis,
    'Declaração Curta de Variáveis': declaracao_curta_variaveis,
    'Declaração de Funções': declaracao_funcoes,
    'Declaração de Métodos': declaracao_metodos,

    # Expressões
    'Operandos': operandos,
    'Identificadores Qualificados': identificadores_qualificados,
    'Literais Compostos': literais_compostos,
    'Função Literal': funcao_literal,
    'Expressões Primárias': expressoes_primarias,
    'Expressões de Métodos': expressoes_metodos,

}

for nome_lista, lista in listas.items():
    for nome_regra, valores_regra in lista.items():
        for valor in valores_regra:
            print(nome_regra, '->', valor)
        print()
#    print()
