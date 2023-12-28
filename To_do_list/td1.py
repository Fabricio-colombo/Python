import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

numero_tarefas = 0

def adicionar_tarefa():
    global numero_tarefas
    tarefa = entrada_tarefa.get()
    if tarefa:
        numero_tarefas += 1
        lista_tarefas.insert(tk.END, f"{numero_tarefas}. {tarefa}")
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Por favor, insira uma tarefa.")

def remover_tarefa():
    try:
        indice_selecionado = lista_tarefas.curselection()
        lista_tarefas.delete(indice_selecionado)
    except:
        messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para remover.")

janela = tk.Tk()
janela.title("To-Do List")

estilo = ttk.Style()
estilo.configure("TButton", padding=6, relief="flat", background="#ccc")
estilo.configure("TEntry", padding=6, relief="flat", background="#eee")

entrada_tarefa = ttk.Entry(janela, font=('Arial', 12))
botao_adicionar = ttk.Button(janela, text="Adicionar", command=adicionar_tarefa)
botao_remover = ttk.Button(janela, text="Remover", command=remover_tarefa)
lista_tarefas = tk.Listbox(janela, selectmode=tk.SINGLE, width=40, height=10, bg='#9b59b6', fg='white', font=('Arial', 12))

entrada_tarefa.pack(pady=10)
botao_adicionar.pack(pady=5)
botao_remover.pack(pady=5)
lista_tarefas.pack(padx=10, pady=10)

janela.mainloop()
