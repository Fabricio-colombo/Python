# meu_modulo.py

def saudacao(nome):
    """Função que imprime uma saudação."""
    print(f"Olá, {nome}!")

mensagem = "Bem-vindo ao meu módulo!"

if __name__ == "__main__":
    print("Este é o código executável do módulo.")


'''
# meu_programa.py

import meu_modulo

meu_modulo.saudacao("Alice")
print(meu_modulo.mensagem)

if __name__ == "__main__":
    print("Este é o código executável do programa.")

'''