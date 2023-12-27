# 1. Tupla de Números
# tuple
tupla_numeros = (1, 2, 3, 4, 5)

# 2. Tupla de Texto (Strings)
# tuple
tupla_frutas = ("maçã", "banana", "laranja")

# 3. Tupla de Mistura de Tipos
# tuple
tupla_mista = (1, "dois", 3.0, True)

# 4. Tupla de Um Elemento
# tuple
tupla_um_elemento = (42,)

# 5. Acesso a Elementos da Tupla
primeiro_elemento = tupla_numeros[0]
ultimo_elemento = tupla_frutas[-1]

# 6. Desempacotamento de Tupla
a, b, c = tupla_numeros

# 7. Comprimento da Tupla
tamanho_tupla_frutas = len(tupla_frutas)

# 8. Iteração sobre uma Tupla
for fruta in tupla_frutas:
    print(fruta)
