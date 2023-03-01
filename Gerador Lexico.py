# Programa para gerar código em JavaCC de reconhecimento léxico da linguagem Go.

nome_da_classe = "Compilador"
prefixo_token = "TOKEN_"

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

# Em Go, apesar de '_42' ser um identificador, '0x_42' é válido.
numeros = \
[
  {
    "nome": "DECIMAL_NUMBER",
    "expressão regular": '"0" | (["1"-"9"] (("_")? ["0"-"9"])*)'
  },
  {
    "nome": "BINARY_NUMBER",
    "expressão regular": '"0" ("b" | "B") (("_")? ["0"-"1"])+'
  },
  {
    "nome": "OCTAL_NUMBER",
    "expressão regular": '"0" ("o" | "O")? (("_")? ["0"-"7"])+'
  },
  {
    "nome": "HEXADECIMAL_NUMBER",
    "expressão regular": '"0" ("x" | "X") ( ("_")? (["0"-"9"] | ["A"-"F"] | ["a"-"f"]) )+'
  }
]

# Listando todas as listas de tokens
listas_de_tokens_normais = \
[
  {
    "nome": "Tipos",
    "referência": tipos
  },
  {
    "nome": "Constantes",
    "referência": constantes
  },
  {
    "nome": "Funções",
    "referência": funcoes
  },
  {
    "nome": "Palavras-Chave",
    "referência": palavras_chave
  },
  {
    "nome": "Valor Zero",
    "referência": valor_zero
  }
]

listas_de_tokens_especiais = \
[
  {
    "nome": "Operadores",
    "referência": operadores
  },
  {
    "nome": "Números",
    "referência": numeros
  }
]


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

## Tokens Normais
for lista in listas_de_tokens_normais[:-1]:
  print("  /** " + lista["nome"] + " */")

  for token in lista["referência"]:
    print("  < " + prefixo_token + token + ': "' + token.lower() + '" >',
          "|",
          sep = "\n")

## Tokens Especiais
for lista in listas_de_tokens_especiais:
  print("  /** " + lista["nome"] + " */")

  for token in lista["referência"]:
    if "valor" in token:
      print("  < " + prefixo_token + token["nome"] + ': "' + token["valor"] + '" >',
            "|",
            sep = "\n")

    else:
      print("  < " + prefixo_token + token["nome"] + ": " + token["expressão regular"] + " >",
            "|",
            sep = "\n")


## Última Lista
print("  /** Valor Zero */")
print("  < " + prefixo_token + valor_zero[0] + ': "' + valor_zero[0] + '" >', sep = "\n")

print("}\n\n")


# Implementação da função de início.
print("void Inicio():",
      "{",
      "  Token t;",
      "}",
      "{",
      "  (",
      sep = "\n")

for lista in listas_de_tokens_normais[:-1]:
  for token in lista["referência"]:
    print("    t = <" + prefixo_token + token + ">",
          "    {",
          '      System.out.println("' + prefixo_token + token + ' " + t.image);',
          "    }",
          "",
          "    |",
          "",
          sep = "\n")

for lista in listas_de_tokens_especiais:
  for token in lista["referência"]:
    print("    t = <" + prefixo_token + token["nome"] + ">",
          "    {",
          '      System.out.println("' + prefixo_token + token["nome"] + ' " + t.image);',
          "    }",
          "",
          "    |",
          "",
          sep = "\n")

print("    t = <" + prefixo_token + valor_zero[0] + ">",
      "    {",
      '      System.out.println("' + prefixo_token + valor_zero[0] + ' " + t.image);',
      "    }",
      sep = "\n")

print("  )*",
      "",
      "  <EOF>",
      "}",
      sep = "\n")
