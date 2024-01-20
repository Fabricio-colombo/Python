# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar números pares da lista
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Lista original:", numeros)
print("Números pares:", numeros_pares)

# Verificar se um número é par
par = lambda x: x % 2 == 0
print(par(9))  # Saída: False

# Verificar se um número é par
num1 = lambda y: y % 2 == 0
print(num1(10))  # Saída: True

# Converter temperatura de Fahrenheit para Celsius
f_c = lambda f: (f - 32)* 5/9
print(f_c(212))  # Saída: 100.0

# Adicionar 5 a um número
number = lambda x: x + 5
print(number(5))  # Saída: 10

# Subtrair 2 de um número
n = lambda i: i - 2
print(n(10))  # Saída: 8

# Dividir um número por 10
nuuum = lambda i: i / 10
print(nuuum(100))  # Saída: 10.0