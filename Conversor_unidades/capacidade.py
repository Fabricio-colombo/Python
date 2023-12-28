def converter_capacidade(valor, unidade_entrada, unidade_saida):
    fatores = {
        'litro': 1,
        'mililitro': 0.001,
        'galao_americano': 3.78541,
        'galao_britanico': 4.54609,
        'copo_americano': 0.24,
        'xicara': 0.24
    }

    try:
        resultado = valor * fatores[unidade_entrada] / fatores[unidade_saida]
        return resultado
    except KeyError:
        return "Unidades de entrada ou saída não suportadas."

def main():
    print("Bem-vindo ao Conversor de Capacidade!")
    
    valor = float(input("Digite o valor a ser convertido: "))
    unidade_entrada = input("Digite a unidade de entrada (litro/mililitro/galao_americano/galao_britanico/copo_americano/xicara): ").lower()
    unidade_saida = input("Digite a unidade de saída (litro/mililitro/galao_americano/galao_britanico/copo_americano/xicara): ").lower()

    resultado = converter_capacidade(valor, unidade_entrada, unidade_saida)

    if isinstance(resultado, float):
        print(f"{valor} {unidade_entrada} é igual a {resultado} {unidade_saida}.")
    else:
        print(resultado)

if __name__ == "__main__":
    main()
