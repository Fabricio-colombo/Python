from functools import reduce

def mult(x, y):
    return x * y

num = [1,2,3,4,5,6]

re = reduce(mult, num)
print(re)






lista_num1 = [1,2,3,4]

total = reduce(lambda x, y: x**2 + y**2, lista_num1)
print(total)