# Manipulação de Erros e Exceções

# 1. Tratamento de ZeroDivisionError
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Erro: {e}")

# 2. Tratamento Genérico (Exception)
try:
    numero = int("abc")
except Exception as e:
    print(f"Erro: {e}")

# 3. Tratamento Múltiplo de Exceções
try:
    lista = [1, 2, 3]
    elemento = lista[5]
    resultado = 10 / 0
except IndexError as e:
    print(f"Erro de índice: {e}")
except ZeroDivisionError as e:
    print(f"Erro de divisão por zero: {e}")
except Exception as e:
    print(f"Outro erro: {e}")

# 4. Bloco `finally`
try:
    arquivo = open("arquivo_inexistente.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError as e:
    print(f"Erro: {e}")
finally:
    print("Este bloco sempre será executado, independentemente de exceções.")
    if 'arquivo' in locals():
        arquivo.close()

# 5. Lançamento de Exceção (raise)
def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

try:
    resultado = dividir(10, 0)
except ValueError as e:
    print(f"Erro: {e}")
