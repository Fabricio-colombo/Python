# 1. Condição Simples (If)
# if
idade = 18
if idade >= 18:
    print("Você é maior de idade")

# 2. Condição Composta (If-Else)
# if, else
numero = 10
if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

# 3. Condição Encadeada (If-Elif-Else)
# if, elif, else
nota = 75
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("F")

# 4. Verificação de Existência (In)
# if, in
frutas = ["maçã", "banana", "laranja"]
if "maçã" in frutas:
    print("Maçã está na lista")

# 5. Operador Ternário
# variavel = valor_se_verdadeiro if condicao else valor_se_falso
idade = 20
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)
