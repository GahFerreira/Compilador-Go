# Programa para gerar código em JavaCC de reconhecimento léxico da linguagem Go.

nome_da_classe = "Compilador"

# Tokens especiais: seus nomes e valores são distintos.
operadores = \
[
  {
    "nome": "DIFFERENT",
    "valor": "!="
  },
  {
    "nome": "LESS_EQUAL",
    "valor": "<="
  },
  {
    "nome": "GREATER_EQUAL",
    "valor": ">="
  },
  {
    "nome": "SHORT_DECLARATION",
    "valor": ":="
  },
  {
    "nome": "ELLIPSIS",
    "valor": "..."
  },
  {
    "nome": "OPEN_PARENTHESIS",
    "valor": "("
  },
  {
    "nome": "CLOSE_PARENTHESIS",
    "valor": ")"
  },
  {
    "nome": "OPEN_BRACKET",
    "valor": "["
  },
  {
    "nome": "CLOSE_BRACKET",
    "valor": "]"
  },
  {
    "nome": "OPEN_CURLY_BRACKET",
    "valor": "{"
  },
  {
    "nome": "CLOSE_CURLY_BRACKET",
    "valor": "}"
  },
  {
    "nome": "COMMA",
    "valor": ","
  },
  {
    "nome": "SEMICOLON",
    "valor": ";"
  },
  {
    "nome": "DOT",
    "valor": "."
  },
  {
    "nome": "COLON",
    "valor": ":"
  },
  {
    "nome": "AND",
    "valor": "&&"
  },
  {
    "nome": "OR",
    "valor": "||"
  },
  {
    "nome": "CHANNEL_DIRECTION",
    "valor": "<-"
  },
  {
    "nome": "PLUS_PLUS",
    "valor": "++"
  },
  {
    "nome": "MINUS_MINUS",
    "valor": "--"
  },
  {
    "nome": "BIT_AND_NOT_ASSIGN",
    "valor": "&^="
  },
  {
    "nome": "BIT_AND_ASSIGN",
    "valor": "&="
  },
  {
    "nome": "BIT_OR_ASSIGN",
    "valor": "|="
  },
  {
    "nome": "BIT_XOR_ASSIGN",
    "valor": "^="
  },
  {
    "nome": "LEFT_SHIFT_ASSIGN",
    "valor": "<<="
  },
  {
    "nome": "RIGHT_SHIFT_ASSIGN",
    "valor": ">>="
  },
  {
    "nome": "PLUS_ASSIGN",
    "valor": "+="
  },
  {
    "nome": "MINUS_ASSIGN",
    "valor": "-="
  },
  {
    "nome": "MULTIPLY_ASSIGN",
    "valor": "*="
  },
  {
    "nome": "DIVIDE_ASSIGN",
    "valor": "/="
  },
  {
    "nome": "REMAINDER_ASSIGN",
    "valor": "%="
  },
  {
    "nome": "BIT_AND_NOT",
    "valor": "&^"
  },
  {
    "nome": "BIT_AND",
    "valor": "&"
  },
  {
    "nome": "BIT_OR",
    "valor": "|"
  },
  {
    "nome": "BIT_XOR",
    "valor": "^"
  },
  {
    "nome": "LEFT_SHIFT",
    "valor": "<<"
  },
  {
    "nome": "RIGHT_SHIFT",
    "valor": ">>"
  },
  {
    "nome": "PLUS",
    "valor": "+"
  },
  {
    "nome": "MINUS",
    "valor": "-"
  },
  {
    "nome": "MULTIPLY",
    "valor": "*"
  },
  {
    "nome": "DIVIDE",
    "valor": "/"
  },
  {
    "nome": "REMAINDER",
    "valor": "%"
  },
  {
    "nome": "EQUAL",
    "valor": "=="
  },
  {
    "nome": "LESS",
    "valor": "<"
  },
  {
    "nome": "GREATER",
    "valor": ">"
  },
  {
    "nome": "ASSIGN",
    "valor": "="
  },
  {
    "nome": "NOT",
    "valor": "!"
  },
  {
    "nome": "TILDE",
    "valor": "~"
  }
]

