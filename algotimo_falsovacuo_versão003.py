import tkinter as tk
from tkinter import messagebox
import time

# Função para calcular a média dos valores nas células mescladas
def calcular_media(celulas_mescladas):
    soma = sum(celulas_mescladas)
    media = soma / len(celulas_mescladas)
    return media

# Função para mesclar células e atualizar a interface
def mesclar_celulas(delta):
    if delta <= 1:
        messagebox.showinfo("Erro", "O valor de delta deve ser maior que 1")
        return

    for i in range(0, 25, delta):
        celulas_mescladas = []
        for j in range(i, i + delta):
            celulas_mescladas.append(j + 1)

        media = calcular_media(celulas_mescladas)

        for j in range(i, i + delta):
            label_values[j]['text'] = f'{media:.2f}'
            label_values[j]['bg'] = 'yellow'

        for k in range(i + 1, i + delta):
            label_values[k].grid_forget()

        root.update()
        time.sleep(3)

# Configuração da janela
root = tk.Tk()
root.title("Mesclar Células")

# Cria a tabela
frame = tk.Frame(root)
frame.pack()

label_values = [None] * 25

for i in range(5):
    for j in range(5):
        index = i * 5 + j
        label = tk.Label(frame, text=str(index + 1), relief="solid", width=10, height=3)
        label.grid(row=i, column=j)
        label_values[index] = label

# Solicita ao usuário o valor de delta
delta = int(input("Digite o valor de delta: "))

# Executa a mesclagem das células
mesclar_celulas(delta)

root.mainloop()
