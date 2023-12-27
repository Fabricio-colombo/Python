# 1. Lista de Números
# list
lista_numeros = [1, 2, 3, 4, 5]

# 2. Lista de Texto (Strings)
# list
lista_frutas = ["maçã", "banana", "laranja"]

# 3. Lista de Mistura de Tipos
# list
lista_mista = [1, "dois", 3.0, True]

# 4. Lista Vazia
# list
lista_vazia = []

# 5. Acesso a Elementos da Lista
primeiro_elemento = lista_numeros[0]
ultimo_elemento = lista_frutas[-1]

# 6. Adição de Elementos à Lista
lista_frutas.append("morango")

# 7. Remoção de Elementos da Lista
lista_numeros.remove(3)

# 8. Comprimento da Lista
tamanho_lista_frutas = len(lista_frutas)

# 9. Iteração sobre uma Lista
for fruta in lista_frutas:
    print(fruta)
