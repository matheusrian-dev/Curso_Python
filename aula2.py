print(12, 34, end='\r\n') # utilizada para exibir informações na tela utilizando argumentos (arg)
print(56, 78, sep="--", end='\r\n') 
print(56, 78, sep="__", end='\n') 
# há alguns caracteres escondidos que não são exibidos mas tem alguma função como a quebra de linha que é representada pelos caracteres abaixo:
# \r\n -> CRLF
# \n -> LF
# é possível utilizar o sep para alterar o separador de argumentos como no exemplo ao lado
# o sep reconhece tanto as aspas simples quanto as aspas duplas
# o end é utilizado para incluir um argumento no final de linha, como mostrado acima onde foi inserido uma quebra de linha