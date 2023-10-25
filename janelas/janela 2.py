import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk

def open_help_link():
    webbrowser.open("https://github.com/Gustavo-Pires/Gamma-Precision-Balance-GPB/blob/main/Manual_GPB.pdf")

def finalizar():
    # Coloque aqui o código para finalizar o programa ou realizar outras ações necessárias
    pass

# Janela principal
root = tk.Tk()
root.title("Gamma Precision Balance GPB")

largura = root.winfo_screenwidth() // 4
altura = root.winfo_screenheight() // 3
root.geometry(f"{largura}x{altura}")

# Botão de ajuda (posicionado no canto inferior esquerdo)
help_button = tk.Button(root, text="?", command=open_help_link, font=("Arial", 14))
help_button.place(x=10, y=altura-30)

# Criando e exibindo o gráfico (logo.png)
image = Image.open("logo.png")
graph_image = ImageTk.PhotoImage(image)
graph_label = tk.Label(root, image=graph_image)
graph_label.place(relx=0.5, rely=0.5, anchor='center')

# Botão "Finalizar" (centralizado na barra inferior)
finalizar_button = tk.Button(root, text="Finalizar", command=finalizar, font=("Arial", 14))
finalizar_button.place(relx=0.5, rely=1, anchor='s')

# Loop principal da aplicação
root.mainloop()
