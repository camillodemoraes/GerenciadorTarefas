class Tarefa:
    def __init__(self, descricao, concluida=False):
        self.descricao = descricao
        self.concluida = concluida


class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def remover_tarefa(self, indice):
        del self.tarefas[indice]

    def marcar_como_concluida(self, indice):
        self.tarefas[indice].concluida = True

    def mostrar_tarefas(self):
        for i, tarefa in enumerate(self.tarefas):
            print(f"{i + 1}. [{'X' if tarefa.concluida else ' '}] {tarefa.descricao}")


lista_tarefas = ListaDeTarefas()

while True:
    print("\n== Gerenciador de Tarefas ==")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Marcar Tarefa como Concluída")
    print("4. Mostrar Tarefas")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        descricao = input("Digite a descrição da nova tarefa: ")
        lista_tarefas.adicionar_tarefa(descricao)
    elif escolha == '2':
        lista_tarefas.mostrar_tarefas()
        indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
        lista_tarefas.remover_tarefa(indice)
    elif escolha == '3':
        lista_tarefas.mostrar_tarefas()
        indice = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
        lista_tarefas.marcar_como_concluida(indice)
    elif escolha == '4':
        lista_tarefas.mostrar_tarefas()
    elif escolha == '5':
        break
    else:
        print("Opção inválida. Tente novamente.")
