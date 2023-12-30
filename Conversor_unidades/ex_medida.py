#escreva um programa que leia  um valor em metros e o exiba convertido em centimetros e milimetros

# 1 metro == 100 centimetros
# 1 metro == 1000 milimetros

print('CONVERSOR DE METROS')
metros = float(input('Digite quantos metros você quer converter: '))

cent = metros * 100
mili = metros * 1000

print(f"{metros} M é igual a {cent} CM e também é igual a {mili} MM")