#faça um programa simples que imprima quantos litros de tinta o usuario precisaria para pintar a sua parede.
#considerando que a cada 2m² eu precisaria de 1 litro de tinta.
#coletar largura > coletar altura e multiplico para saber o m²
#posteriormente faço a divisão pela tinta.

def tinta():
    largura = float(input('Qual a largura da sua parede: '))
    altura = float(input('Qual a altura da sua parede: '))
    calc = round((largura * altura) / 2, 2)
    print(f"Para {largura} de largura e {altura} de altura, vamos precisar usar {calc} litros de tinta.")

while True:
    try:
        tinta()
        break
    except ValueError:
        print('ERROR - Digite apenas numeros para calcular')
    except:
        print('ERROR - Desconhecido')
    finally:
        print('FIM DO PROGRAMA')