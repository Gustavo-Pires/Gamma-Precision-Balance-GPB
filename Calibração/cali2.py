#---------------------------------------------BIBLIOTECAS ---------------------------------------------
import tkinter as tk
import tkinter.messagebox as messagebox
from datetime import datetime
from tkinter import PhotoImage
#import xlwings as xw
#------------------------------------------------------------------------------------------------------

root = tk.Tk()
root.title("Calibrator")

# Adicionando título centralizado
title = tk.Label(root, text="Hyperpure Germanium Detector(HPGe)-Calibration", font=("Arial", 16))
title.pack()

# Adicionando imagem
logo = PhotoImage(file="/Users/Gustavo/Desktop/logo.png")
logo = logo.subsample(int(logo.width()/300))
logo_label = tk.Label(root, image=logo)
logo_label.pack()

# Adicionando mensagem
version = tk.Label(root, text="Alpha Version- By Gustavo Pires Bertaco", font=("Arial", 10))
version.pack()

# criando um frame para os botões
frame = tk.Frame(root)
frame.pack()

# criando os botões e adicionando ao frame
calibrate_button = tk.Button(frame, text="Calibrate", command=root.destroy)
calibrate_button.pack(side=tk.LEFT)
cancel_button = tk.Button(frame, text="Cancel", command=root.destroy)
cancel_button.pack(side=tk.LEFT)


root.mainloop()
#---------------------------------------------LOG DO USUARIO ---------------------------------------------
root = tk.Tk()
root.title("Calibrator")

def get_name():
    name = entry.get()
    usuario.append(name)
    message = "Calibração feita por " + name
    messagebox.showinfo("Calibração", message)
    root.destroy()

label = tk.Label(root, text="What's your name?")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="OK", command=get_name)
button.pack()

root.mainloop()

# Create a table with the measurements
table = tk.Frame(root)
table.pack()

# Create the labels for the table
label_121 = tk.Label(table, text="121")
label_121.grid(row=0, column=0)
label_1332 = tk.Label(table, text="1332")
label_1332.grid(row=0, column=1)

# Create the entries for the table
entry_121_cont = tk.Entry(table)
entry_121_cont.grid(row=1, column=0)
entry_121_inc = tk.Entry(table)
entry_121_inc.grid(row=1, column=1)
entry_1332_cont = tk.Entry(table)
entry_1332_cont.grid(row=2, column=0)
entry_1332_inc = tk.Entry(table)
entry_1332_inc.grid(row=2, column=1)

#---------------------------------------------ARQUIVO DE CONTAGEM ---------------------------------------------
ws = xw.Book("cali.xlsx").sheets['Planilha1']
 
ekev = ws.range("A7:A107").value
ekev = [x.strip() for x in ekev if x is not None]
ekev = [x.replace(',', '.') for x in ekev]
ekev = list(map(float, ekev))

BG = ws.range("C7:C107").value
contagem = ws.range("D7:D107").value
incerteza = ws.range("E7:E107").value
canal =ws.range("E7:E107").value


#----------removendo celulas vazias----------
ekev= [x for x in  ekev if x is not None]
BG= [x for x in BG if x is not None]
resolucao= [x for x in BG if x is not None]
contagem= [x for x in contagem if x is not None]
incerteza= [x for x in incerteza if x is not None]
canal= [x for x in canal if x is not None]
#----------------------------------------------

#------------------------Cobalto 1332------------------------
Energia = 0
for num in ekev:
    if 1331.0 <= num <= 1333.0:
        Energia = num
        break

ekev_filtered = list(filter(lambda x: 1331 <= x <= 1333, ekev))
index = ekev.index(ekev_filtered[0])

ekev_1332 = ekev[index]
bg_1332 = BG[index]
contagem_1332 = contagem[index]
incerteza_1332 = incerteza[index]
canal_1332 = canal[index]
#---------------------------------------------------------------------

#---------------------------------------------LOG DE DATA E HORA ---------------------------------------------
current_time = datetime.now()
formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")
#------------------------------------------------------------------------------------------------------

#---------------------------------------------SALVANDO NA PLANILHA ---------------------------------------------
ws2= xw.Book("/Users/Gustavo/Documents/Calibracao.xlsx").sheets['Worksheet']

#------------------------Cobalto 1332------------------------
ekev_cont= ws2.range("A1:A31").options(numbers=str).value
BG_cont= ws2.range("B1:B31").options(numbers=str).value
contagem_cont= ws2.range("C1:C31").options(numbers=str).value
incerteza_cont= ws2.range("D1:D31").options(numbers=str).value
canal_cont=ws2.range("E1:E31").options(numbers=str).value
hora=ws2.range("F1:F31").options(numbers=str).value
usuario=ws2.range("G1:G31").options(numbers=str).value

ekev_cont= [x for x in  ekev_cont if x is not None]
BG_cont= [x for x in BG_cont if x is not None]
contagem_cont= [x for x in contagem_cont if x is not None]
incerteza_cont= [x for x in incerteza_cont if x is not None]
canal_cont= [x for x in canal_cont if x is not None]
hora= [x for x in hora if x is not None]
usuario= [x for x in usuario if x is not None]

ekev_cont.append(ekev_1332)
BG_cont.append(bg_1332)
contagem_cont.append(contagem_1332)
incerteza_cont.append(incerteza_1332)
canal_cont.append(canal_1332)
hora.append(formatted_time)


ws2.range("A1:A31").value = ekev_cont
ws2.range("B1:B31").value = BG_cont
ws2.range("C1:C31").value = contagem_cont
ws2.range("D1:D31").value = incerteza_cont
ws2.range("E1:E31").value = canal_cont
ws2.range("F1:F31").value = hora

#------------------------------------------------------------------------------------------------------



# Salvar dados na planilha
ws2.range("A1:A31").value = ekev_cont
ws2.range("B1:B31").value = BG_cont
ws2.range("C1:C31").value = contagem_cont
ws2.range("D1:D31").value = incerteza_cont
ws2.range("E1:E31").value = canal_cont
ws2.range("F1:F31").value = hora
ws2.range("G1:G31").value = usuario

# Verificar se a calibração é alta
limite=bg_1332[-1]
if limite > 400:
    messagebox.showerror("Calibração alta", "A calibração está muito alta, por favor verifique.")
    
ws = xw.Book("cali.xlsx").sheets['Worksheet']
