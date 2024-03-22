import tkinter as tk
from tkinter import messagebox
import pickle


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
        self.tarefas[indice].concluida = not self.tarefas[indice].concluida

    def mostrar_tarefas(self):
        tarefas_formatadas = ""
        for i, tarefa in enumerate(self.tarefas):
            tarefas_formatadas += f"{i + 1}. {tarefa.descricao}\n"
        return tarefas_formatadas

    def salvar_tarefas(self, nome_arquivo):
        with open(nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.tarefas, arquivo)

    def carregar_tarefas(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'rb') as arquivo:
                self.tarefas = pickle.load(arquivo)
        except FileNotFoundError:
            pass


def adicionar_tarefa():
    descricao = entrada_tarefa.get()
    if descricao:
        lista_tarefas.adicionar_tarefa(descricao)
        atualizar_lista_tarefas()
        entrada_tarefa.delete(0, tk.END)


def remover_tarefa():
    indice = lista_tarefas_listbox.curselection()
    if indice:
        lista_tarefas.remover_tarefa(indice[0])
        atualizar_lista_tarefas()


def marcar_como_concluida():
    indice = lista_tarefas_listbox.curselection()
    if indice:
        lista_tarefas.marcar_como_concluida(indice[0])
        atualizar_lista_tarefas()


def atualizar_lista_tarefas():
    lista_tarefas_listbox.delete(0, tk.END)
    for tarefa in lista_tarefas.tarefas:
        lista_tarefas_listbox.insert(tk.END, f"[{'X' if tarefa.concluida else ' '}] {tarefa.descricao}")


def salvar_tarefas():
    lista_tarefas.salvar_tarefas(nome_arquivo)
    messagebox.showinfo("Salvar Tarefas", "Tarefas salvas com sucesso!")


# Configuração da janela principal
root = tk.Tk()
root.title("Gerenciador de Tarefas")

# Entrada de tarefa
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)
entrada_tarefa = tk.Entry(frame_entrada, width=50)
entrada_tarefa.pack(side=tk.LEFT, padx=5)
botao_adicionar = tk.Button(frame_entrada, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.pack(side=tk.LEFT)

# Lista de tarefas
frame_lista_tarefas = tk.Frame(root)
frame_lista_tarefas.pack(padx=10, pady=5)
lista_tarefas_listbox = tk.Listbox(frame_lista_tarefas, width=50, height=10)
lista_tarefas_listbox.pack(side=tk.LEFT, padx=5)
scrollbar_lista = tk.Scrollbar(frame_lista_tarefas, orient=tk.VERTICAL)
scrollbar_lista.config(command=lista_tarefas_listbox.yview)
scrollbar_lista.pack(side=tk.RIGHT, fill=tk.Y)
lista_tarefas_listbox.config(yscrollcommand=scrollbar_lista.set)

# Botões para remover, marcar como concluída e salvar
frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=5)
botao_remover = tk.Button(frame_botoes, text="Remover Tarefa", command=remover_tarefa)
botao_remover.pack(side=tk.LEFT, padx=5)
botao_concluir = tk.Button(frame_botoes, text="Concluir Tarefa", command=marcar_como_concluida)
botao_concluir.pack(side=tk.LEFT, padx=5)
botao_salvar = tk.Button(frame_botoes, text="Salvar Tarefas", command=salvar_tarefas)
botao_salvar.pack(side=tk.LEFT, padx=5)

# Inicializar lista de tarefas
lista_tarefas = ListaDeTarefas()
nome_arquivo = "tarefas.pkl"
lista_tarefas.carregar_tarefas(nome_arquivo)
atualizar_lista_tarefas()

# Executar aplicativo
root.mainloop()