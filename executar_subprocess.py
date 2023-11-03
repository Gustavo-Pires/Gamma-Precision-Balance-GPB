import subprocess

# Caminhos dos arquivos que você deseja executar
caminho_planilha = 'Planilha.py'
caminho_graficos = 'graficos_individual.py'

# Execute Planilha.py
subprocess.run(['python', caminho_planilha])

# Execute graficos_individual.py
subprocess.run(['python', caminho_graficos])
