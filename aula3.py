"""
Python = Linguagem de Programação
Tipo de Tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que são inseridos dentro de aspas
"""
print(1234)

# Aspas Simples
print('Green')

# Aspas Duplas
print("Blue")

# Escape - Utilizado para poder inserir certos caracteres dentro da string que seriam interpretados de outra forma (como as aspas duplas no exemplo abaixo)
print("Green \" Blue\"")

# r - Insere na string todos os caracteres passados dentro do parâmetro
print(r"Green \"Blue\"")

# Apesar dos métodos acimas (escape e r) serem úteis, complicam de forma desnecessária o código, podendo ser simplificado de forma abaixo
print('Green "Blue"')

# Também é possível utilizar de forma inversa, como abaixo
print("Green 'Blue'")