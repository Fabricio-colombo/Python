#digite um numero para ver a sua tabuada

# Solicita que o usuário digite um número
numero = int(input("Digite um número para a tabuada: "))

# Utiliza o laço de repetição for para calcular e exibir a tabuada
print(f"Tabuada do {numero}:")
for i in range(11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
