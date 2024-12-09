import tkinter as tk
from tkinter import ttk
import random

# Função para começar/parar a rolagem de dados
def toggle_roll():
    global rolling
    if rolling:
        stop_rolling()
    else:
        start_rolling()

# Inicia a rolagem de dados
def start_rolling():
    global rolling, interval_id
    rolling = True
    start_stop_button.config(text="Pare de rolar")
    roll_dice()  # Chama a função que rola os dados repetidamente

# Para a rolagem de dados
def stop_rolling():
    global rolling
    rolling = False
    root.after_cancel(interval_id)  # Cancela o agendamento do próximo "tick"
    start_stop_button.config(text="Role os dados")

# Realiza a rolagem dos dados e atualiza os resultados
def roll_dice():
    global interval_id
    try:
        num_dice = int(num_dice_var.get())
        num_sides = int(num_sides_var.get())
    except ValueError:
        output_label.config(text="Erro: Insira números válidos.")
        return

    if num_dice < 1 or num_sides < 2:
        output_label.config(text="Erro: Dados inválidos.")
        return

    # Gerar resultados
    results = []
    total = 0
    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        results.append(f"Nº {i + 1}: {roll}")
        total += roll

    # Atualizar a interface com os resultados
    output_label.config(text=", ".join(results))
    total_label.config(text=f"Total: {total}")

    # Programar próxima atualização enquanto rolando
    if rolling:
        interval_id = root.after(100, roll_dice)

# Configuração inicial
root = tk.Tk()
root.title("Rolo de Dados Múltiplos")
root.geometry("400x300")
root.config(bg="#39b55c")

# Variáveis globais
rolling = False
interval_id = None

# Estilo
style = ttk.Style()
style.configure("TLabel", font=("Poppins", 12), background="#39b55c")

# Widgets
title_label = ttk.Label(root, text="Rolo de Dados Múltiplos", font=("Poppins", 16, "bold"))
title_label.pack(pady=10)

inputs_frame = tk.Frame(root, bg="#39b55c")
inputs_frame.pack(pady=10)

num_dice_var = tk.StringVar(value="1")
num_sides_var = tk.StringVar(value="6")

# Entrada: Número de dados
dice_label = ttk.Label(inputs_frame, text="Número de dados:")
dice_label.grid(row=0, column=0, padx=5, pady=5)
num_dice_entry = ttk.Entry(inputs_frame, textvariable=num_dice_var, width=5, justify="center")
num_dice_entry.grid(row=0, column=1, padx=5, pady=5)

# Entrada: Número de lados
sides_label = ttk.Label(inputs_frame, text="Número de lados:")
sides_label.grid(row=1, column=0, padx=5, pady=5)
num_sides_entry = ttk.Entry(inputs_frame, textvariable=num_sides_var, width=5, justify="center")
num_sides_entry.grid(row=1, column=1, padx=5, pady=5)

# Botão: Rolar dados
start_stop_button = tk.Button(root, text="Role os dados", command=toggle_roll, font=("Arial", 14, "bold"), background="#8EA302", foreground="#FFFFFF")
start_stop_button.pack(pady=10)

# Resultados
output_label = ttk.Label(root, text="", wraplength=350, anchor="center")
output_label.pack(pady=10)
total_label = ttk.Label(root, text="", font=("Poppins", 14, "bold"))
total_label.pack(pady=10)

# Iniciar aplicação
root.mainloop()
