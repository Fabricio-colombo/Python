def converter_comprimento(valor, unidade_entrada, unidade_saida):
    fatores = {
        'metro': 1,
        'quilometro': 1000,
        'centimetro': 0.01,
        'milimetro': 0.001,
        'polegada': 0.0254,
        'pe': 0.3048
    }

    try:
        resultado = valor * fatores[unidade_entrada] / fatores[unidade_saida]
        return resultado
    except KeyError:
        return "Unidades de entrada ou saída não suportadas."

def main():
    print("Bem-vindo ao Conversor de Comprimento!")
    
    valor = float(input("Digite o valor a ser convertido: "))
    unidade_entrada = input("Digite a unidade de entrada (metro/quilometro/centimetro/milimetro/polegada/pe): ").lower()
    unidade_saida = input("Digite a unidade de saída (metro/quilometro/centimetro/milimetro/polegada/pe): ").lower()

    resultado = converter_comprimento(valor, unidade_entrada, unidade_saida)

    if isinstance(resultado, float):
        print(f"{valor} {unidade_entrada} é igual a {resultado} {unidade_saida}.")
    else:
        print(resultado)

if __name__ == "__main__":
    main()
