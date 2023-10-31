from tkinter import Tk
from tkinter.filedialog import askopenfilename

janela_padrao = Tk().withdraw()
caminho_do_arquivo = askopenfilename(filetypes = (("Arquivos Excel", "*.xlsx"), ("Arquivos Excel", "*.xls")))

print(caminho_do_arquivo)
