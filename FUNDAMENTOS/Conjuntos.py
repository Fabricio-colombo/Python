# 1. Conjunto de Números
# set
conjunto_numeros = {1, 2, 3, 4, 5}

# 2. Conjunto de Texto (Strings)
# set
conjunto_frutas = {"maçã", "banana", "laranja"}

# 3. Conjunto de Mistura de Tipos
# set
conjunto_misto = {1, "dois", 3.0, True}

# 4. Conjunto Vazio
# set
conjunto_vazio = set()

# 5. Adição de Elementos ao Conjunto
conjunto_frutas.add("morango")

# 6. Remoção de Elementos do Conjunto
conjunto_numeros.remove(3)

# 7. Operações de Conjuntos (união, interseção, diferença)
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}
uniao = conjunto_a.union(conjunto_b)
intersecao = conjunto_a.intersection(conjunto_b)
diferenca = conjunto_a.difference(conjunto_b)

# 8. Iteração sobre um Conjunto
for fruta in conjunto_frutas:
    print(fruta)
