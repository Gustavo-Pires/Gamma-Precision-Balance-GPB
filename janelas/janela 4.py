import tkinter as tk
import webbrowser
import smtplib
from email.message import EmailMessage

# Função para abrir o link no navegador
def open_help_link():
    webbrowser.open("https://github.com/Gustavo-Pires/Gamma-Precision-Balance-GPB/blob/main/Manual_GPB.pdf")

# Função para enviar emails
def enviar_email():
    try:
        # Configurar o servidor SMTP (exemplo usando Gmail)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Autenticar com o servidor de email (substitua com seu endereço de email e senha)
        server.login('seu_email@gmail.com', 'sua_senha')

        # Criar a mensagem de email
        msg = EmailMessage()
        msg.set_content('Mensagem de teste.')
        msg['Subject'] = 'Assunto do Email'
        msg['From'] = 'seu_email@gmail.com'
        msg['To'] = ['destinatario1@example.com', 'destinatario2@example.com']  # Lista de destinatários

        # Enviar o email
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

# Criando a janela principal
root = tk.Tk()
root.title("Gamma Precision Balance GPB")

# Calculando as dimensões da janela
largura = 600
altura = 400
root.geometry(f"{largura}x{altura}")

# Botão de ajuda (posicionado no canto superior direito)
help_button = tk.Button(root, text="?", command=open_help_link, font=("Arial", 14))
help_button.place(x=largura - 40, y=10)

# Texto na janela
texto = "AVISO⚠️\nCalibração não realizada\nEntre em contato\nGustavo.pb@usp.br\ngzahn@ipen.br\npscsilva@ipen.br"
texto_label = tk.Label(root, text=texto, font=("Arial", 16), justify='center')
texto_label.place(relx=0.5, rely=0.5, anchor='center')

# Botão "Entrar em Contato" (centralizado na janela)
contato_button = tk.Button(root, text="Entrar em Contato", command=enviar_email, font=("Arial", 14))
contato_button.place(relx=0.5, rely=0.8, anchor='center')

# Loop principal da aplicação
root.mainloop()
