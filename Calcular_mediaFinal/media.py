#faça um programa que calcule a media final do aluno.

nome = input('Digite seu nome, aluno: ')

n1 = float(input('Digite a nota da sua primeira prova: '))
n2 = float(input('Digite a nota da segunda prova: '))

media = (n1 + n2) / 2

if media >= 7:
    print(f"Parabéns {nome}, sua nota final é {media} e por isto você passou de ano!")
elif media < 7 and media > 5:
    print(f"{nome}, sua media final é {media} e por isto você está de recuperação!")
else:
    print(f"{nome}, sua média final é insuficiente, você tirou {media} e por isso reprovou de ano!")