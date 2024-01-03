#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

#Preço Total=(Quantidade de Dias×60)+(Quantidade de Km×0.15)

def aluguel():
    quantidade_dias = int(input('Quantos dias usou o carro? '))
    quantidade_km = float(input('Quantos km foi rodado? '))
    preco_final = (quantidade_dias * 60) + (quantidade_km * 0.15)
    print(f"O preço total a pagar é de R${preco_final} reais")
    
while True:
    try:
        aluguel()
        break
    except:
        print('Digite corretamente')
    finally:
        print('FIM')