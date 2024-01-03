#função map()

num = [1,2,3,4,5,6,7,8,9]
dobro = list(map(lambda x: x*2, num))
print(dobro)


palavras = ['python', 'é uma', 'linguagem', 'top das', 'galaxias']
maiuscula = list(map(str.upper, palavras))
print(maiuscula)


def numeros(x):
    return x % 2 == 0

numeros_1 = [1,2,3,4,5,6,7,8,9,10,11,12]

num_par = list(map(numeros, numeros_1))

print(num_par)