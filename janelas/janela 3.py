import tkinter as tk
import webbrowser
import os
import sys

# Redireciona stdout para um dispositivo nulo para evitar output no console
sys.stdout = open(os.devnull, "w")

def open_help_link():
    webbrowser.open("https://github.com/Gustavo-Pires/Gamma-Precision-Balance-GPB/blob/main/Manual_GPB.pdf")

def finalizar():
    root.destroy()  # Fecha a janela principal ao clicar no botão "Finalizar"
    try:
        # Abre a imagem com o visualizador de imagens padrão do sistema operacional
        os.system('logo.png')  # Este comando é para sistemas Windows, ajuste conforme o sistema operacional do usuário
    except Exception as e:
        pass  # Trate qualquer exceção silenciosamente

# Janela principal
root = tk.Tk()
root.title("Gamma Precision Balance GPB")

largura = root.winfo_screenwidth() // 4
altura = root.winfo_screenheight() // 3
root.geometry(f"{largura}x{altura}")

# Botão de ajuda (posicionado no canto inferior esquerdo)
help_button = tk.Button(root, text="?", command=open_help_link, font=("Arial", 14))
help_button.place(x=10, y=altura-30)

# Texto "Calibração realizada com sucesso"
texto_calibracao = tk.Label(root, text="Calibração realizada com sucesso", font=("Arial", 16))
texto_calibracao.place(relx=0.5, rely=0.5, anchor='center')

# Botão "Finalizar" (centralizado na barra inferior)
finalizar_button = tk.Button(root, text="Finalizar", command=finalizar, font=("Arial", 14))
finalizar_button.place(relx=0.5, rely=1, anchor='s')

# Loop principal da aplicação
root.mainloop()
