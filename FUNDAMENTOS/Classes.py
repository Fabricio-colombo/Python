# 1. Definição de uma Classe Simples
# class
class Pessoa:
    """Uma classe simples para representar uma pessoa."""

    def __init__(self, nome, idade):
        """Construtor da classe Pessoa."""
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        """Método para apresentar a pessoa."""
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# 2. Instância da Classe e Chamada de Método
# instanciação, chamada de método
pessoa1 = Pessoa("Alice", 25)
pessoa1.apresentar()

# 3. Herança de Classe
# class, herança
class Estudante(Pessoa):
    """Uma classe que herda de Pessoa e representa um estudante."""

    def __init__(self, nome, idade, curso):
        """Construtor da classe Estudante."""
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        """Método para apresentar o estudante."""
        print(f"Olá, sou {self.nome}, tenho {self.idade} anos e estudo {self.curso}.")

# 4. Instância da Classe Herdada
# instanciação, chamada de método
estudante1 = Estudante("Bob", 20, "Ciência da Computação")
estudante1.apresentar()

# 5. Atributos de Classe
# class
class ContaBancaria:
    """Uma classe com atributo de classe para contar o número de contas."""

    num_contas = 0

    def __init__(self, titular, saldo):
        """Construtor da classe ContaBancaria."""
        self.titular = titular
        self.saldo = saldo
        ContaBancaria.num_contas += 1

    def exibir_info(self):
        """Método para exibir informações da conta."""
        print(f"Titular: {self.titular}, Saldo: {self.saldo}")

# 6. Acesso a Atributo de Classe
# instanciação, acesso a atributo de classe
conta1 = ContaBancaria("Alice", 1000)
conta2 = ContaBancaria("Bob", 500)
print(f"Número total de contas: {ContaBancaria.num_contas}")
