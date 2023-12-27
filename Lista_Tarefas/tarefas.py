class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

    def marcar_como_concluida(self):
        self.concluida = True

    def __str__(self):
        status = "✔" if self.concluida else "✘"
        return f"{status} {self.descricao}"


class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        nova_tarefa = Tarefa(descricao)
        self.tarefas.append(nova_tarefa)

    def remover_tarefa(self, indice):
        try:
            tarefa_removida = self.tarefas.pop(indice)
            print(f"Tarefa removida: {tarefa_removida}")
        except IndexError:
            print("Índice inválido. Tarefa não encontrada.")

    def exibir_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa na lista.")
        else:
            for i, tarefa in enumerate(self.tarefas):
                print(f"{i + 1}. {tarefa}")

    def marcar_tarefa_como_concluida(self, indice):
        try:
            tarefa = self.tarefas[indice]
            tarefa.marcar_como_concluida()
            print(f"Tarefa '{tarefa.descricao}' marcada como concluída.")
        except IndexError:
            print("Índice inválido. Tarefa não encontrada.")


# Exemplo de uso
lista_tarefas = ListaDeTarefas()

while True:
    print("\n=== Lista de Tarefas ===")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Exibir Tarefas")
    print("4. Marcar Tarefa como Concluída")
    print("5. Sair")

    escolha = input("Escolha uma opção (1-5): ")

    if escolha == "1":
        descricao = input("Digite a descrição da tarefa: ")
        lista_tarefas.adicionar_tarefa(descricao)
    elif escolha == "2":
        lista_tarefas.exibir_tarefas()
        indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
        lista_tarefas.remover_tarefa(indice)
    elif escolha == "3":
        lista_tarefas.exibir_tarefas()
    elif escolha == "4":
        lista_tarefas.exibir_tarefas()
        indice = int(input("Digite o número da tarefa concluída: ")) - 1
        lista_tarefas.marcar_tarefa_como_concluida(indice)
    elif escolha == "5":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
