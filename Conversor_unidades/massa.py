def converter_massa(valor, unidade_entrada, unidade_saida):
    fatores = {
        'quilograma': 1,
        'grama': 0.001,
        'miligrama': 0.000001,
        'tonelada': 1000,
        'libra': 0.453592,
        'onca': 0.0283495
    }

    try:
        resultado = valor * fatores[unidade_entrada] / fatores[unidade_saida]
        return resultado
    except KeyError:
        return "Unidades de entrada ou saída não suportadas."

def main():
    print("Bem-vindo ao Conversor de Massa!")
    
    valor = float(input("Digite o valor a ser convertido: "))
    unidade_entrada = input("Digite a unidade de entrada (quilograma/grama/miligrama/tonelada/libra/onca): ").lower()
    unidade_saida = input("Digite a unidade de saída (quilograma/grama/miligrama/tonelada/libra/onca): ").lower()

    resultado = converter_massa(valor, unidade_entrada, unidade_saida)

    if isinstance(resultado, float):
        print(f"{valor} {unidade_entrada} é igual a {resultado} {unidade_saida}.")
    else:
        print(resultado)

if __name__ == "__main__":
    main()
