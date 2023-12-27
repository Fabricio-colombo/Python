# 1. For Loop com Lista
# for
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

# 2. While Loop
# while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# 3. For Loop com Range
# for, range
for i in range(5):
    print(i)

# 4. Break e Continue no For Loop
# for, break, continue
for i in range(10):
    if i == 3:
        break  # Sai do loop quando i é igual a 3
    if i % 2 == 0:
        continue  # Pula para a próxima iteração se i é par
    print(i)

# 5. Enumerate no For Loop
# for, enumerate
frutas = ["maçã", "banana", "laranja"]
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")
