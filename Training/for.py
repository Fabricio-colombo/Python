'''
lista = [1, 3, 5, 7, 77, 43, 53, 60]

for item in lista:
    print(lista)
'''

for i in range(1, 11):
   print(i)

def tabuada(numero):
    print(f"Tabuada do {numero}:")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

if __name__ == "__main__":
    try:
        numero_informado = int(input("Digite um número para a tabuada: "))
        tabuada(numero_informado)
    except ValueError:
        print("Por favor, digite um número válido.")




'''
tupla = ('Maça', 'Goiaba', 'Macarrão', 'Arroz', 'Feijão', 'Ervilha')

for comida in tupla:
    if comida == 'Arroz':
        continue
    print(comida)
'''