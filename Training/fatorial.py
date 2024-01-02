def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

# Calcular o fatorial de 5
resultado = fatorial(4)

print(resultado)


# para facilitar vou importar a biblioteca math

import math

resultado = fatorial(5)

print(resultado)