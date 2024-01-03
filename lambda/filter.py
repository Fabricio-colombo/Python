def numeros(x):
    return x % 2 == 0

numeros_1 = [1,2,3,4,5,6,7,8,9,10,11,12]

num_par = list(filter(numeros, numeros_1))

print(num_par)


number1 = [1,2,3,4,5,6,7,8,9,10,11,12]

x = lambda x: x % 2 != 0
x1 = list(filter(x, number1))
print(x1)



lista_1 = [33,35,37,39,45,46,48,53,56,59,63,65,67,69,72,74,73,79]

num_par = list(filter(lambda x: x % 2 == 0, lista_1))
print(num_par)

num_impar = list(filter(lambda x: x % 2 != 0, lista_1))
print(num_impar)

