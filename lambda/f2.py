numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

par = lambda x: x % 2 == 0

impar = lambda y: y % 2 != 0

res_par = filter(par, numeros)
res_par2 = list(res_par)        #criei outra variavel para receber a list
print(res_par2)

res_impar = filter(impar, numeros)
print(list(res_impar))        #fiz a list direto no print