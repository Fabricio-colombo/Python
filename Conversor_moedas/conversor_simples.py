# 1 USD == 4.85 BRL

print('Conversor de Moeda\n BRL >> USD')

real = float(input('Quantos reais você quer converter para Dolar: R$'))
dolar = 1
converter = real * 0.21

print(f"{real} BRL foi convertido para" ,round(converter, 2), 'USD')