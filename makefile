# Parte léxica
NOME_CLASSE = Compilador
ARQUIVO_JJ = $(NOME_CLASSE).jj
GERADOR_LEXICO = gerador_lexico.py

# Parte sintática
NOME_GRAMATICA = gramatica
EXTENSAO_GRAMATICA = gramatica
GERAR_GRAMATICA = gerar_gramatica.py

all: lexico sintatico

# Agrupadores
lexico: gerador_lexico javacc javac

sintatico: gerar_gramatica

# Comandos
java:
	java $(NOME_CLASSE)

javac: 
	javac *.java

javacc: $(GERADOR_LEXICO) $(ARQUIVO_JJ)
	javacc $(ARQUIVO_JJ)

gerador_lexico: $(GERADOR_LEXICO)
	py $(GERADOR_LEXICO) > $(ARQUIVO_JJ)

gerar_gramatica: $(GERAR_GRAMATICA)
	py $(GERAR_GRAMATICA) > $(NOME_GRAMATICA).$(EXTENSAO_GRAMATICA)

clean:
	rm *.class *.java