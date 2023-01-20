#---------------------------------------------BIBLIOTECAS ---------------------------------------------
import tkinter as tk
import tkinter.messagebox as messagebox
from datetime import datetime
#------------------------------------------------------------------------------------------------------

#---------------------------------------------LOG DO USUARIO ---------------------------------------------
root = tk.Tk()
root.title("Nome do usuário")

def get_name():
    name = entry.get()
    message = "Calibração feita por " + name
    messagebox.showinfo("Calibração", message)
    root.destroy()

label = tk.Label(root, text="Insira seu nome:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="OK", command=get_name)
button.pack()

root.mainloop()
#------------------------------------------------------------------------------------------------------

#---------------------------------------------LOG DE DATA E HORA ---------------------------------------------
current_time = datetime.now()
formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")
print(formatted_time)
#------------------------------------------------------------------------------------------------------