# Tokens normais: seus nomes e valores são iguais.
tipos = [ "ANY", "BOOL", "BYTE", "COMPARABLE", "COMPLEX64", "COMPLEX128", "ERROR",
          "FLOAT32", "FLOAT64", "INT", "INT8", "INT16", "INT32", "INT64", "RUNE",
          "STRING", "UINT", "UINT8", "UINT16", "UINT32", "UINT64", "UINTPTR" ]

constantes = [ "TRUE", "FALSE", "IOTA" ]

funcoes = [ "APPEND", "CAP", "CLOSE", "COMPLEX", "COPY", "DELETE", "IMAG", "LEN",
            "MAKE", "NEW", "PANIC", "PRINTLN", "PRINT", "REAL", "RECOVER" ]

palavras_chave = [ "BREAK", "DEFAULT", "FUNC", "INTERFACE", "SELECT", "CASE",
                   "DEFER", "GO", "MAP", "STRUCT", "CHAN", "ELSE", "GOTO",
                   "PACKAGE", "SWITCH", "CONST", "FALLTHROUGH", "IF", "RANGE",
                   "TYPE", "CONTINUE", "FOR", "IMPORT", "RETURN", "VAR" ]

valor_zero = [ "NIL" ]

'''# Listando todas as listas de tokens
listas_de_tokens = \
[
  {
    "nome_lista": "Operadores",
    "referência": operadores
  },
  { "nome_lista": "Tipos",
    "referência": tipos
  },
  {
    "nome_lista": "Constantes",
    "referência": constantes
  },
  {
    "nome_lista": "Funções",
    "referência": funcoes
  },
  {
    "nome_lista": "Palavras-Chave",
    "referência": palavras_chave
  },
  {
    "nome_lista": "Valor Zero",
    "referência": valor_zero
  }
]'''

# Implementa a classe base.
print("PARSER_BEGIN(" + nome_da_classe + ")",
      "",
      "public class " + nome_da_classe,
      "{",
      "  public static void main(String args[]) throws ParseException, TokenMgrError",
      "  {",
      "    " + nome_da_classe + " parser = new " + nome_da_classe + "(System.in);",
      "",
      "    parser.Inicio();",
      "  }",
      "}",
      "",
      "PARSER_END(" + nome_da_classe + ")",
      "",
      "",
      sep = "\n")


# SKIP
print("SKIP:",
      "{",
      "  /** Espaços em Branco */",
      '  " "',
      '| "\\t"',
      '| "\\n"',
      '| "\\r"',
      "}",
      "",
      sep = "\n")

# TOKEN
print("TOKEN:",
      "{",
      sep = "\n")

## OPERADORES
print("  /** Operadores */")

_ = [print("  < " + operador["nome"] + ': "' + operador["valor"] + '" >',
           "|",
           sep = "\n")
     for operador in operadores]

## TIPOS
print("  /** Tipos */")

_ = [print("  < " + tipo + ': "' + tipo.lower() + '" >',
           "|",
           sep = "\n")
     for tipo in tipos]

## CONSTANTES
print("  /** Constantes */")

_ = [print("  < " + constante + ': "' + constante.lower() + '" >',
           "|",
           sep = "\n")
     for constante in constantes]

## FUNÇÕES
print("  /** Funções */")

_ = [print("  < " + funcao + ': "' + funcao.lower() + '" >',
           "|",
           sep = "\n")
     for funcao in funcoes]

## PALAVRAS-CHAVE
print("  /** Palavras-Chave */")

_ = [print("  < " + palavra_chave + ': "' + palavra_chave.lower() + '" >',
           "|",
           sep = "\n")
     for palavra_chave in palavras_chave]

## VALOR ZERO
print("  /** Valor Zero */")

print("  < " + valor_zero[0] + ': "' + valor_zero[0] + '" >', sep = "\n")

print("}\n\n")

# Implementação da função de início.
print("void Inicio():",
      "{",
      "  Token t;",
      "}",
      "{",
      "  (",
      sep = "\n")
