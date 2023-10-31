from tkinter import Tk
from tkinter.filedialog import askopenfilename

janela_padrao = Tk().withdraw()
caminho_do_arquivo = askopenfilename(filetypes = [("Arquivos csv", "*.csv")])
print(caminho_do_arquivo)
