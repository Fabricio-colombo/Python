def converter_tempo(valor, unidade_entrada, unidade_saida):
    fatores = {
        'segundo': 1,
        'minuto': 60,
        'hora': 3600,
        'dia': 86400,
        'semana': 604800,
        'ano': 31536000
    }

    try:
        resultado = valor * fatores[unidade_entrada] / fatores[unidade_saida]
        return resultado
    except KeyError:
        return "Unidades de entrada ou saída não suportadas."

def main():
    print("Bem-vindo ao Conversor de Tempo!")
    
    valor = float(input("Digite o valor a ser convertido: "))
    unidade_entrada = input("Digite a unidade de entrada (segundo/minuto/hora/dia/semana/ano): ").lower()
    unidade_saida = input("Digite a unidade de saída (segundo/minuto/hora/dia/semana/ano): ").lower()

    resultado = converter_tempo(valor, unidade_entrada, unidade_saida)

    if isinstance(resultado, float):
        print(f"{valor} {unidade_entrada} é igual a {resultado} {unidade_saida}.")
    else:
        print(resultado)

if __name__ == "__main__":
    main()
