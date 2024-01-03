# crie um programa que de desconto para o usuario no total de suas compras
#conta 10 / 100 * valor total

valor_total = float(input('Digite qual foi o valor total dos produtos que você comprou: R$'))
print('BOM, agora vamos aplicar um desconto de 10% para você\n')
desconto = 10
valor_desconto = lambda x, y: (x / 100) * 100
desconto_final = (valor_desconto(desconto, valor_total))
desc_final2 = valor_total / desconto * 9

print(f"PARABÉNS, o valor final de sua compra ficou em R${desc_final2} reais")
