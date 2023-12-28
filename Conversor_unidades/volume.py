def converter_volume(valor, unidade_entrada, unidade_saida):
    fatores = {
        'litro': 1,
        'mililitro': 0.001,
        'metro_cubico': 1000,
        'centimetro_cubico': 0.001,
        'galao_americano': 3.78541,
        'galao_britanico': 4.54609
    }

    try:
        resultado = valor * fatores[unidade_entrada] / fatores[unidade_saida]
        return resultado
    except KeyError:
        return "Unidades de entrada ou saída não suportadas."

def main():
    print("Bem-vindo ao Conversor de Volume!")
    
    valor = float(input("Digite o valor a ser convertido: "))
    unidade_entrada = input("Digite a unidade de entrada (litro/mililitro/metro_cubico/centimetro_cubico/galao_americano/galao_britanico): ").lower()
    unidade_saida = input("Digite a unidade de saída (litro/mililitro/metro_cubico/centimetro_cubico/galao_americano/galao_britanico): ").lower()

    resultado = converter_volume(valor, unidade_entrada, unidade_saida)

    if isinstance(resultado, float):
        print(f"{valor} {unidade_entrada} é igual a {resultado} {unidade_saida}.")
    else:
        print(resultado)

if __name__ == "__main__":
    main()
