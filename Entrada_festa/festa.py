'''
Está rolando um evento, onde tem 3 pista de dança, uma pra criança de 0 a 13 anos, outra para adolescente de 14 a 18 e pra adulto de 18+.
crie um programa que gerencie a entrada das pistas de dança, e com base na idade, vai indicar para qual pista de dança a pessoa deve ir. 
Chegando na pista de dança tem outra entrada onde se compra o ingresso na hora, e os valores são 10 reais para criança, 20 para 
adolescente e 30 para adultos. se a pessoa comprar o ingresso ela pode entrar no evento.
'''
nome = input('Me diga seu nome: ')
idade = int(input('Me diga a sua idade agora: '))

if idade <=13:
    print(f"{nome}, pela sua idade, você vai ir para a pista de dança 1 de criança!")
elif idade >=14 and idade <18:
    print(f"{nome}, pela sua idade, você vai para a pista de dança 2 de adolescente!")
else:
    print(f"{nome}, você é maior de 18, vai para a pista 3 de adultos!")
    
pista1 = 10
pista2 = 20
pista3 = 30

print('INDO PARA A PISTA INDICADA')

#CHEGANDO NA PISTA INDICADA

print(f"Olá {nome}, agora você precisa comprar o ingresso da sua pista para entrar no evento indicado.")

ingresso = input('me diga agora, se você quer comprar o ingresso da pista1, pista2 ou pista3: ')

if ingresso == pista1:
    print(f"{nome}, o valor do seu ingresso é de ", pista1)
elif ingresso == pista2:
    print(f"{nome}, o valor do seu ingresso é ", pista2)
elif ingresso == pista3:
    print(f"{nome}, o valor do seu ingresso é ", pista3)