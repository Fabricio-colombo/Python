# 1. Definição de Função Simples
# def
def saudacao(nome):
    """Função que imprime uma saudação."""
    print(f"Olá, {nome}!")

# 2. Chamada de Função
# chamada de função
saudacao("Alice")

# 3. Função com Parâmetros e Retorno
# def, return
def calcular_media(notas):
    """Função que calcula a média de uma lista de notas."""
    media = sum(notas) / len(notas)
    return media

notas_aluno = [85, 90, 88]
media_aluno = calcular_media(notas_aluno)
print(f"A média do aluno é: {media_aluno}")

# 4. Função com Parâmetros Padrão
# def, parametros padrão
def saudacao_personalizada(nome, saudacao="Olá"):
    """Função que imprime uma saudação personalizada."""
    print(f"{saudacao}, {nome}!")

saudacao_personalizada("Carlos")
saudacao_personalizada("Maria", "Bom dia")

# 5. Função com Número Variável de Argumentos
# def, *args
def soma(*numeros):
    """Função que soma um número variável de argumentos."""
    resultado = sum(numeros)
    return resultado

resultado_soma = soma(1, 2, 3, 4, 5)
print(f"A soma é: {resultado_soma}")

# 6. Função Lambda (Função Anônima)
# lambda
quadrado = lambda x: x**2
print(f"O quadrado de 4 é: {quadrado(4)}")
