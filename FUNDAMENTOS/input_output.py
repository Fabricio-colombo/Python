# 1. Entrada de Dados (Input)
# input
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

# 2. Conversão de Entrada para Número
# float
altura = float(input("Digite sua altura em metros: "))
print(f"Sua altura é {altura} metros.")

# 3. Saída de Dados (Print)
# print
idade = 25
print("Idade:", idade)

# 4. Formatação de Saída
# f-string
nome = "Alice"
idade = 30
print(f"{nome} tem {idade} anos.")

# 5. Saída com múltiplos valores
# print
fruta1 = "maçã"
fruta2 = "banana"
print("Frutas:", fruta1, fruta2)

# 6. Saída com Separação e Fim Personalizados
# print
print("Olá", "mundo", sep="-", end="!\n")

# 7. Saída Formatada
# print
valor1 = 10
valor2 = 20
print("A soma de {} e {} é {}".format(valor1, valor2, valor1 + valor2))

# 8. Saída com Operador %
# print
percentagem = 75.6
print("O desconto é %.2f%%" % percentagem)
