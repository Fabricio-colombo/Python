numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print("Lista original:", numeros)
print("Números pares:", numeros_pares)


par = lambda x: x % 2 == 0
print(par(9))


num1 = lambda y: y % 2 == 0
print(num1(10))


f_c = lambda f: (f - 32)* 5/9
print(f_c(212))

number = lambda x: x + 5
print(number(5))

n = lambda i: i - 2
print(n(10))

nuuum = lambda i: i / 10
print(nuuum(100))