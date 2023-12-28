#crie um programa que o usuario tem que adivinhar o numero correto de 0 a 20 e se acertar encerra com parabéns.

nome = str(input('Qual é seu nome participante? '))

print(f"Seja bem-vindo(a) {nome}, agora você tem que adivinhar o numero correto de 0 a 20 para ganhar seu Parabéns")

tentativa = int(input('de 0 a 20 qual numero você escolhe? '))

while tentativa != 16:
    print('ERROUUUUUUU!!!')
    tentativa = int(input('de 0 a 20 qual numero você escolhe? '))
    if tentativa == 16:
        print('ACERTOUUUUUUUUU!!!!!')
        break
    
    
    
