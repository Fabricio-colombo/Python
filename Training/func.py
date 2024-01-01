#funções / input >> fun >> output

#função sem arg

def rx():
    print('Welcome-dog-crazy')
    for i in range(5):
        print(i)
        i+= 1
        
rx()

#função com arg

x = 10
y = 5
def soma(x, y):
    print(x + y)
    
soma(x, y)

#função com return
a = 5
b = 4

def mult(a, b):
    return a * b


c = mult(a, b)
print(c)