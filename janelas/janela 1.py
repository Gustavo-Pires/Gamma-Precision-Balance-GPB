import tkinter as tk
from tkinter import ttk
import webbrowser

# Função para abrir o link no navegador
def open_help_link():
    webbrowser.open("https://github.com/Gustavo-Pires/Gamma-Precision-Balance-GPB/blob/main/Manual_GPB.pdf")

# Função para ser chamada quando o botão "Iniciar Calibração" for pressionado
def iniciar_calibracao():
    # Coloque aqui o código para a próxima parte do seu programa
    pass

# Criando a janela principal
root = tk.Tk()
root.title("Gamma Precision Balance GPB")

# Definindo as dimensões da janela
largura = root.winfo_screenwidth() // 4
altura = root.winfo_screenheight() // 3
root.geometry(f"{largura}x{altura}")

# Carregando e redimensionando o logo (substitua "logo.png" pelo caminho correto para o seu arquivo)
logo = tk.PhotoImage(file="logo.png")
logo = logo.subsample(3)  # Redimensionando para 0.6 da escala original

# Calculando as coordenadas para centralizar o logo na janela
x_logo = (largura - logo.width()) // 2
y_logo = (altura - logo.height()) // 2

# Exibindo o logo na janela (centralizado)
logo_label = tk.Label(root, image=logo)
logo_label.place(x=x_logo, y=y_logo)

# Botão de ajuda (posicionado no canto inferior esquerdo)
help_button = tk.Button(root, text="?", command=open_help_link, font=("Arial", 14))
help_button.place(x=10, y=altura-30)

# Botão "Iniciar Calibração" simples, apenas com texto
start_button = tk.Button(root, text="Iniciar Calibração", command=iniciar_calibracao, font=("Arial", 16))
start_button.pack(side=tk.BOTTOM, pady=20)  # Posicionando na parte inferior central da janela

# Loop principal da aplicação
root.mainloop()
