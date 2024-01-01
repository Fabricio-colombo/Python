# Dólar: R$ 4,8611
# Euro: R$ 5,3541
# Libra: R$ 6,2341

def dolar():
    dolar = 4.86
    real = float(input('Digite a quantidade de reais para converter em dolar: '))
    converter = real * dolar
    print(f"PARABÉNS!! Acabou de converter {real} BRL em", round(converter, 2), 'USD')
    
def euro():
    euro = 5.35
    real = float(input('Digite a quantidade de reais para converter em euro: '))
    converter = real * euro
    print(f"PARABÉNS!! Acabou de converter {real} BRL em", round(converter, 2), 'EUR')

def libra():
    libra = 6.23
    real = float(input('Digite a quantidade de reais para converter em libra: '))
    converter = real * libra
    print(f"PARABÉNS!! Acabou de converter {real} BRL em ", round(converter, 2), 'LIB')

if __name__ == "__main__":
    print('-----Conversor de Moedas-----')
msg_inicial = input('Deseja converter de real para dolar, euro ou libra? ')
msg_minuscula = msg_inicial.lower()

if msg_minuscula == 'dolar':
    dolar()
elif msg_minuscula == 'euro':
    euro()
elif msg_minuscula == 'libra':
    libra()
else:
    print('Digite CORRETAMENTE!')