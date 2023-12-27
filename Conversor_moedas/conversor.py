import requests

def obter_taxas():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/exchange_rates")
        data = response.json()
        rates = data['rates']
        return rates
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter as taxas: {e}")
        return None

def converter_moeda(valor, moeda_origem, moeda_destino, taxas):
    if not taxas:
        return None

    taxa_origem = taxas.get(moeda_origem.lower())
    taxa_destino = taxas.get(moeda_destino.lower())

    if taxa_origem is None or taxa_destino is None:
        return None

    valor_convertido = valor * (1 / taxa_origem) * taxa_destino
    return valor_convertido

def main():
    taxas = obter_taxas()

    if taxas is not None:
        print("Taxas de câmbio disponíveis:")
        for moeda, taxa in taxas.items():
            print(f"{moeda}: {taxa}")

        valor = float(input("Digite o valor a ser convertido: "))
        moeda_origem = input("Digite a moeda de origem (por exemplo, USD): ").upper()
        moeda_destino = input("Digite a moeda de destino (por exemplo, EUR): ").upper()

        resultado = converter_moeda(valor, moeda_origem, moeda_destino, taxas)

        if resultado is not None:
            print(f"{valor} {moeda_origem} é equivalente a {resultado:.2f} {moeda_destino}")
        else:
            print("Não foi possível realizar a conversão.")

if __name__ == "__main__":
    main()
