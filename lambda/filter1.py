numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def eh_par(numero):
    return numero % 2 == 0

pares = filter(eh_par, numeros)

print(list(pares))
